Chapitre 4 -- lecture de l'entrée
##################################

Introduction
============

Lire des entiers
-----------------

On souhaite écrire un programme demandant deux entiers à l'utilisateur, la longueur et la largeur d'un rectangle, et qui affiche l'aire du rectangle. En Python on fera ainsi :

::

    longueur = int(input())
    largeur = int(input())

    print(longueur * largeur)

Analyse du programme
-----------------

La ligne

::

    longueur = int(input())

est celle qui permet de récupérer l'entier donné par l'utilisateur (qui correspond à la longueur du rectangle) et de le stocker dans la variable longueur. Il en est de même avec la ligne suivante pour la largeur du rectangle.

Comme ``int`` signifie "entier" et ``input`` signifie ici récupérer, ``int(input())`` se lit "récupérer un entier". On demande à Python de nous donner la valeur du prochain entier qu'indiquera l'utilisateur.

Entrée et espaces
------------------

Lorsqu'on fournit les entrées au programme, il faut faire bien attention de donner un et un seul entier par ligne, sans espaces après les entiers.

Erreurs possibles
=================

Erreur si l'on ne donne pas un entier 
-------------------------------------

Imaginons que le programme demande un entier mais que l'utilisateur fournisse un texte, par exemple "coucou". Bien sûr, le programme produit une erreur, car "coucou" ne peut pas être interprété comme un nombre.

::

    taille = int(input())
    print(taille)

    
Si on fournit en entrée la chaine de caractères ``"coucou"`` à ce programme, il va se produire l'erreur suivante :

::

    ValueError: invalid literal for int() with base 10: 'coucou'

Notez qu'une erreur similaire peut se produire si vous ajoutez des espaces autour d'un nombre.

Lecture d'entiers : autres erreurs possibles
--------------------------------------------

Si on oublie le ``int(...)`` et que l'on écrit juste ``input()`` à la place de ``int(input())``, on peut avoir de grosses surprises, comme le montre l'exemple suivant.

::

    valeur1 = input()                
    valeur2 = input()
    print(valeur1 + valeur2)

Avec l'entrée

::

    11
    22

On aurait comme sortie

::

    1122 

Si on oublie le ``int(...)`` autour du ``input()``, les valeurs ne sont pas traitées comme des entiers mais comme du texte. Le symbole ``+`` agit alors comme un opérateur qui concatène (c'est-à-dire qui met bout à bout) deux textes, et du coup on obtient ``11`` collé à ``22`` (c'est-à-dire ``1122``) à la place de ``11`` additionné à ``22`` (c'est-à-dire ``33``).

Faîtes donc toujours attention à ne pas utiliser ``input()`` tout seul. De plus, si les résultats des calculs sont manifestement faux, pensez à vérifier si les nombres ne sont pas traités comme du texte.