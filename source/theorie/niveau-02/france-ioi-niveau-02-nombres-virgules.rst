Nombres à virgule
#################

Afficher un nombre à virgule
============================

En Python, les nombres à virgules (ou nombres décimaux) ne s'écrivent pas avec une "virgule" mais avec un "point", comme le font les anglais ou les américains. Ainsi, si on veut afficher le nombre "3,14" on va écrire le programme suivant :

::

    >>> print(3.14)
    3.14 

Déclarer un nombre à virgule
============================

Pour affecter à une variable une valeur décimale (c'est-à-dire non entière), ou pour faire des calculs, on fait comme pour les entiers.

::

    >>> prixJeu = 29.99
    >>> prixConsole = 299
    >>> print(prixJeu + prixConsole - 49.95)
    279.04 

Nombre à vigule : point et pas virgule !
========================================

Attention de bien utiliser un point et pas une virgule quand vous écrivez des
nombre "à virgule", sinon vous aurez des surprises. Regardons simplement
quelques exemples :

::

    >>> print((1,5) + 2)
    TypeError: can only concatenate tuple (not "int") to tuple


Autre cas possible :

::

    >>> print(1,5 + 2)
    1 7 

Il faut donc toujours utiliser un point pour les "nombres à virgule" !

Faire des divisions
===================

Comme en mathématiques, si on veut diviser deux nombres, on les sépare par le
symbole ``/``.

Il est très simple de diviser entre eux des nombres à virgule ou des entiers, on obtiendra toujours un nombre à virgule comme résultat :

::

    >>> print(10.5 / 3.5)
    3.0 
    >>> print(10 / 3)
    3.3333333333333335 
    >>> print(10 / 2)
    5.0 
    >>> print(10 / 4.5)
    2.2222222222222223 

Lecture de nombres à virgule
============================

Pour lire un nombre à virgule on utilise le code suivant :

::

    nombre = float(input())
    print(nombre * 2)

Cela ressemble donc beaucoup à la lecture d'un nombre entier, on utilise simplement ``float(input())`` au lieu de ``int(input())``.

..  note::

    La fonction python ``float()`` tente de convertir une valeur quelconque en
    un nombre à virgule flottante. En général, on utilise cette fonction avec une chaine de caractères ou un nombre entier : 

    ::

        >>> float(10)
        10.0
        >>> float("123.50")
        123.5

..  note::

    Le mot "float" vient de l'anglais "floating-point" qui signifie "à virgule flottante".

Lecture de décimaux : erreur possible
=====================================

Que se passe-t-il si on essaie de lire un entier alors que le nombre qu'on
nous donne est un nombre décimal ?

::

    >>> x = int(input())  # lecture de 12.34
    >>> print(x)
    ValueError: invalid literal for int() with base 10: '12.34'

Le programme s'attendait donc à lire un entier depuis l'entrée standard, mais
on lui a fourni un nombre décimal, ce qui a provoqué une erreur.
