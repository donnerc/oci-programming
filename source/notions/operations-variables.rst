Opérations avec des variables
#############################

..	admonition:: Prérequis

	Opérations sur les nombres Affichage et variables

..	admonition:: Résumé

	Intérêt pratique des variables. Modification de variable, réaffectation.

Opérations usuelles
===================

Quand on veut récupérer (« sauvegarder ») le résultat d'un calcul, on le place
dans une nouvelle variable.

..	code-block:: python
	:linenos:

	x = 42
	y = 5
	z = (x * y + 5) * (x ** 2 + y **2 ) - 100
	u = (z - 10000) * x

..	admonition:: Sortie

	::

		print(u)

qui affiche :

--output--

	15730470                                

*	Lignes 3 : on stocke sous le nom de ``z`` le résultat d'un calcul en mémoire
*	Lignes 4 : on stocke sous le nom de ``u`` le résultat d'un autre calcul
*	Ligne 6 : on affiche le contenu de la variable

Variable modifiée ou pas ?
==========================

Une opération utilisant une variable n'affecte pas le contenu de la variable :

..	code-block:: python
	:linenos:

	toto = 42
	print(toto + 1)                         
	print(toto)

..	admonition:: Sortie

	::

		43                                      
		42

*	Ligne 2 : on ajoute ``1`` à la valeur de ``toto``. Le résultat (ici 43) est affichée mais ce calcul est « perdu » puisque la valeur n'est pas replacé dans une variable et n'est donc pas réutilisable par la suite du programme.
*	Ligne 5 : bien qu'on ait ajouté ``1`` à ``toto``, le contenu de la variable ``toto`` reste inchangé par rapport à sa valeur initiale.

Réaffectation
=============

Il peut arriver qu'un calcul avec une variable, disons ``x``, soit suivi de la modification de la valeur de la variable ``toto``.

..	code-block:: python
	:linenos:

	x = 42
	x = 2 * x + 10                          
	print(x)

..	admonition:: Sortie

	::

		94                                      

*	Ligne 2 : L'expression $2 * x + 10$ est évaluée et la valeur obtenue (94) est réaffectée à ``x``. Ce type d'affectation (ligne 1 vs ligne 2) s'appelle une réaffectation. La valeur initiale d'affectation (ici 42) est « perdue ».
Augmenter de ``1`` la valeur d'une variable (comme ``toto`` ci-dessous) s'appelle une **incrémentation**.

..	code-block:: python
	:linenos:

	toto = 42
	print(toto)

	toto = toto + 1                         
	
	..	admonition:: Sortie

		::

			42                                      
			43

*	Ligne 4 : ``toto + 1`` est évalué et la valeur obtenue (43) est réaffectée à ``toto``.

..	note::

	La pratique de la réaffectation est extrêmement courante.