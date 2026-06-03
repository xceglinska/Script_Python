# Application Mini-Annuaire Réseau (Client / Serveur)

Ce projet implémente une architecture réseau Client/Serveur complète permettant de collecter, stocker et interroger des informations d'infrastructure système relatives à des noms de domaines internet (Adresse IPv4, Propriétaire/Contact Registrant, et adresse e-mail associée).

---

## Instructions d'installation

### 1. Dépendances système (Impératif)
L'application s'appuie sur la commande système native `whois` pour interroger les registres de noms de domaines. Assurez-vous qu'elle est installée sur votre machine hôte :

```bash
# Sur les distributions basées sur Debian/Ubuntu (Ex: Ubuntu, Linux Mint)
sudo apt update && sudo apt install whois -y

# Sur macOS (via Homebrew)
brew install whois
