# Feedback — S03/A5 (Convertisseur de températures, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : drapeaux `--from`/`--to` (avec `dest=` pour éviter le mot-clé Python `from`), `choices=["C","F","K"]`, conversion via un **pivot Celsius**.

Constat sur ton code :
- ✓ `--from` et `--to` déclarés avec `dest="depuis"` / `dest="vers"` pour contourner le conflit avec `from`.
- ✓ Pivot Celsius bien identifié : étape 1 convertit l'entrée vers Celsius, étape 2 va de Celsius vers la cible — l'architecture demandée est en place.
- ✓ Argument `valeur` positionnel typé `float`, et bonus pertinent avec `--precision` pour l'affichage formaté.
- ⚠ Les `choices` sont `["celsius", "fahrenheit", "kelvin"]` au lieu de `["C", "F", "K"]` attendus dans la consigne. C'est plus lisible mais ça oblige l'utilisateur à taper davantage et ça s'écarte du format demandé.

---
*Évalué sur le commit `ff9d769` (fichier `system/SYS_03_Atelier_5`).*
