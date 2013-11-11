Fonctions
#########

Idées de questions à poser
==========================

#)  Définir la fonction ``abs(number) ==> number`` qui retourne la valeur absolue
#)  Définir la fonction ``square(number) ==> number`` qui retourne le carré
#)  Définir la fonction ``min(number, number) ==> number`` qui retourne le minimum de ``a`` et ``b``
#)  Définir la fonction ``min(number, number, number) ==> number`` qui retourne  le minimum de ``a`` et ``b`` et ``c``
#)  Définir la fonction ``max(nomber, nomber) ==> nombre`` en utilisant la fonction ``min`` de manière intelligente
#)  Définir la fonction ``mediane(a, b, c) ==> nombre`` qui retourne le nombre médian entre ``a``, ``b`` et ``c``

Quiz 1
------

On considère la fonction ``foo(a, b)`` définie par

::

    def foo(a, b):
        if test(a):
            return b
        return a

Parmi les fonctions ci-dessous, cocher celles qui sont équivalentes à ``foo``.
Deux fonctions sont équivalentes si pour n'importe quel couple de paramètres
``a`` et ``b``, elles retournent exactement la même valeur.

..  qcm:: Équivalence de fonctions

    * ::

        def foo1(x, y):
            if test(x):
                return y
            else:
                return x

    x ::

        def foo2(a, b):
            if not test(b):
                return a
            else:
                return b

    * ::

        def foo3(a, b):
            resultat = a
            if test(a):
                resultat = b
            return restultat

    * ::

        def foo3(a, b):
            if not test(a):
                b = 'Van Rossum'
            else:
                return b
            return a


Problème
--------

Définir une fonction ``find_last(search, target)`` qui retourne la position du
premier caractère de la dernière occurrence de la chaine ``target`` dans la
chaine ``search``.

..  admonition:: Indications

    *   Utiliser la méthode ``find(s,t)`` de la classe ``str``.

Problème
--------

Définir une fonction ``print_multiplication_table(n)`` qui prend en entrée un
nombre entier positif et qui imprime sur la sortie standard (avec ``print()``)
une table de multiplication complète selon l'exemple suivant :

::

    >>> print_multiplication_table(2)
    1 * 1 = 1
    1 * 2 = 2
    2 * 1 = 2
    2 * 2 = 4

    >>> print_multiplication_table(3)
    1 * 1 = 1
    1 * 2 = 2
    1 * 3 = 3
    2 * 1 = 2
    2 * 2 = 4
    2 * 3 = 6
    3 * 1 = 3
    3 * 2 = 6
    3 * 3 = 9

..  only:: correction

    ::

        def print_multiplication_table(n):

            i = 1
            while i <= n:
                k = 1
                while k <= n:
                    print i, '*', k, '=', i*k
                    k += 1
                    
                i += 1








