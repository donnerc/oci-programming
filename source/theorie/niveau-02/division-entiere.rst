Opérateurs division entière et reste
####################################

Vous avez :math:`666` allumettes que vous voulez répartir par boites de :math:`13`, combien de
boites pleines y aura-t-il ? S'il y a une boite non-pleine combien
d'allumettes contiendra-t-telle ?

Ces questions sont liées à ce qu'on appelle la division euclidienne (ou division entière), c'est-à-dire qu'on souhaite trouver nbBoites et nbReste tels que :


*	``666 = 13 * nbBoites + nbReste``
*	``0 <= nbReste < 13``

La première condition signifie qu'on ne perd aucune allumette et la seconde
que la boite non-pleine (si elle existe, c'est à dire si nbReste est différent
de 0) ne peut pas contenir 13 allumettes (elle serait pleine sinon).

En Python il est possible de calculer nbBoites et nbReste très facilement, à l'aide de deux nouveaux opérateurs :

	::

		>>> nbBoites = 666 // 13
		>>> nbReste = 666 % 13
		>>> print(nbBoites)
		51 
		>>> print(nbReste)
		3 

En terme de division euclidienne on a donc que, pour ``a`` et ``b`` deux
entiers :

*	``a // b`` donne le quotient de la division euclidienne de ``a`` par ``b``
*	``a % b`` donne le reste de la division euclidienne de ``a`` par ``b``

Que se passe-t-il si au lieu de :math: `666` on avait choisi un dividende négatif (on
supposera que le diviseur est positif) ?

On ne peut plus parler d'allumettes mais imaginons qu'on doive payer :math:`666` euros pour une anthologie de Heavy Métal (:math:`42` DVD !) et qu'on n'ait que des billets de :math:`50` euros. On va donc donner :math:`700` euros (soit :math:`14` billets) et on va nous rendre :math:`34` euros . Comme on paye quelque chose on a moins d'argent dans notre portefeuille, donc on perd de l'argent :

*	:math:`-666 = 50 * (-14) + 34`
*	:math:`0 \leq 34 < 50`

On a donc perdu 14 billets de 50 mais on a récupéré 34 euros.

Si on essaie d'écrire cela en Python, on a :

::

	>>> print(-666 // 50)
	-14 
	>>> print(-666 % 50)
	34 

La division euclidienne marche donc pour des nombres positifs et négatifs et
garantit que si on a

::	

	quotient = dividende // diviseur
	reste = dividende % diviseur

alors

..	math::

	dividende = diviseur * quotient + reste
	0 \leq reste < diviseur

Un exemple fréquent d'utilisation de ces opérateurs :

::

	nombre = int(input())
	if (nombre % 2) == 0:
	   print("Le nombre est pair")

En effet, si le reste vaut zéro c'est que nombre = 2 x quotient donc nombre
est divisible par 2.
