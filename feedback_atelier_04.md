# Feedback — Atelier 4 (Xavier CEGLINSKA)

## Respect de la consigne

Excellent rendu, complet et bien argumenté :

- `socket.socketpair()` ✓
- `with s1, s2:` ✓
- Tableau formaté pour `fileno()`, `getsockname()`, `getpeername()` ✓
- **Trois réponses détaillées et précises** dans un docstring :
  1. pourquoi adresses vides (AF_UNIX, pas de chemin assigné) ✓
  2. ce que signifie « anonyme » (pas d'adresse liée, pas
     accessible par nom) ✓
  3. différence avec TCP/IPv4 (adresse globale vs canal privé) +
     analogie utile avec `pipe` (mais full-duplex) ✓

Sur ta réponse 1, une précision : les sockets *sont* liés
(connectés) par le noyau — ils ne sont juste pas **nommés**. La
notion de « bind » s'applique à un nom externe. Tes phrases sont
correctes, c'est juste le mot « liés » qui peut prêter à
confusion (utilise « nommés » pour être plus précis).

## Côté Python (à titre indicatif)

- Structure propre : fonction `explore_socket_pair()` + garde.
- Le docstring à l'intérieur du `with` est *exécuté* (string
  littéral) — donc évalué puis jeté. C'est sans conséquence
  pratique mais idéalement, placer ces commentaires en docstring
  de module (en haut du fichier) ou en commentaires `#`.
- Fichier sans extension (`00_Atelier_4`) — préfère
  `atelier_04.py`.

---
*Évalué sur le commit `3536527` (fichier `00_Atelier_4`).*
