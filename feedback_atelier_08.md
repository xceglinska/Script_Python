# Feedback — Atelier 8 (Xavier CEGLINSKA)

## Respect de la consigne

Très bien :

- `socket.socketpair()` ✓
- test 1 : `settimeout(0.2)` + `recv` + `TimeoutError` + mesure
  via `time.perf_counter()` ✓
- test 2 : `setblocking(False)` + `recv` + `BlockingIOError` +
  mesure ✓
- affichage des durées en ms ✓

**Manquant** : la **réponse écrite** à la question « pourquoi ne
peut-on pas tester aussi simplement le mode bloquant par défaut ?
Que faudrait-il pour le faire ? ». À ajouter en commentaire :

> En mode bloquant par défaut, `recv()` attend indéfiniment sur
> un socket vide → le script ne se termine jamais. Pour le
> tester, il faudrait introduire de la concurrence (un thread ou
> processus parallèle qui envoie des données ou ferme le socket
> après un délai), ce qui sort du périmètre de cet atelier.

## Côté Python (à titre indicatif)

- Fichier sans extension (`00_Atelier_8`) — à renommer en
  `atelier_08.py`.
- Structure : fonction + garde — bonne pratique.
- Code lisible.

---
*Évalué sur le commit `ca5e2a1` (fichier `00_Atelier_8`).*
