Charger un module
#################

Dans Python, toutes les fonctions (en particulier les fonctions mathématiques)
ne sont pas disponibles par défaut. Elles sont rangées dans ce qu'on appelle
des modules (ou bibliothèques) qu'on peut voir comme des "boites à outils".
Quand on veut utiliser un "outil" il faut d'abord "ouvrir la boite". Ainsi,
pour accéder aux fonctions mathématiques de façon simple on utilise la
commande suivante :

::

	from math import *

Elle peut se traduire par "importer tout ce qui est dans le module math".

Cette commande est à placer tout en haut du fichier et permet ensuite
d'utiliser dans votre programme toutes les fonctions ou constantes définies
dans ce module. On dit qu'on a importé le module.

Par exemple, pour un calcul de racine carrée :

::

	>>> from math import * 
	>>> print(sqrt(100))
	10.0
