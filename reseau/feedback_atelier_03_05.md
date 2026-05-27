# Feedback — Atelier 5 (R03 Socketserver, Xavier CEGLINSKA)

## Respect de la consigne

Très bien :

- `class ThreadedTCPServer(socketserver.ThreadingMixIn,
  socketserver.TCPServer)` — mixin en premier (commentaire
  explicatif inclus) ✓
- `MyThreadedHandler` hérite de `BaseRequestHandler` (au lieu de
  `StreamRequestHandler`) — utilise `self.request.recv()` /
  `self.request.sendall()`. Variante valide, mais
  `StreamRequestHandler` avec `self.rfile.readline()` aurait été
  plus dans l'esprit du chapitre.
- `time.sleep(2)` pour démontrer le parallélisme ✓
- log avec `threading.current_thread().name` — très utile pour
  visualiser le multi-thread.

**Détails** :

- Port 9999 au lieu de 8808 (sans conséquence).
- `recv(1024)` après `sleep(2)` : l'ordre inverse (recv puis
  sleep) serait plus intuitif (« je reçois, je traite »).

## Côté Python (à titre indicatif)

- Fichier sans extension (`03_Atelier_5`) — voir mes retours
  précédents.
- Commentaires pédagogiques bien placés.

---
*Évalué sur le commit `f799034` (fichier `reseau/03_Atelier_5`).*
