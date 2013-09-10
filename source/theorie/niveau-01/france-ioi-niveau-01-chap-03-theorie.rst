Chapitre 3 -- calculs et variables
##################################

Mémoriser des informations
==========================

Principe
--------

Supposons que l'on souhaite écrire un programme qui affiche d'abord la distance qui séparait la Terre et Mars le 27 Août 2003 (55'758'000 km), puis la distance à parcourir par la lumière pour faire l'aller-retour depuis la Terre (le double). On pourrait écrire le programme ainsi :

 

::

    print(55758000)
    print(2 * 55758000)

::

    55758000 
    111516000 

Ce programme fonctionne parfaitement bien, mais il n'est pas idéal car on a dû écrire deux fois le nombre ``55758000 dans le code du programme. Cela signifie que si on veut afficher ces informations pour un autre jour, pendant lequel la distance entre les deux planètes est différente, il faudra modifier le programme à deux endroits différents.

Pour éviter de devoir faire des modifications en double, on va utiliser une **variable**, appelée ``distance``, pour stocker la valeur ``55758000``. Grâce à cette variable, on peut réécrire le programme précédent en ne faisant apparaître qu'une seule fois le nombre ``55758000`` :

::

    distance = 55758000
    print(distance)
    print(2 * distance)

::

    55758000 
    111516000

Le programme fonctionne exactement comme avant. Peu importe qu'il soit un peu plus long, ce qui compte vraiment, c'est qu'on a maintenant deux fois moins de chance de se tromper lorsqu'on modifie la distance.

On peut voir une variable comme une boîte qui porte un nom et qui contient quelque chose : on peut y stocker des informations et les retrouver plus tard. Dans notre exemple, la boîte porte le nom ``distance`` et contient la valeur ``55758000``.

Une boîte contenant un nombre

La boîte ``distance`` a été créée par l'instruction suivante, qui s'appelle une **affectation** :

::

    distance = 55758000

Les deux instructions d'affichage ont consulté le contenu de la boîte distance pour y lire la valeur ``55758000``.

::

    print(distance)
    print(2 * distance)

Plusieurs variables
-------------------

Dans l'exemple ci-dessus, nous avons utilisé une seule variable, mais les programmes en utilisent généralement plusieurs. Le programme suivant illustre cela : il utilise deux variables nommées ``largeur`` et ``longueur`` afin de calculer l'aire, en mm2 d'une feuille A4 (21cm x 29,7cm), et il enregistre le résultat dans une variable nommée surface. Le contenu de cette variable est ensuite affiché.

::

    largeur = 210
    longueur = 297

::

    surface = longueur * largeur
    print(surface)

::

    62370 

Débogage : variables inexistantes
==================================

Si on utilise une variable qui n'existe pas encore, on obtient une erreur. Par exemple, le programme suivant définit une variable longueur, et tente ensuite d'afficher le contenu d'une variable nommée largeur qui n'a jamais été définie. ::

    longueur = 297
    print(largeur)

::

    NameError: name 'largeur' is not defined

Il faut faire particulièrement attention au fait que les minuscules et majuscules ne sont pas considérées comme équivalentes. Ainsi, la variable nommée longueur n'a strictement rien à voir avec la variable nommée Longueur.

::

    longueur = 10
    print(Longueur)

::

    NameError: name 'Longueur' is not defined

Si on rencontre une erreur de la forme ``NameError: name 'xxxxx'`` is not defined, on pensera à bien vérifier que l'on n'a pas fait de faute de frappe dans les noms de variables que l'on a utilisés dans le programme.