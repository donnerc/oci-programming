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

..  admonition:: Entrée

    ::

        11
        22

..  admonition:: Sortie

    ::

        1122 

Si on oublie le ``int(...)`` autour du ``input()``, les valeurs ne sont pas traitées comme des entiers mais comme du texte. Le symbole ``+`` agit alors comme un opérateur qui **concatène** (c'est-à-dire qui met bout à bout) deux textes, et du coup on obtient ``11`` collé à ``22`` (c'est-à-dire ``1122``) à la place de ``11`` additionné à ``22`` (c'est-à-dire ``33``).

Faîtes donc toujours attention à ne pas utiliser ``input()`` tout seul. De plus, si les résultats des calculs sont manifestement faux, pensez à vérifier si les nombres ne sont pas traités comme du texte.

Erreur si on lit trop de choses
-------------------------------

Une erreur qui peut se produire est d'essayer de lire trop de données.
Imaginons par exemple qu'il faille lire deux entiers et afficher leur produit
mais qu'on se soit trompé dans le programme et qu'on lise trois entiers :

::

    premierNombre = int(input())
    secondNombre = int(input())
    troisiemeNombre = int(input())
    print(premierNombre * secondNombre * troisiemeNombre)

..  admonition:: Sortie

    ::

        4
        5

        Traceback (most recent call last):
          File "./run/exe", line 3, in 
            troisiemeNombre = int(input())
        EOFError: EOF when reading a line

On sait que le programme n'est pas bon car il essaie de lire un troisième nombre qui n'existe pas, mais que signifie exactement cette erreur ?

``EOF`` est une abréviation pour **"End Of File"**, c'est-à-dire, si on traduit en français "Fin Du Fichier". **"EOFError: EOF when reading a line"** peut donc se traduire par "Erreur de Fin Du Fichier : fin du fichier atteinte alors qu'on essaie de lire une nouvelle ligne". Le "fichier" dont il est question ici est le fichier qui contient toutes les données que le programme va lire. Le message signifie donc qu'on a essayé de lire quelque chose (ici un entier) alors qu'on avait atteint la fin du fichier contenant les données à lire. Une erreur s'est donc produite.

On peut également remarquer que le message d'erreur nous indique exactement où cette erreur s'est produite, au moment d'exécuter la ligne

::

    troisiemeNombre = int(input())"

En résumé, si on obtient une erreur avec un ``EOF`` c'est qu'on a essayé de lire trop de choses.

Portée d'une variable
=====================

En Python toute variable déclarée au sein d'un programme peut être lue ou modifiée depuis n'importe quel endroit du programme. Par exemple :

::

    nbValeurs = int(input())
    for loop in range(nbValeurs):
       derniereValeurLue = int(input())
    print(derniereValeurLue)

..  admonition:: Entrée

    ::

        2
        10
        25

..  admonition:: Sortie

    ::

        25 


Ainsi, la variable ``derniereValeurLue``, déclarée au sein de la boucle, peut être affichée après la boucle. Cela peut vous sembler naturel, mais beaucoup de langages de programmation ne fonctionnent pas de cette manière.

On appelle **portée** d'une variable l'ensemble des endroits du programme où elle peut être utilisée, c'est-à-dire où elle existe. En Python, la portée d'une variable est donc tout le programme. Notez cependant que cette règle ne marchera plus complétement si votre programme contient des **fonctions**. Nous verrons cela plus tard dans le chapitre sur les fonctions.