import argparse
import logging
import os
import sys
from dotenv import load_dotenv

# Importation des composants
import serveur
import client

def configurer_logging(niveau_verbosite: int):
    """
    Configure le module logging global selon le nombre de -v (Partie 5.2).
    """
    format_simple = "%(levelname)s: %(message)s"
    format_detaille = "[%s(asctime)s] [%(threadName)s] %(levelname)s [%(filename)s:%(lineno)d] - %(message)s"

    if niveau_verbosite == 0:
        logging.basicConfig(level=logging.WARNING, format=format_simple)
    elif niveau_verbosite == 1:
        logging.basicConfig(level=logging.INFO, format=format_simple)
    elif niveau_verbosite == 2:
        logging.basicConfig(level=logging.DEBUG, format=format_simple)
    else:
        logging.basicConfig(level=logging.DEBUG, format=format_detaille)


def executer_cli():
    """
    Construit la structure de la CLI et injecte la configuration .env (Partie 5.1 & 5.3).
    """
    # 1. Chargement de l'environnement .env
    load_dotenv()
    host_env = os.getenv("HOST", "127.0.0.1")
    port_env = int(os.getenv("PORT", "8888"))

    # 2. Définition des arguments CLI
    parser = argparse.ArgumentParser(
        description="Mini-annuaire réseau de domaines (Client/Serveur)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="count",
        default=0,
        help="Augmente le niveau de verbosité des logs (-v, -vv, -vvv)"
    )

    subparsers = parser.add_subparsers(dest="commande", required=True, help="Commandes disponibles")
    subparsers.add_parser("serve", help="Lance le serveur d'application")

    parser_search = subparsers.add_parser("search", help="Recherche un domaine enregistré")
    parser_search.add_argument("hote", type=str, help="Le nom d'hôte à rechercher")

    parser_record = subparsers.add_parser("record", help="Collecte et enregistre un domaine")
    parser_record.add_argument("hote", type=str, help="Le nom d'hôte à collecter")

    subparsers.add_parser("count", help="Nombre total de domaines")
    subparsers.add_parser("list", help="Liste des hôtes enregistrés")

    args = parser.parse_args()

    # 3. Activation des logs
    configurer_logging(args.verbose)
    logger = logging.getLogger("annuaire")

    # 4. Routage avec injection des variables d'environnement (Pas d'interblocage)
    try:
        if args.commande == "serve":
            logger.warning("Lancement du serveur sur %s:%d via .env", host_env, port_env)
            serveur.lancer(host=host_env, port=port_env)

        elif args.commande == "search":
            logger.info("Exécution SEARCH pour l'hôte : %s", args.hote)
            domaine = client.cmd_search(args.hote, host=host_env, port=port_env)
            if domaine:
                print(f"Hôte    : {domaine.hote}")
                print(f"IP      : {domaine.ip}")
                print(f"Contact : {domaine.contact}")
                print(f"Email   : {domaine.email}")
            else:
                print(f"Le domaine '{args.hote}' n'a pas été trouvé.", file=sys.stderr)

        elif args.commande == "record":
            logger.info("Exécution RECORD pour l'hôte : %s", args.hote)
            statut = client.cmd_record(args.hote, host=host_env, port=port_env)
            if statut == "OK":
                print(f"Succès : Le domaine '{args.hote}' a été enregistré.")
            elif statut == "ALREADY_EXISTS":
                print(f"Info : Le domaine '{args.hote}' existe déjà.")
            else:
                print(f"Erreur : {statut}", file=sys.stderr)

        elif args.commande == "count":
            logger.info("Exécution COUNT")
            total = client.cmd_count(host=host_env, port=port_env)
            print(f"Nombre de domaines enregistrés : {total}")

        elif args.commande == "list":
            logger.info("Exécution LIST")
            domaines = client.cmd_list(host=host_env, port=port_env)
            if domaines:
                print("Domaines enregistrés :")
                for d in domaines:
                    print(f" - {d}")
            else:
                print("Aucun domaine en base de données.")

    except Exception as e:
        logger.error("Erreur d'exécution critique : %s", e)
        sys.exit(1)


if __name__ == "__main__":
    executer_cli()
