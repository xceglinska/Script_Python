# Feedback — S07/A3 (Extraction tar.gz sécurisée, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : créer une archive `.tar.gz` factice (via `tempfile`), l'extraire vers une cible avec `tar.extractall(cible, filter="data")`, puis lister le contenu extrait.

Constat sur ton code :
- ✓ Ouverture en `tarfile.open(archive_path, "r:gz")` et appel à `extractall` — squelette correct.
- ✓ Préoccupation de sécurité bien présente : fonction `est_sur()` qui résout les chemins et bloque les remontées `..`/liens symboliques avant extraction.
- ⚠ Le mécanisme de sécurité repose sur un **filtrage manuel** des membres (`members=membres_suris`) au lieu du paramètre `filter="data"` ajouté en Python 3.12, qui fait exactement ce travail (et plus) en standard. La consigne attendait l'usage direct du filtre intégré.
- ⚠ Pas de génération d'archive factice via `tempfile` : ton script suppose qu'une archive existe déjà et la prend en argument CLI. Le scénario auto-portant (créer puis extraire dans la foulée) n'est pas implémenté.
- ⚠ Aucune étape de listing du contenu après extraction (la consigne demandait d'énumérer ce qui a été extrait, en plus du message de succès).

---
*Évalué sur le commit `01ddabe` (fichier `system/SYS_07_Atelier_3`).*
