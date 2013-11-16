Partie pratique
################

..  admonition:: Données personnelles

    *   Nom :
    *   Prénom :
    *   Date :
    *   Classe :

À rendre
========

Vous rendrez à une archive zip contenant les fichiers suivants 

*	``question_01.py`` (Programme python pour la question 1)
*	``question_02.py`` (Programme python pour la question 2)
*	``bonus.py`` (Programme python pour la question 2)

Merci de nommer votre archive avec le format suivant : ``NomPrenom-oci-examen1.zip`` en remplaçant ``Nom`` et ``Prenom`` par ce qui convient et de l'envoyer à l'adresse ``cedonner@gmail.com`` en mentionnant dans l'objet **Examen OCI**



Question 1
========

Compléter le programme suivant pour qu'il lise sur l'entrée standard un nombre
entier ``n`` et qu'il affiche la factorielle ``n!`` de ce nombre.

**Contrainte** : vous utiliserez une boucle ``while``

..	admonition:: Code à compléter

	..	code-block:: python 
		
		n = int(input())
		factorielle = ...

		# code à compléter 









		print(factorielle)


..	tip::

	*	:math:`5! = 5 \cdot 4 \cdot 3 \cdot 2 \cdot 1 = 120`
	*	:math:`n! = n \cdot (n-1) \cdot \ldots \cdot 2 \cdot 1`

Exemple
-------

..	admonition:: Entrée

	::

		5

..	admonition:: Sortie

	::

		120



Question 2 
==========

Noël approchant, vous êtes contactés par un décorateur pour générer des images
de sapins de différente taille. Les paramètres fournis au programme depuis
l'entrée standard sont les suivants :

*	``dessin`` : Caractère à utiliser (ici ``dessin = '#'``)
*	``hauteurTronc`` : nombre entier (ici ``hauteurTronc = 4``)
*	``largeurTronc`` : nombre entier (ici ``largeurTronc = 1``)
*	``hauteurTriangle`` : nombre entier indiquant la hauteur de la partie triangulaire du sapin (ici ``hauteurTriangle = 6``)


Exemple
-------

..	admonition:: Entrée

	::

		#
		4
		1
		6

..	admonition:: Sortie

	::
		     
		     #
		    ###
		   #####
		  #######
		 #########
		###########
		     #
		     #
		     #
		     #


BONUS
=====

..	admonition:: Entrée
	
	*	La première ligne contient un nombre entier ``nbNombres``
	*	Les ``nbNombres`` lignes suivantes contiennent toutes un nombre entier

Consigne
--------

Votre programme doit afficher sur 4 lignes différentes les éléments suivants :

*	Le nombre le plus grand de la liste
*	Le nombre le plus petit
*	Le nombre de multiples de 3
*	La moyenne des nombres arrondie à 3 chiffres après la virgule


Exemple
-------


..	admonition:: Entrée

	::

		6
		1
		3
		5
		3
		8
		9

..	admonition:: Sortie

	::

		 9
		 1
		 3
		 5.833