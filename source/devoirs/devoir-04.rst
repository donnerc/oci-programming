#####################################
Devoir 04 -- pour le mardi 01.10.2013
#####################################

Questions théoriques et de compréhension
========================================

#)	Déterminer, entre les deux programmes suivants, lequel est le plus
	élégant et le plus efficace pour résoudre l'exercice
	http://www.france-ioi.org/algo/task.php?idChapter=646&idTask=0&sTab=task&iOrder=9.
	**Justifier votre réponse !**

	*	Programme A

		::

			premierDe = int(input())
			secondDe = int(input())
			somme = premierDe + secondDe

			if somme >= 10:
			   print("Taxe spéciale !")
			   print(36)
			else:
			   print("Taxe régulière")
			   print(2 * somme)

	*	Programme B

		::

			de1 = int(input())
			de2 = int(input())

			if de1 + de2 >= 10:
			   print("Taxe spéciale !")
			   print(36)
			else:
			   print("Taxe régulière")
			   print(2* (de1 + de2))


Programmation
=============

*	Terminer le chapitre 7 sur les conditions avancées


Lecture (introduction à GitHub)
===============================

*	Lire le document :ref:`premiere-utilisation-github` et
	effectuer les opérations qui y sont décrites sur le site GitHub

*	Copier tous vos programmes concernant les problèmes de type
	**validation** des chapitres 5 à 7 dans votre *fork* du dépôt ``oci-prog-exos`` à l'aide de l'éditeur de code source intégré sur GitHub.

	..	note::

		Pour le chapitre 7, rendre tous les exercices du chapitre
