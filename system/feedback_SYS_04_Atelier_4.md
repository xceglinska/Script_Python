# Feedback — S04/A4 (Décomposition de chemins, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : fonction `decomposer(chemin)` retournant `(parent, stem, suffix)` via `pathlib.Path`, illustrée par 3 exemples dont une archive type `.tar.gz` et un fichier sans extension.

Constat sur ton code :
- ✓ Signature `decomposer(chemin_str: str) -> tuple[str, str, str]` typée proprement.
- ✓ Utilisation correcte de `Path.parent`, `Path.stem`, `Path.suffix`.
- ✓ Quatre exemples (au-delà du minimum demandé) : `/tmp/a.txt`, `/var/log/archive.tar.gz`, `/etc/hosts` (sans extension), `script_local.py`.
- ✓ Le commentaire signale honnêtement la limite de `.suffix` sur `.tar.gz` (renvoie `.gz` et stem = `archive.tar`).
- ✓ Tableau d'affichage aligné, lisible.

---
*Évalué sur le commit `70ec3da` (fichier `system/SYS_04_Atelier_4`).*
