# Feedback — Atelier 7 (Xavier CEGLINSKA)

## Respect de la consigne

Tout est rendu correctement :

- octets bruts ✓
- valeur 1 big-endian via `struct.unpack("!I", ...)` ✓
- valeur 2 little-endian via `struct.unpack("<I", ...)` ✓
- valeur 3 inversion + big-endian via `donnees[::-1]` +
  `unpack(">I", ...)` ✓
- vérification automatique des valeurs 2 et 3 ✓

**Manquant** : la **réponse écrite** au « Pourquoi ? ». Tu
affiches « valeurs 2 et 3 sont IDENTIQUES » mais sans expliquer
la raison. À ajouter en commentaire :

> Lire en little-endian (de droite à gauche) revient à inverser
> physiquement les octets puis lire en big-endian (de gauche à
> droite). Dans les deux cas, on traite les octets dans le même
> ordre logique (du plus significatif au moins significatif).

## Côté Python (à titre indicatif)

- Structure : fonction `etude_boutisme()` + garde — bonne
  pratique.
- Fichier sans extension (`00_Atelier_7`) — voir mes retours
  précédents.
- Code lisible.

---
*Évalué sur le commit `ac6ca5a` (fichier `00_Atelier_7`).*
