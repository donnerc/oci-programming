Boucles
#######

Quiz
====

#)	Que fait le programme suivant :

	::

		i = 0
		while i != 0:
			i = i + 1
			print(i, end=" ")

	..	qcm::

		x 	Produit une erreur
		x 	Affiche ``0 1 2 3 4 5 6 7 8 9``
		x 	Affiche ``1 2 3 4 5 6 7 8 9``
		* 	Affiche ``1 2 3 4 5 6 7 8 9 10``
		x 	Ne s'arrête jamais

#)	Que fait le programme suivant :

	::

		i = 1
		while i != 10:
		      i = i + 2
		      print i

		..	qcm::

			x 	Produit une erreur
			x 	Affiche ``2 4 6 8``
			x 	Affiche ``1 3 5 7 9``
			x 	Affiche ``3 5 7 9``
			*	Ne s'arrête jamais

#)	Indiquer parmi les programmes donnés ci-dessous lesquels sont toujours
	équivalents au programme suivant :

	::

		while test:
			<instructions>

	..	qcm::

		*	::

			while test:
			    if False:
			        break
			    <instructions>
		x	::

			while test:
			    <instructions>
			    break
		x	::

			while True:
			    if test:
			        break
			    <instructions>
		*	::

			while test:
			    <instructions>
			    if <T>:
			        <instructions>
			    else:
			        break

Quiz 2 (terminaison de boucles)
-------------------------------

Pour chacune des boucles ci-dessous, cocher l'unique affirmation qui convient.

Boucle 1
++++++++

::  

    n = any positive integer
    i = 0
    while i <= n:
        i = i + 1

..  qcm::

    *   se terminer quelle que soit la valeur de la variable ``n`` avant l'exécution de la boucle
    x   il existe des valeurs pour ``n`` pour lesquelles la boucle ne se termine pas
    x   impossible à décider si la boucle se termine ou pas pour toute valeur de ``n``

Boucle 2
++++++++

::
    

    n = any positive integer
    i = 1
    while True:
        i = i * 2
        n = n + 1
        if i > n:
            break

..  qcm::

    *   se terminer quelle que soit la valeur de la variable ``n`` avant l'exécution de la boucle
    x   il existe des valeurs pour ``n`` pour lesquelles la boucle ne se termine pas
    x   impossible à décider si la boucle se termine ou pas pour toute valeur de ``n``                

Boucle 3
++++++++

::
    

    n = any positive integer
    while n != 1:
        if n % 2 == 0: #n is even
            n = n/2
        else:
            n = 3 * n + 1

..  qcm::

    x   se terminer quelle que soit la valeur de la variable ``n`` avant l'exécution de la boucle
    x   il existe des valeurs pour ``n`` pour lesquelles la boucle ne se termine pas
    *   il est impossible à décider si la boucle se termine ou pas pour toute valeur de ``n``

..  only:: corrige

    ..  note::

        Dire que la boucle se termine pour toute valeur de ``n`` serait un énoncé équivalent
        à la *Conjecture de Syracuse* (http://fr.wikipedia.org/wiki/Conjecture_de_Syracuse).

        Cette conjecture continue de défier les mathématiciens. On n'est donc pas
        sûr que cette boucle se termine pour tout entier :math:`n \in
        \mathbb{N}_{>0}`, mais on n'a jamais pu trouver un nombre :math:`n` pour
        lequel la boucle ne se termine pas.
