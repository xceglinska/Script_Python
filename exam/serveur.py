import logging
import os
import socketserver
import sys
from dotenv import load_dotenv
from sqlalchemy.exc import IntegrityError

from collecte import collecter
from donnees import chercher, enregistrer, lister

logger = logging.getLogger(__name__)

# Chargement de la configuration via .env (Partie 5.3)
load_dotenv()
HOST = os.getenv("HOST", "127.0.0.1")
PORT = int(os.getenv("PORT", "8888"))


# partie 3 exo 2 + 3

class Handler(socketserver.StreamRequestHandler):

    def handle(self):
        logger.info("Connexion entrante : %s", self.client_address)
        for ligne in self.rfile:
            ligne = ligne.decode("utf-8").rstrip("\r\n")
            if not ligne:
                continue
            logger.debug("Commande reçue : %r", ligne)
            reponse = self._traiter(ligne)
            self.wfile.write((reponse + "\n").encode("utf-8"))

    def _traiter(self, ligne: str) -> str:
        parties = ligne.split(maxsplit=1)
        commande = parties[0].upper()
        argument = parties[1] if len(parties) > 1 else ""

        if commande == "SEARCH":
            return self._cmd_search(argument)
        elif commande == "RECORD":
            return self._cmd_record(argument)
        elif commande == "COUNT":
            return self._cmd_count()
        elif commande == "LIST":
            return self._cmd_list()
        else:
            return f"ERROR commande inconnue : {commande}"

    def _cmd_search(self, hote: str) -> str:
        if not hote:
            return "ERROR argument manquant"
        domaine = chercher(hote)
        if domaine is None:
            return "NOT_FOUND"
        return f"{domaine.hote}|{domaine.ip}|{domaine.contact}|{domaine.email}"

    def _cmd_record(self, hote: str) -> str:
        if not hote:
            return "ERROR argument manquant"
        if chercher(hote) is not None:
            return "ALREADY_EXISTS"
        try:
            domaine = collecter(hote)
            enregistrer(domaine)
            return "OK"
        except IntegrityError:
            return "ALREADY_EXISTS"
        except Exception as e:
            logger.warning("Erreur lors de la collecte de %s : %s", hote, e)
            return f"ERROR {e}"

    def _cmd_count(self) -> str:
        return str(len(lister()))

    def _cmd_list(self) -> str:
        domaines = lister()
        if not domaines:
            return ""
        return "|".join(d.hote for d in domaines)


class Serveur(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


def lancer(host: str = HOST, port: int = PORT):
    with Serveur((host, port), Handler) as serveur:
        logger.info("Serveur démarré sur %s:%d", host, port)
        try:
            serveur.serve_forever()
        except KeyboardInterrupt:
            logger.info("Arrêt du serveur.")
            sys.exit(0)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
    lancer()
