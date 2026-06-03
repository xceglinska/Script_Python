import logging
import socket
from collecte import Domaine

logger = logging.getLogger(__name__)

# Configuration par défaut conforme au sujet
DEFAULT_HOST = "127.0.0.1"
DEFAULT_PORT = 8888
TIMEOUT = 5.0  # Évite de bloquer indéfiniment (Partie 4)


def recv_ligne(sock: socket.socket) -> str:
    """
    Lit le socket octet par octet jusqu'à rencontrer le caractère de fin de ligne '\\n'.
    Option requise pour le Protocole A (Partie 4).
    """
    donnees = bytearray()
    while True:
        octet = sock.recv(1)
        if not octet:
            # Le socket a été fermé par le serveur prématurément
            break
        donnees.extend(octet)
        if octet == b'\n':
            break
    return donnees.decode("utf-8").rstrip("\r\n")


def envoyer_commande(commande_brute: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> str:
    """
    Gère le cycle de vie complet d'une connexion socket bas niveau :
    Connexion, envoi de la ligne, réception de la réponse et fermeture.
    """
    # Utilisation obligatoire de socket.socket (pas de socketserver ici)
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(TIMEOUT)  # Protection anti-blocage obligatoire
    
    try:
        s.connect((host, port))
        logger.debug("Connecté au serveur %s:%d", host, port)
        
        # Envoi de la commande avec le délimiteur de fin de ligne
        requete = f"{commande_brute}\n"
        s.sendall(requete.encode("utf-8"))
        
        # Lecture de l'unique ligne de réponse
        reponse = recv_ligne(s)
        logger.debug("Réponse brute reçue : %r", reponse)
        return reponse

    except ConnectionRefusedError:
        logger.error("Erreur : Impossible de se connecter au serveur sur %s:%d. Vérifiez qu'il est lancé.", host, port)
        raise
    except socket.timeout:
        logger.error("Erreur : Le serveur n'a pas répondu dans le délai imparti de %s secondes.", TIMEOUT)
        raise
    finally:
        s.close()


# --- Fonctions exposées par commande (Exigence du sujet) ---

def cmd_search(hote: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> Domaine | None:
    """
    Envoie la commande SEARCH au serveur.
    Retourne une instance de Domaine Pydantic si trouvé, ou None si NOT_FOUND.
    """
    try:
        reponse = envoyer_commande(f"SEARCH {hote}", host, port)
        if reponse == "NOT_FOUND" or reponse.startswith("ERROR"):
            return None
        
        # Découpage selon notre délimiteur pipe '|'
        parts = reponse.split("|")
        if len(parts) == 4:
            # Reconstruction sécurisée du modèle Pydantic
            return Domaine.model_construct(
                hote=parts[0],
                ip=parts[1] if parts[1] != "None" else None,
                contact=parts[2] if parts[2] != "None" else None,
                email=parts[3] if parts[3] != "None" else None
            )
    except Exception:
        pass
    return None


def cmd_record(hote: str, host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> str:
    """
    Envoie la commande RECORD au serveur pour lancer la collecte et l'enregistrement.
    Retourne la chaîne de statut renvoyée par le serveur ('OK', 'ALREADY_EXISTS', 'ERROR ...').
    """
    try:
        return envoyer_commande(f"RECORD {hote}", host, port)
    except Exception as e:
        return f"ERROR {e}"


def cmd_count(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> int:
    """
    Envoie la commande COUNT au serveur.
    Retourne le nombre entier de domaines enregistrés.
    """
    try:
        reponse = envoyer_commande("COUNT", host, port)
        return int(reponse)
    except Exception:
        return 0


def cmd_list(host: str = DEFAULT_HOST, port: int = DEFAULT_PORT) -> list[str]:
    """
    Envoie la commande LIST au serveur.
    Retourne la liste des noms d'hôtes sous forme de liste Python de chaînes de caractères.
    """
    try:
        reponse = envoyer_commande("LIST", host, port)
        if not reponse:
            return []
        # Extraction de la ligne unique délimitée par les pipes '|'
        return reponse.split("|")
    except Exception:
        return []


if __name__ == "__main__":
    # Petit test d'intégration autonome du client
    logging.basicConfig(level=logging.DEBUG, format="%(levelname)s: %(message)s")
    
    print("--- Test des commandes clientes (Le serveur doit être lancé) ---")
    try:
        print("Enregistrement de google.com :", cmd_record("google.com"))
        print("Nombre de domaines :", cmd_count())
        print("Recherche google.com :", cmd_search("google.com"))
        print("Liste des hôtes :", cmd_list())
    except Exception as err:
        print(f"Échec du test : {err}")
