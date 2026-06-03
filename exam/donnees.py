import logging
from pathlib import Path

from sqlalchemy import create_engine, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

from collecte import Domaine

logger = logging.getLogger(__name__)

BDD_PATH = Path(__file__).parent / "domaines.db"


# partie 2 exo 1

class Base(DeclarativeBase):
    pass


class DomaineORM(Base):
    __tablename__ = "domaines"

    hote: Mapped[str] = mapped_column(String, primary_key=True)
    ip: Mapped[str | None] = mapped_column(String, nullable=True)
    contact: Mapped[str | None] = mapped_column(String, nullable=True)
    email: Mapped[str | None] = mapped_column(String, nullable=True)


# partie 2 exo 2

engine = create_engine(
    f"sqlite:///{BDD_PATH}",
    connect_args={"check_same_thread": False},
)
Base.metadata.create_all(engine)


def _nouvelle_session() -> Session:
    return Session(engine)


# partie 2 exo 3

def enregistrer(domaine: Domaine) -> None:
    with _nouvelle_session() as session:
        orm = DomaineORM(
            hote=domaine.hote,
            ip=domaine.ip,
            contact=domaine.contact,
            email=str(domaine.email) if domaine.email else None,
        )
        session.add(orm)
        try:
            session.commit()
            logger.info("Domaine enregistré : %s", domaine.hote)
        except IntegrityError:
            session.rollback()
            logger.warning("Domaine déjà présent : %s", domaine.hote)
            raise


def lister() -> list[Domaine]:
    with _nouvelle_session() as session:
        rows = session.query(DomaineORM).all()
        # model_construct permet de charger les objets sans déclencher les validateurs stricts
        return [
            Domaine.model_construct(hote=r.hote, ip=r.ip, contact=r.contact, email=r.email)
            for r in rows
        ]


def chercher(hote: str) -> Domaine | None:
    with _nouvelle_session() as session:
        row = session.get(DomaineORM, hote)
        if row is None:
            return None
        # model_construct sécurise la lecture concurrentielle réseau
        return Domaine.model_construct(hote=row.hote, ip=row.ip, contact=row.contact, email=row.email)


if __name__ == "__main__":
    import sys
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

    d = Domaine(hote="example.com", ip="93.184.216.34", contact="IANA", email=None)

    try:
        enregistrer(d)
        print("Enregistré.")
    except IntegrityError:
        print("Déjà présent.", file=sys.stderr)

    print("Liste :", lister())
    print("Chercher example.com :", chercher("example.com"))
    print("Chercher inconnu.fr :", chercher("inconnu.fr"))
