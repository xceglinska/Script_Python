# Feedback — Atelier 1 (Xavier XEGLINSKA)

## Respect de la consigne

Le contrat est rempli :

- argument CLI validé (`len(sys.argv) < 2`) avec message d'usage et
  `sys.exit(1)`,
- exception `socket.gaierror` rattrapée,
- IPv4 et IPv6 séparées dans deux listes,
- déduplication par `if adresse not in ipv4_list`,
- total cohérent : `len(ipv4_list) + len(ipv6_list)`,
- format de sortie conforme (`IPv4 : ...`).

Bonne copie sur le fond et la forme.

## Côté réseau

- Tu as bien identifié que `getaddrinfo` peut renvoyer des doublons
  (ta dédup explicite le prouve).
- Indexation par position (`item[0]`, `item[4][0]`) avec commentaire
  explicatif — pédagogique pour toi. Le dépaquetage nommé serait
  encore plus lisible :
  ```python
  for famille, _t, _p, _c, sockaddr in infos:
      adresse = sockaddr[0]
  ```
- Alternative à `not in liste` : un `set()`. Complexité O(1) au
  lieu de O(n) sur `in`. Pour ce volume aucune différence ; c'est
  pour la culture.

## Côté Python (à titre indicatif)

- Structure propre : `main()` + garde `if __name__ == "__main__":`.
- Commentaires didactiques, bien placés.
- Gestion d'erreur explicite et ciblée sur `socket.gaierror` — bien
  vu (plutôt qu'un `except Exception` trop large).

---
*Évalué sur le commit `ec0cc2e` (fichier `reseau/00_Atelier_1`).*
