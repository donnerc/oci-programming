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