Utilisation d'un «compteur»
###########################

..	admonition:: Prérequis

	*	Instruction if dans une boucle for
	*	Opérations avec des variables

..	admonition:: Résumé

	Implémentation en Python d'une technique élémentaire d'algorithmique pour
	dénombrer à l'aide d'une variable initialement placée à 0 et qu'on
	augmente, en général, d'une unité, chaque fois qu'une certaine propriété
	se produit.

Problème-type
=============

On va illustrer la technique du compteur en se basant sur le problème suivant :

On donne une liste ``t`` d'entiers et on demande de donner le nombre d'entiers de
``t`` compris entre :math:`18` et :math:`65` au sens large. Par exemple, si ``t = [12, 81, 82, 9,
31, 65, 46]``, la réponse demandée est :math:`3`.

La technique
============

La technique est de principe très simple et s'assimile au fait de compter sur
ses doigts :

*	Au début du programme, on définit une variable, nommé par exemple ``cpt`` et initialisée à ``0``. À la fin du programme, la valeur de ``cpt`` sera le nombre recherché.
*	On parcourt la liste ``t`` avec la technique vue à l'unité **Boucle for : parcours d'une liste par indices**.
*	À chaque étape du parcours, on teste si l'élément courant est entre :math:`18` et :math:`65` au sens large. Si oui, on augmente de :math:`1` la valeur du compteur ``cpt``.
*	Dans le jargon, on dit parfois que la sélection par le critère « être entre 18 et 65 » est un **filtrage** et que l'augmentation du compteur d'une unité est une **incrémentation**

Le code
=======

Voici le code implémentant la technique du compteur pour le problème posé ci-dessus :

..	code-block:: python
	:linenos:

	t = [12, 81, 82, 9, 31, 65, 46]
	cpt = 0
	i = 0

	for loop in range(len(t)):
	    x = t[i]
	    if 18 <= x <= 65:
	        cpt = cpt +1
	    i = i + 1

	print(cpt)

..	admonition:: Sortie

	::

		3

*	Ligne 2 : variable compteur définie en début de programme et initialisée à ``0``
*	Ligne 6 : extraction de l'élément courant de la liste
*	Ligne 8 : incrémentation du compteur si (cf. ligne 7) l'élément courant de la liste satisfait le critère.
*	Ligne 9 : en fin de parcours, ``cpt`` contient le nombre requis.

Usage
=====

La technique du compteur est extrêmement fréquente en programmation. Elle s'utilise chaque fois que l'on veut déterminer le nombre de fois qu'une certaine propriété se rencontre et pas nécessairement en la présence d'une liste. En général, la technique du compteur est associée à une boucle.

