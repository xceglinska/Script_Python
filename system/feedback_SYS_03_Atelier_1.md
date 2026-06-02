# Feedback — S03/A1 (Mini-calculatrice argparse, CEGLINSKA Xavier)

## Respect de la consigne

Critères attendus : `argparse` avec 3 arguments positionnels (`float`, `choices=["+","-","*","/"]`, `float`), division par zéro traitée par message sur `stderr` et `sys.exit(1)`.

Constat sur ton code :
- ✓ Trois positionnels déclarés dans l'ordre : `nb1` (`type=float`), `op` (`choices=["+", "-", "*", "/"]`), `nb2` (`type=float`).
- ✓ Validation de l'opérateur déléguée à `argparse` via `choices`.
- ✓ Division par zéro interceptée avant le calcul : message sur `sys.stderr` puis `sys.exit(1)`.
- ✓ Affichage final propre `f"{args.nb1} {args.op} {args.nb2} = {resultat}"`.
- ⚠ Tu testes `args.nb2 == 0` au lieu de laisser remonter une `ZeroDivisionError` ; les deux approches sont valides, la tienne évite carrément le calcul.

---
*Évalué sur le commit `ff9d769` (fichier `system/SYS_03_Atelier_1`).*
