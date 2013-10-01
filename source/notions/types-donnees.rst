Types de base
#############

..	admonition:: Prérequis

	*	Afficher

..	admonition:: Résumé

	*	entier
	*	flottant
	*	booléen
	*	chaîne.

La notion de type
=================

Les objets manipulées par un programme Python ont un type, au sens d'un
langage de programmation : un type correspond à une catégorie d'objets
(entiers, nombres réels, valeurs logiques, etc).

Exemples de types
=================

On va décrire les types les plus usuels.

..	code-block:: python
	:linenos:

	print(42)
	print(4 + 6)
	print(-5 * 2)

	print(421.5)
	print(2.7 + 10)                         

	print(421 > 42)
	print(421 < 42)

	print("toto")

..	admonition:: Sortie

	..	code-block:: txt
		:linenos:

		42
		10
		-10
		421.5                                   
		12.7
		True
		False
		toto

*	Lignes 1-3 : type entier. Les entiers peuvent être positifs comme négatifs.
*	Lignes 5-6 : type flottant. Pour simplifier, il s'agit de nombres dit « à virgule », ci-dessus représentés en base 10. Le point utilisé dans le nombre représente notre virgule décimale (« flottant » fait allusion à la notion de virgule « flottante »).
*	Lignes 8-9 et 17-18 : type booléen. Une expression de type booléen a une valeur de vérite True ou False.
*	Ligne 11 : le type chaîne. En première approximation, une chaîne représente une suite de caractères. Dans l'exemple, pour que Python reconnaisse le mot toto comme une donnée de type chaîne, on entoure le mot d'une paire de guillemets.

Usage des types en Python
=========================

Python est un langage typé : toute donnée utilisée possède un type (entier,
flottant, complexe, chaîne de caractères, etc). Le langage Python contient de
très nombreux types (plusieurs dizaines).

En Python, le type est un outil plutôt théorique et détermine en partie

*	les opérations qu'on peut effectuer entre données
*	les valeurs que peuvent prendre les données.

Par exemple

::

	print(3 * "Hello")                      

..	admonition:: Sortie

	..	code-block:: txt
		:linenos:

		HelloHelloHello

*	Ligne 1 : on peut « multiplier » (avec l'opérateur ``*``) un entier (ici 3) et une chaîne (``"Hello"``) :

Soit maintenant le code :

..	code-block:: python
	:linenos:

	print(3 + "Hello")

..	admonition:: Sortie

	..	code-block:: txt
		:linenos:

		Traceback (most recent call last):
		  File "somme_chaine.py", line 1, in <module>
		    print(3 + "Hello")
		TypeError: unsupported operand type(s) for +: 'int' and 'str'

*	Ligne 1 : on veut « additionner » un entier et une chaîne
*	Lignes 2-5 : on obtient un message TypeError (ligne 5) ce qui signifie une erreur de type : on ne peut pas « additionner » un entier et une chaîne (cf. ligne 1).

On voit donc que certaines opérations sont possibles et d'autres pas : le
typage permet entre autres de savoir qu'elles sont les opérations permises ou
pas.

Le typage en Python est réel et même assez complexe mais d'importance pratique
secondaire. Quand on débute en Python, l'existence de types est peu
importante. Même lorsqu'on est plus avancé, l'utilisation explicite de types
est plutôt à éviter.
