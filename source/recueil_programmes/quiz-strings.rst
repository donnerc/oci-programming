Chaines de caractères
#####################

..  admonition:: Source et référence

    La théorie de ce présent chapitre est une reprise et une traduction du
    cours "Building a search engine" donné sur https://www.udacity.com/wiki/cs101/unit_1

Théorie
=======


Indexation de chaines de caractères vides
-----------------------------------------

Lorsqu'on indexe une chaine de caractèes vide (i.e. string = ""), les
règles suivantes s'appliquent dans lesquelles ``#`` représente un nombre
quelconque :

*   ``print string [#]`` --> produit une erreur
*   ``print string [:]`` --> ne produit pas d'erreur
*   ``print string [#:#]`` --> ne produit pas d'erreur
*   ``print string [-#:-#]`` --> ne produit pas d'erreur
*   ``print string [#:-#]`` --> ne produit pas d'erreur
*   ``print string [0:0]`` --> ne produit pas d'erreur

Chercher des chaines dans des chaines
-------------------------------------

..  markdown::
    :lang: en

    The find method is a built in operation, or method, provided by Python, that operates on strings. The output of find is the position of the string where the specified sub-string is found.

    - *<search string>.**find**(<target string>)*

    If the target string is not found anywhere in the search string, then the output will be -1.

    Here are some examples (try them yourself in the interpreter):

    ::

        pythagoras = 'There is geometry in the humming of the strings, there is music in the spacing of the spheres. '

        print(pythagoras.find('string'))
        40
        print(pythagoras[40:])
        'strings, there is music in the spacing of the spheres.'
        print(pythagoras.find('T'))
        0
        print(pythagoras.find('sphere'))
        86
        print(pythagoras[86:])
        spheres.
        print(pythagoras.find('algebra'))
        -1    

Chercher avec des nombres
-------------------------

..  markdown::
    :lang: en

    En plus de passer une chaine "a_trouver" à trouver, il est également
    possible de passer un nombre ``<start_indice>`` comme second argument :

    ::

        <chaine_ou_on_cherche>.find(<a_trouver>, <start_indice>)

    L'entier ``<start_indice>`` représente la position dans
    ``chaine_ou_on_cherche`` à partir de laquelle ``find`` va chercher la
    chaine ``a_trouver``. De ce fait, la valeur de retour de ``find`` est un
    entier indiquant la position dans ``chaine_ou_on_cherche`` de la première
    occurrence de ``a_trouver`` à commencer à partir de l'indice
    ``start_indice``. S'il n'y a pas d'occurrence trouvée à partir de la
    position ``start_indice``, la fonction retourne ``-1``.

    Par exemple :

    ::

        >>> danton = "De l'audace, encore de l'audace, toujours de l'audace."
        >>> print(danton.find('audace'))
        5
        >>> print(danton.find('audace', 0))
        5
        >>> print(danton.find('audace', 5))
        5
        >>> print(danton.find('audace', 6))
        25
        >>> print(danton.find('audace', 25))
        25
        >>> print(danton.find('audace', 48))
        -1

..  quiz:: Début de la recherche

    Pour n'importe quelle chaines de caractères **s** et **t**, et pour un nombre **i** :

    ::

        s = '<any string>'
        t = '<any string>'
        i = <any number>

    Parmi les expressions suivantes, indiquer lesquelles sont évaluées à
    ``True`` :

    ..  qcm::

        -   ``s[i: ].find(t) == s.find(t,i)``
        -   ``s.find(t)[ :i] == s.find(t,i)``
        -   ``s[i: ].find(t) + i == s.find(t,i)``
        -   ``s[i: ].find(t[i: ]) == s.find(t,i)``
        -   aucune de ces expressions



Quiz
====

..  quiz:: Validité de chaines
    
    Cocher les définitions de chaines valides parmi les suivantes

    ..  qcm::
        
        *   ``"Ada"``
        x   ``'Ada"``
        x   ``"Ada``
        x   ``Ada``
        *   ``' "Ada'``

..  quiz:: Indexation de chaines
    :url: https://www.udacity.com/course/viewer#!/c-cs101/l-48299949/e-48755011/m-48695555

    Soit ``s`` une chaine de caractères quelconque définie par 

    ::

        s = input()

    Cocher toutes les affirmations qui sont  correctes à coup sûr :

    ..  qcm::
        
        -   ``s[3] == s[1 + 1 + 1]``
        -   ``s[0] == (s + s)[0]``
        -   ``s[0] + s[1] == s[0+1]``
        -   ``s[1] == (s + blabla)[1]``
        -   ``s[-1] == (s + s)[-1]``

..  quiz:: Slices (tranches) de chaines
    :url: https://www.udacity.com/course/viewer#!/c-cs101/l-48299949/e-48480572/m-48670980

    Soit ``s`` une chaine de caractères quelconque définie par 

    ::

        s = input()

    Cocher toutes les affirmations qui sont  correctes à coup sûr :

    ..  qcm::
        
        *   ``s[:] == s``
        *   ``s + s[0:-1+1] == s``
        *   ``s[0:] == s``
        x   ``s[:-1] == s``
        *   ``s[:3] + s[3:] == s``


..  quiz:: ``str.find()``
    :url: https://www.udacity.com/course/viewer#!/c-cs101/l-48299949/e-48704312/m-48700407

    Cocher les expressions qui sont évaluées à ``-1`` :

    ..  qcm::
        
        *   ``'test'.find('t')``
        x   ``"Test".find('te')``
        *   ``"test".find('st')``
        x   ``"Ouest".find('Est')``


..  quiz:: Indexation de chaines
    :url: https://www.udacity.com/course/viewer#!/c-cs101/l-48299949/e-48724449/m-48709193

    Soit ``s`` une chaine de caractères quelconque définie par 

    ::

        s = input()

    Cocher toutes les affirmations qui sont correctes quelle que soit la valeur de ``s`` :

    ..  qcm::
        
        *   ``s.find(s) == 0``
        x   ``s.find('s') == 0``
        *   ``'s'.find('s') == 0``
        *   ``s.find('') == 0``
        *   ``s.find(s + '!!!') + 1 == 0``


Questions de récapitulation
===========================

#)  Étant donnée une chaine de caractères ``s`` quelconque, cocher les
    qui sont évaluées à ``True``.

    ..  attention::

        Il se peut que ``s`` soit la chaine vide ``''``, i.e. ``s = ''`` :

    ..  qcm::

        *   ``('a' + s)[1:]``
        x   ``s[0] + s[1:]``
        *   ``s + ''``
        *   ``s[0:]``

#)  Question très intéressante sur les slices 

    #)  https://www.udacity.com/course/viewer#!/c-cs101/l-48587892/m-48719245
    #)  