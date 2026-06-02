# Feedback — S06/A2 (Backup horodaté, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : `shutil.copytree` vers un dossier `backup_<YYYYMMDD_HHMMSS>/`.

Constat sur ton code :
- ✓ Appel `shutil.copytree(source, destination)` — la copie récursive en une ligne, c'est exactement l'API attendue.
- ✓ Horodatage généré par `datetime.now().strftime("%Y%m%d_%H%M%S")` et nom de dossier `backup_{timestamp}`, conforme au format demandé.
- ✓ Vérifications préalables solides : existence (`source.exists()`) et type (`source.is_dir()`) avec messages explicites.
- ✓ Destination placée dans le dossier parent de la source — choix raisonnable.
- ⚠ **Bug**: ligne 37, `destination.rgob("*")` — typo, il faut lire `rglob("*")`. Le `try/except Exception` rattrape silencieusement l'`AttributeError` après que la copie a réussi, donc tu obtiens un message d'erreur au lieu du compte de fichiers. À corriger.

---
*Évalué sur le commit `01ddabe` (fichier `system/SYS_06_Atelier_2`).*
