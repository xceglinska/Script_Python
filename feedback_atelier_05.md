# Feedback — Atelier 5 (Xavier CEGLINSKA)

## Respect de la consigne

Très propre :

- `recv_ligne(sock)` lit octet par octet, arrêt sur `b"\n"`,
  délimiteur non inclus ✓
- gestion de la fin de flux (sortie de boucle si `recv(1)`
  retourne `b""`) ✓
- test avec `socketpair`, envoi correct, deux appels `recv_ligne`
  via `with` ✓

**Point manquant** : pas de réponse au bonus (« pourquoi
inefficace ? quelle structure pour optimiser ? »). C'est un point
optionnel mais important pour la suite du cours. À ajouter :

> Inefficace car chaque `recv(1)` provoque un appel système
> (passage utilisateur → noyau → utilisateur, ~1 μs). Pour une
> ligne de 100 octets, 100 appels au lieu d'un seul. Structure
> d'optimisation : un buffer interne (`bytearray`), avec lecture
> par blocs (`recv(4096)`) et recherche du `\n` avec `.find()`.

## Côté Python (à titre indicatif)

- Code lisible, bons commentaires.
- Structure : fonction `recv_ligne` + fonction `test_framing` +
  garde — bonne pratique.

---
*Évalué sur le commit `ac6ca5a` (fichier `00_Atelier_5`).*
