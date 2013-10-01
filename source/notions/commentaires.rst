Commentaires
############

Utilisation de commentaires
===========================

Lorsqu'un de vos programmes fait plus que quelques lignes, il est parfois difficile pour quelqu'un de le comprendre tout de suite (et ce quelqu'un peut très bien être vous-même quelques semaines plus tard !). Pour aider à comprendre la structure du programme et les difficultés qu'il contient, on peut écrire des commentaires dans son programme.

Un commentaire est un texte qui commence par le caractère ``#`` appelé dièse.

Il peut commencer tout au début d'une ligne ou bien être placé à la suite d'une instruction.

Dans tous les cas, tout le texte qui suit le ``#`` sera complètement ignoré lors de l'exécution du programme. Voici un exemple :

::

	# Ce programme a été écrit par Hermione Granger le 10/01/1994
	# Quatrième année, cours d'étude des moldus"
	 
	# Affiche un rectangle rempli de X 
	for loop in range(5):
	   for loop in range(10):
	      print("X", end = "")  # pas de retour à la ligne ici
	   print("")

..	admonition:: Bien programmer

	La priorité est toujours d'écrire le code le plus clair possible, pour qu'on puisse en comprendre un maximum sans explications. On réservera donc l'utilisation des commentaires aux explications des parties les plus complexes d'un programme.
