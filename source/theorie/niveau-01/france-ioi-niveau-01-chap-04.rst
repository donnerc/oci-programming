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