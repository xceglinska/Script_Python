# Feedback — Atelier 3 (Xavier CEGLINSKA)

## Respect de la consigne

Très complet et propre :

- argparse avec `--protocole tcp|udp` requis ✓
- TCP : `with` + `settimeout(1)` + capture séparée de
  `ConnectionRefusedError`, `socket.timeout`, et fallback générique
  → messages clairs et différenciés ✓
- UDP : `sendto` + vérification `> 0` + message conforme ✓
- Commentaires pertinents (« Port 1 : généralement
  fermé/privilégié ») qui montrent que tu comprends pourquoi ce
  port est utilisé.

`except Exception as e:` en fallback est OK pour ne pas masquer
des erreurs imprévues à l'évaluation, mais en production on
préfère lister les types attendus pour ne pas dissimuler de bugs.

Note technique : `socket.timeout` est un alias historique de
`TimeoutError`. Sur Python 3.10+, on peut écrire directement
`except TimeoutError:`. Aucun problème de fond.

## Côté Python (à titre indicatif)

- Structure très lisible : `main()` + garde
  `if __name__ == "__main__":`.
- Le fichier s'appelle `00_Atelier_3` (sans extension). À
  renommer en `atelier_03.py` pour la cohérence et la
  reconnaissance par les outils Python.

---
*Évalué sur le commit `3536527` (fichier `00_Atelier_3`).*
