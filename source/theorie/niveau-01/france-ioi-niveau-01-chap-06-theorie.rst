Chapitre 6 : Structures avancées
################################

Structures imbriquées
=====================

Vous avez déjà appris que, lorsqu'on place une boucle de répétition à l'intérieur d'une autre boucle de répétition, la boucle imbriquée (celle qui se situe à l'intérieur de l'autre) doit avoir tout son code indenté (décalé vers la droite). De la même manière, il faut indenter correctement le code lorsqu'un test (``if`` ou ``if/else``) est placé à l'intérieur d'une boucle de répétition ou d'un autre ``if``, ou bien lorsqu'une boucle de répétition est placé à l'intérieur du corps d'un test.

Le programme suivant illustre cela dans le cas d'une boucle de répétition placé à l'intérieur d'un ``if``. Ce programme lit un entier nommé cible. Si cible est un nombre positif, le programme affiche tous les entiers compris entre ``1`` et ``cible`` à l'aide d'une boucle de répétition. Sinon, le programme affiche le texte ``"Rien à faire"``.

::

	cible = int(input())
	if cible >= 0:
	   valeur = 1
	   for loop in range(cible):
	      print(valeur)
	      valeur = valeur + 1
	else:
	   print("Rien à faire")

Observez la manière dont est indenté le code qui se trouve entre le ``if`` et le ``else``.

