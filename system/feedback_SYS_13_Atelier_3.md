# Feedback — S13 Atelier 3 (Token URL-safe, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : `secrets.token_urlsafe(32)`, écriture/relecture dans un `.env` temporaire, comparaison via `secrets.compare_digest`

Constat sur ton code :
- ✓ `secrets.token_urlsafe(32)` bien utilisé.
- ✓ `tempfile.TemporaryDirectory()` avec `Path(tmpdir) / ".env"`, écriture au format `TOKEN=...`.
- ✓ Relecture, extraction via `contenu.partition("=")` (avec une petite vérif `if cle == "TOKEN"`, bien vu).
- ✓ Comparaison via `secrets.compare_digest` — pas de `==`, parfait.
- ⚠ `import os` non utilisé, tu peux le retirer.
- ⚠ Détail : le fichier n'a pas d'extension `.py` (consigne demandait `atelier_03.py`).

Atelier maîtrisé, tu as ajouté la vérif explicite sur la clé.

---
*Évalué sur le commit `68321f7` (fichier `system/SYS_13_Atelier_3`).*
