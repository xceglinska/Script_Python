# Feedback — Atelier 6 (Xavier CEGLINSKA)

## Respect de la consigne

Excellent rendu :

- `recv_exactement(sock, n)` gère les `recv` partiels et lève
  `ConnectionError` sur EOF ✓
- `envoyer_message` : préfixe 4 octets en big-endian via
  `struct.pack("!I", ...)` + `sendall` ✓
- `recevoir_message` : lit 4 octets, décode, lit la quantité
  voulue ✓
- test avec `socketpair`, 3 messages, **vérification par assert**
  ✓

C'est un rendu modèle. Les docstrings et les commentaires
(« Big-Endian / Unsigned Int (4 octets) ») montrent que tu
comprends ce que tu fais.

## Côté Python (à titre indicatif)

- Structure : `recv_exactement` + `envoyer_message` + `recevoir_message`
  + `test_protocole_binaire` + garde — propre.
- Fichier sans extension (`00_Atelier_6`) — à renommer en
  `atelier_06.py`.

---
*Évalué sur le commit `915e367` (fichier `reseau/00_Atelier_6`).*
