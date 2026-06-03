# Mini-Annuaire Réseau (Client / Serveur)

Ce projet est une application réseau permettant de collecter, stocker et interroger des informations sur des noms de domaines (IP, contact, e-mail).

## 🏢 Description des Scripts

* **`annuaire.py`** : La télécommande principale (CLI). C'est le seul script à lancer. Il permet de démarrer le serveur ou d'envoyer des ordres en tant que client.
* **`serveur.py`** : Gère la ligne réseau, écoute les demandes des clients et y répond en tâche de fond (multi-threadé).
* **`client.py`** : Se connecte brièvement au serveur pour lui envoyer une commande (`RECORD`, `SEARCH`, `LIST`, `COUNT`) et afficher le résultat.
* **`collecte.py`** : L'enquêteur informatique. Il extrait l'IP du domaine et interroge le registre mondial (`whois`).
* **`donnees.py`** : Le classeur (Base de données). Il s'occupe de sauvegarder et lire proprement les informations dans un fichier SQLite (`domaines.db`).

---

## 🛠️ Librairies à installer

### 1. Outil système (Requis pour l'enquête Whois)
Avant toute chose, l'ordinateur doit disposer de l'outil système `whois` :
```bash
# Sur Linux (Ubuntu/Debian)
sudo apt update && sudo apt install whois -y

# Sur macOS
brew install whois
```
### 2. librairie python 
```
pip install pydantic

pip install email-validator

pip install sqlalchemy

pip install python-dotenv
```
