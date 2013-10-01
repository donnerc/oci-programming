Boucle while
############

..	admonition:: Prérequis

	*	

..	admonition:: Résumé


Un problème typique
===================

Étant donné un entier :math:`n`, on cherche un entier noté m qui soit le
premier multiple de 10 supérieur ou égal à :math:`n`. Si par exemple
:math:`n=42` alors :math:`m=50` : en effet, :math:`50` est bien un multiple de
10 et il n'y en pas d'autre entre :math:`42` et :math:`50`. Voici d'autres
exemples :

:math:`n`	2013	420	0
:math:`m`	2020	420	0

L'idée à implémenter
--------------------

Les multiples de :math:`10$ sont les entiers : $0,10,20,30$ etc. Ils s'écrivent sous la forme $10k$ où $k$ varie à partir de $0`.

Pour trouver :math:`m$, on parcourt les multiples de $10$ depuis $0$ et on s'arrête une fois qu'on a atteint ou dépassé l'entier n donné. Autrement dit, on énumère les multiples $m$ de $10$ tant que $m<n$. Le parcours est montré dans le tableau ci-dessous où on suppose que $n=42`.

..	list-table::

	-	*	:math:`k`
		*	:math:`0`
		*	:math:`1`
		*	:math:`2`
		*	:math:`3`
		*	:math:`4`
		*	:math:`5`
	-	*	:math:`10k<n ?`
		*	oui
		*	oui
		*	oui
		*	oui
		*	oui
		*	non


Implémentation en Python
========================

La notion de « dès que », « une fois que » ou de « tant que » est traduite dans le code Python par l'instruction while.

Le code suivant répond au problème posé :


:file:`while_typique.py`
------------------------

..	code-block:: python
	:linenos:

	n = 42
	k = 0

	while 10 * k < n:                       
	    k = k + 1

	print(10 * k)
	while_typique.py.output

..	admonition:: Sortie

	50                                      

On voit (cf. lignes 7 et 8) que la solution au problème est 50.

Analyse de code
===============

On passe en revue le code de :file:`while_typique.py`.

Vocabulaire de la boucle while
------------------------------

La boucle ``while`` se trouve aux lignes 4-5. Ces deux lignes forment une
seule et même instruction, dite instruction ``while``. Ligne 4 : l'en-tête de
la boucle ``while`` est la partie qui commence avec ``while`` et se termine
avant le séparateur ``:`` (deux-points). Ce qu'on appelle le corps de la
boucle ``while`` est tout le bloc indenté (ici ligne 5) qui est sous les deux-
points. Répétition

Une boucle ``while`` répète une action (ligne 5) tant qu'une condition , ici
(cf. ligne 4) :

::
	
	10 * k < n

reste vraie. Plus précisément, si la condition est vraie, l'exécution entre
dans le corps de la boucle et à la fin du corps de la boucle, la condition est
à nouveau testée (d'où le terme de boucle) si la condition est fausse,
l'exécution du programme va au-delà du corps de la boucle, ici à la ligne 6.

Variable de contrôle
--------------------

Une boucle ``while`` fait souvent appel à une variable de contrôle, ici :math:`k`, qui
évolue pendant la boucle. Typiquement,

*	cette variable est initialisée avant la boucle, ici ligne 2
*	cette variable est réaffectée, dans le corps de la boucle while, ici par l'instruction ligne 5
*	la condition à tester (ici ligne 4) est différente d'un tour de boucle à l'autre car elle dépend de k qui, entre-temps, a varié.

Remarques
---------

*	Lignes 4 : dans l'immense majorité des cas, le corps d'une boucle ``while`` est indenté.
*	Il est possible de faire d'autres essais de code en changeant juste la valeur
	de n à la ligne 1. Par exemple, si on change ``n`` en ``2013``, le programme affichera
	``2020``.

*	Il se peut que l'exécution du code n'entre même pas dans le corps de la boucle
	``while``. Par exemple, si ligne 1, on choisit ``n=0`` au lieu de ``n=42``, le test ``10 * k < n`` 
	(ligne 4) échoue immédiatement et donc le programme continue à la ligne 6 sans même passer par la ligne 5.

Comprendre comment s'exécute une boucle while
=============================================

Modifions le code précédent :file:`while_typique.py` pour mieux comprendre l'exécution de la boucle ``while``:

..	code-block:: python
	:linenos:

	n = 42
	k = 0
	print("avant while", "k=", k)
	print()

	while 10 * k < n:
	  print("debut while", "k=", k, "10*k=", 10*k)
	  k = k + 1
	  print("fin while", "k=", k)
	  print()
	print("apres while")
	print(10 * k)

..	admonition:: Sortie

	avant while : k= 0

	debut while : k= 0 10*k= 0
	fin while : k= 1

	debut while : k= 1 10*k= 10             
	fin while : k= 2

	debut while : k= 2 10*k= 20
	fin while : k= 3

	debut while : k= 3 10*k= 30
	fin while : k= 4

	debut while : k= 4 10*k= 40
	fin while : k= 5

	apres while
	50

En plus du code initial, :file:`while_typique_affichage.py` contient des instructions
d'affichage (lignes 3, 7, 9 et 11) et des instructions de sauts de ligne
(lignes 4 et 10) dans la sortie pour observer l'évolution de ``k`` et de ``10 * k``
avant, pendant et après la boucle while.

L'exécution du programme est la suivante :

*	Lignes 2 et 7 : la valeur de ``k`` avant le commencement de la boucle ``while``
*	Ligne 6 : k vaut 0. Le test de la boucle ``while`` est effectué : a-t-on ``0 < 42`` ? La réponse est oui donc, l'exécution du code continue dans le corps de la boucle ``while``
*	Lignes 7-10 et lignes 15-16: Les affichages sont effectués : ``k`` est changé de ``0`` à ``1``.
*	Ligne 6 : le test de la boucle ``while`` est à nouveau effectué : a-t-on ``10<42`` ? La réponse est oui et l'exécution entre à nouveau dans le corps de la boucle. Cette opération se répète jusqu'à ce que ``k = 5`` (ligne 8 et lignes 18-28).
*	Ligne 6 : le test de la boucle ``while`` est effectué : a-t-on ``50<42`` ? Cette fois, la réponse est non donc l'exécution quitte la boucle et continue lignes 11 et 12, cf. lignes 30 et 31.
*	Ligne 12 : le résultat affiché (cf. ligne 31) est bien le résultat demandé. Comme le test ``10 * k < n`` a échoué pour la première fois, c'est qu'on a ``10 * k >= n`` avec ``k`` minimal et c'est bien ce que l'on cherchait.