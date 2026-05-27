# Feedback — Atelier 2 (Xavier CEGLINSKA)

> **Note du formateur (mise à jour 2026-05-27)** : la présence ou
> l'absence de `AF_UNIX` n'est **plus prise en compte** dans la
> notation. Plusieurs étudiants travaillent sous Windows où cette
> famille de sockets n'est pas (ou peu) supportée. Les remarques
> ci-dessous qui critiquaient l'absence ou le remplacement de
> `AF_UNIX` (par `AF_INET6` notamment) sont à considérer comme
> **caduques**.


## Respect de la consigne

Bien rempli :

- les trois sockets demandés (TCP, UDP, AF_UNIX),
- `with` imbriqué (trois niveaux explicites),
- `fileno()`, `family.name`, `type.name` imprimés,
- réponse à la question correcte (descripteur unique par
  ressource OS, pas de partage).

Détails appréciables : tu mets une **note d'environnement** en
en-tête (`AF_UNIX` indisponible sur Windows) et tu **vérifies
dynamiquement** avec `hasattr(socket, 'AF_UNIX')`. C'est plus
robuste que de planter sans message. Le tableau formaté
(`{'TYPE':<15} | {'FILENO':<8} | …`) est très lisible.

L'explication peut être un cran plus précise : ce n'est pas
seulement « identifiant distinct par socket », c'est le **plus
petit entier libre** dans la table des descripteurs du processus.
C'est cette règle qui produit la séquence 3, 4, 5 que tu peux
observer.

## Côté Python (à titre indicatif)

- Le fichier s'appelle `00_Atelier_2` (sans extension `.py`).
  L'interpréteur lit le contenu sans problème, mais les outils
  Python (linters, IDE, formateurs) ne le reconnaissent pas. Je
  recommande `atelier_02.py` (ou `00_Atelier_2.py`).
- Structure propre : `create_sockets()` + garde
  `if __name__ == "__main__":`.

---
*Évalué sur le commit `f9c2cf3` (fichier `reseau/00_Atelier_2`).*
