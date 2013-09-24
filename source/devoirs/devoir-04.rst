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


