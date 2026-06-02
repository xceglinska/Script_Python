# Feedback — S05/A3 (Logger horodaté, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : écriture en mode `"a"` (append) dans un fichier de log, avec horodatage en tête de chaque entrée.

Constat sur ton code :
- ✓ Ouverture en `open("app.log", "a", encoding="utf-8")` — append correct, encodage explicite.
- ✓ Horodatage ISO via `datetime.now().isoformat(timespec="seconds")` — format normalisé et lisible.
- ✓ Concaténation `sys.argv[1:]` pour accepter aussi bien un message entre guillemets qu'une suite de mots.
- ✓ Gestion d'erreur d'écriture avec `try/except OSError` et sortie sur `stderr`+`exit(1)`.
- ✓ Garde `if len(sys.argv) < 2` avec message d'usage clair.

---
*Évalué sur le commit `a342f9a` (fichier `system/SYS_05_Atelier_3`).*
