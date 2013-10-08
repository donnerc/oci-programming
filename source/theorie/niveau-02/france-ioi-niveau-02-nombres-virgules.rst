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


Des calculs approchés
=====================

Quand on travaille avec des nombres à virgule, le résultat affiché n'est pas
toujours exact, car seulement 17 chiffres (avant ou après la virgule) seront
conservés au maximum :

::

    >>> print(2 / 3)
    0.6666666666666666 

Le fait que les nombres puissent être arrondis donne parfois lieu à des
résultats surprenants, comme l'illustre l'exemple suivant :

::

    >>> print(1.0 - 0.000000000000000000000001)
    1.0 

Au contraire, lorsqu'on travaille avec des nombres entiers, les résultats ne
sont jamais arrondis. En particulier, les nombres peuvent devenir aussi grands
qu'on le souhaite !

::

    >>> print(12345678987654321 * 9876543210123456789)
    121932631979881115785550983112635269 

Dès qu'on utilise une division, on obtient forcément un nombre à virgule en
résultat et cela peut parfois être surprenant :

::

    >>> grosNombre = 1000 * 1000 * 1000 * 1000 * 1000 * 1000
    >>> nombre = grosNombre + 1
    >>> print(nombre)
    1000000000000000001 
    >>> nombre = (grosNombre + 1) / 1
    >>> print(nombre)
    1e+18 
    >>> nombre = (grosNombre + 1) / 1 - grosNombre
    >>> print(nombre)
    0.0 

..  note::

    Le "1e+18" ci-dessus est en fait égal au nombre constitué d'un "1" suivi de 18
    "0". Cette notation est expliquée plus en détail au cours suivant.

Mais que s'est-il passé ? Quand on a divisé par 1 on est passé d'un nombre
entier (avec un nombre de chiffres non-limité) à un nombre à virgule (qui ne
garde que 17 chiffres) et donc le chiffre des unités a été "oublié". Même
quand on soustrait le nombre ``grosNombre`` on ne peut récupérer ce chiffre des
unités et le résultat est donc égal à ``0.0`` !

Un exemple étonnant
-------------------

Considérons l'exemple suivant :

::

    >>> prixJeu = 29.99
    >>> prixConsole = 299
    >>> print(prixJeu + prixConsole - 49.90)
    279.09000000000003

Le résultat "mathématique" serait bien sûr :math:`279.09` alors pourquoi y
a-t-il ce :math:`3` tout à la fin ? La méthode utilisée par l'ordinateur pour
stocker en mémoire les nombres à virgules ne permet pas de stocker de manière
exacte tout nombre à virgule. Ainsi de très légères erreurs peuvent apparaître
pour les tout derniers chiffres.

Pas de tests d'égalité
----------------------

Considérons le programme suivant :

::

    if 0.1 + 0.2 == 0.3:
       print("Exact")
    else:
       print("Approché")
    print(0.1 + 0.2 - 0.3)

..  admonition:: Sortie

    ::

        Approché 
        5.551115123125783e-17 

Et oui, ``0.1 + 0.2`` n'est pas égal à ``0.3`` ! Ces trois valeurs ne peuvent en
fait pas être représentées de manière exacte par l'ordinateur et donc ``0.1 +
0.2`` n'est qu'une approximation du rationnel :math:`3 \over 10`, tandis que ``0.3`` en est
une autre approximation.

Deux approximations du même nombre ne sont pas forcément égales, elles sont
simplement très proches, à une distance à peu près égale à
:math:`0.0000000000000000555` !

Conclusion
----------

Vous aurez l'occasion d'en savoir plus sur ces histoires d'approximation dans
un prochain cours mais le sujet est assez technique, aussi ne vous en
préoccupez pas en détail pour le moment.

La seule chose à retenir c'est que les calculs avec des nombres décimaux ne
sont pas exacts mais approchés, à cause de ces petites erreurs. Aussi on
utilisera autant que possible des entiers plutôt que des nombres décimaux. En
particulier il ne faut jamais faire de tests d'égalité ou d'inégalité sur des
nombres décimaux. Quand aux inégalités entre nombres décimaux on évitera aussi
et on préférera calculer avec des entiers et ne passer vers des nombres
décimaux que le plus tard possible dans le programme.

La notation scientifique
========================

..  note::

    Cette partie est peut-être un peu technique car elle explique une notion
    mathématique. Il est important de bien la comprendre pour certains
    exercices que vous rencontrerez par la suite.


Quand un nombre à virgule a beaucoup de chiffres il est affiché avec la
notation scientifique :

::

    >>> print(12345678987654321 * 1234567.89)
    1.524157885840573e+22 

Si on ne retenait pas que les 17 premiers chiffres, le résultat serait égal à

..  math:: 1.524157885840573112635269 \times 10^{22}

On ne garde que les 17 premiers chiffres de la mantisse en faisant un arrondi
c'est-à-dire

..  math:: 1.524157885840573 \times 10^{22}

Autre exemple
-------------

::

    >>> print(1 / 12345678987654321)
    8.1000000162e-17

ce qui équivaut à 

..  math:: 8.1000000162 \times 10^{-17}