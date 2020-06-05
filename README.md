# Template pour la rédaction de thèse

Dossier issu des templates de David Leh et Florian Huet (docteurs au laboratoire SYMME).
Ce dossier final est une fusion des fonctionnalités de chacun des templates (regroupement de fonctionnalités) et avec la mise à jour des packages devenus obsolètes par Jean Collomb.
Un dossier pour les notebook de chaque chapitre a été ajouté pour créer des figures à la bonne taille du manuscrit avec une police automatique adéquate et lisible.


## Fonctionnement

* Le fichier "manuscrit.tex" (dossier manuscrit) est le document maître.
* Il suffit de rédiger des les fichiers .tex de chacun des dossiers, puis d'excécuter le fichier maître.
* Il est possible d'ajouter ou de supprimer des dossiers/fichiers (par exemple des chapitres). Il suffit d'ajouter/désactiver les lignes correspondantes dans le fichier "manuscrit.tex".
* Le dossier Notebooks permet de créer pour chaque chapitre un notebook dédié.
* Dans le notebook Chap donné en exemple, des exemples de figures sont proposés pour créer des figures adaptées à la largeur du document dans latex, ainsi que des options de tailles, couleurs et styles pour une bonne lisiblité. Les tailles de police sont automatiques. Le mode LaTeX est activé dans le notebook dans matplotlib pour écrire des équations dans les figures.

## Modifications autres
* Spécialité du doctorat peut être modifiée dans le fichier "meta-donnees.sty".
* Laboratoire peut être modifié dans le fichier "meta-donnees.sty".
* Ecole doctorale peut être modifiée dans le fichier "meta-donnees.sty".
* Des packages peuvent être ajoutés dans le fichier "packages.tex".
* Les couleurs (Tableaux, références, liens ...) peuvent être modifiés dans le fichier "packages.tex" via le package "hyperref".
