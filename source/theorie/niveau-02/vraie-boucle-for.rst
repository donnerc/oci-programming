La boucle ``for``
###############

Introduction
============

Ce cours est une première ébauche d'un futur chapitre sur la boucle ``for``. Il
n'est pas (encore) accompagné d'exercices d'application mais un certain nombre
d'exemples sont fournis.

Son but est de vous présenter le fonctionnement de la "boucle for" qui va
désormais remplacer la "boucle de répétition" que vous utilisiez jusqu'à
présent.

La "vraie" boucle
=================

Pour afficher les nombres de 0 à 9, c'est-à-dire de 0 (inclu) à 10 (non inclu)
vous utilisez actuellement le code suivant :

::

	nombre = 0
	for loop in range(10):
	   print(nombre)
	   nombre = nombre + 1

Eh bien, sachez qu'il est également possible de faire ainsi :

::

	for loop in range(10):
	   print(loop)

Ce que nous ne vous avions donc pas encore dit c'est que ``loop`` est en fait une
variable ! On peut donc l'utiliser comme n'importe quelle variable, en
particulier pour l'afficher. On peut également utiliser un autre nom de
variable (``loop`` n'étant pas très clair). Ainsi on écrira plutôt :

::

	for nombre in range(10):
	   print(nombre)

En pratique ``range(10)`` se comporte comme la suite de valeurs 0, 1, ..., 9
et ce code revient à dire :

::

	Pour chaque valeur dans [0, 1, ..., 9] affecter cette valeur à la variable "nombre" et
	   Afficher la variable "nombre"

Dans la suite de ce cours nous allons voir la puissance de cette écriture qui
permet d'avoir des programmes plus courts et compacts.

Cas général
===========

Le fonctionnement de ``range()`` est en réalité un peu plus complexe que cela et
sous sa forme générale, il s'utilise ainsi :

::

	for nombre in range(<debut>, <fin>, <saut>):
	   ...

ce qui va faire prendre à la variable nombre toutes les valeurs entre ``<debut>``
(inclu) et ``<fin>`` (non inclu) en faisant des sauts de <saut> à chaque fois.
Pour bien comprendre, le mieux est de regarder quelques exemples :

Afficher les nombres de 0 à 9
-----------------------------

::

	for nombre in range(0, 10, 1):
	   print(nombre, end = " ")

..	admonition:: Sortie
	
	::

		0 1 2 3 4 5 6 7 8 9 

On va donc de 0 (inclu) à 10 (non inclu, c'est-à-dire 9 inclu) en faisant "+1"
entre chaque valeur.

Afficher les nombres de 10 à 20
-------------------------------

::

	for nombre in range(10, 21, 1):
	   print(nombre)

..	admonition:: Sortie
	
	::

		10 11 12 13 14 15 16 17 18 19 20 

On va donc de 10 (inclu) à 21 (non inclu, c'est-à-dire 20 inclu) en faisant
"+1" entre chaque valeur.

Afficher les nombres pairs de 100 à 120
---------------------------------------

::

	for nombre in range(100, 121, 2):
	   print(nombre)

..	admonition:: Sortie
	
	::

		100 102 104 106 108 110 112 114 116 118 120 

On va donc de 100 (inclu) à 121 (non inclu, c'est-à-dire 120 inclu) en faisant
"+2" entre chaque valeur.

Afficher les multiples de 5 de 20 à -20
---------------------------------------

On veut donc afficher des nombres de manière décroissante, donc le "saut" est
négatif

::

	for nombre in range(20, -21, -5):
	   print(nombre)

..	admonition:: Sortie
	
	::

		20 15 10 5 0 -5 -10 -15 -20 

On va donc de 20 (inclu) à -21 (non inclu, c'est-à-dire -20 inclu) en faisant
"-5" entre chaque valeur.

Interprétation
--------------

On commence donc par la valeur de début et tant qu'on est strictement plus
petit (si le saut est positif) / grand (si le saut est négatif) que la valeur
de fin, on passe d'une valeur à la valeur suivante en faisant le "saut"
indiqué.

Notez que toutes les variations suivantes sont donc équivalentes !

::

	range(10, 101, 5)
	range(10, 102, 5)
	range(10, 103, 5)
	range(10, 104, 5)
	range(10, 105, 5)

Elle vont toutes afficher les multiples de 5 entre 10 et 100.

Formes réduites
===============

Saut non précisé
----------------

S'il n'est pas précisé, le "saut" vaut 1, on peut donc écrire

::

	for nombre in range(100, 201):
	   ...

à la place de

::

	for nombre in range(100, 201, 1):
	   ...

Ces deux codes sont équivalents.

Début et saut non précisé
-------------------------

Si on à un "début" égal à 0 et un "saut" égal à 1, alors il existe une
écriture plus courte. Ainsi :

::

	for nombre in range(0, 10, 1):
	   ...

peut être remplacé par

::

	for nombre in range(10):
	   ...

C'est la forme que vous connaissiez et que vous utilisiez jusqu'à présent.
Elle permettait bien de répéter 10 fois une suite d'instruction puisque
range(10) contient les valeurs 0, 1, ..., 9 soit 10 valeurs au total.
