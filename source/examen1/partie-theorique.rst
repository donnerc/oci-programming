Partie théorique
################

..  admonition:: Données personnelles

    *   Nom :
    *   Prénom :
    *   Date :
    *   Classe :

Question 0 (6 points)
==========


Parmi les séquences d'instructions suivantes, indiquer pour lesquelles la
valeur de la variable ``x`` est la même après l'exécution des instructions
qu'avant. On suppose que les variables ``x`` et ``a`` sont des entiers
quelconques avant l'exécution des instructions

::

    a = int(input())
    x = int(input())



..  admonition:: Entourer les programmes qui ne changent pas la valeur de la variable ``x``

    #)  

        ..  code-block:: python
            :linenos:

            a = x
            a = a + 1

    #)  

        ..  code-block:: python
            :linenos:

            a = x
            x = a

    #)  

        ..  code-block:: python
            :linenos:

            x = x + 1
            x = x

    #)  

        ..  code-block:: python
            :linenos:

            z = x
            a = z
            x = a

    #)  

        ..  code-block:: python
            :linenos:

            x *= 1
            a += 1

    #)  

        ..  code-block:: python
            :linenos:

            x *= 0
            a += 0

Question 1 (Analyse de programmes)
==========

#)  Que fait le programme suivant : 

    ..  code-block:: python 
        :linenos:

        i = 0
        while i != 10:
            i = i + 1
            print(i, end=" ")

    ..  admonition:: Cocher ce qui convient

        *   Produit une erreur
        *   Affiche ``0 1 2 3 4 5 6 7 8 9``
        *   Affiche ``1 2 3 4 5 6 7 8 9``
        *   Affiche ``1 2 3 4 5 6 7 8 9 10``
        *   Ne s'arrête jamais

#)  Que fait le programme suivant :

    ..  code-block:: python 
        :linenos:

        i = 1
        while i != 10:
              i = i + 2
              print i

    ..  admonition:: Cocher ce qui convient

        *   Produit une erreur
        *   Affiche ``2 4 6 8``
        *   Affiche ``1 3 5 7 9``
        *   Affiche ``3 5 7 9``
        *   Ne s'arrête jamais


#)  On donne le programme suivant dans lequel ``<test>`` est une expression
    booléenne quelconque et ``<instructions>`` une suite quelconque d'instructions Python.

    ..  code-block:: python 
        :linenos:

        while <test>:
            <instructions>

    Entourer les programmes ci-dessous qui sont équivalents au programme donné ci-dessus

    ..  code-block:: python 
        :linenos:

        while <test>:
            if False:
                break
            <instructions>

    ..  code-block:: python 
        :linenos:

        while <test>:
            <instructions>
            break

    ..  code-block:: python 
        :linenos:

        while True:
            if <test>:
                break
            <instructions>

    ..  code-block:: python 
        :linenos:

        while <test>:
            <instructions>
            if <test>:
                <instructions>
            else:
                break                    

Question 2 (5 points)
==========

Déterminer le type de données de chaque variable du programme à la fin de son
exécution :

..  code-block:: python 
    :linenos:

    a = 16 + 2
    b = 15.0
    c = float(a)
    d = c / 3
    e = input("Entrez un nombre entier")


Question 3 (5 points)
==========

#)  Noter à côté de chaque instruction ``print`` du programme ci-dessous ce
    qu'elle affiche sur la sortie standard

    ..  code-block:: python 
        :linenos:

        a = True
        b = False

        print( a and a, a and b, b and b )
        print( a or a, a or b, b or b )
        print( not b, not a )
        print( not a and b )
        print( not (a and b) and a or b )

Question 3b (3 points)
===========

Pour chaque programme ci-dessous, indiquer ce qu'il affiche sur la sortie
standard ou quelle type d'erreur il produit dans le cas où il contient une erreur

*   Programme 1

    ..  code-block:: python 
        :linenos:

        print "salut tout le monde"

*   Programme 2

    ..  code-block:: python 
        :linenos:

        print('Le soleil s'est levé ce matin')


*   Programme 3

    ..  code-block:: python 
        :linenos:

        valeur = float(input())
        print("Le carré du nombre entré est " + valeur ** 2)



Question 4 (3 points)
==========

Convertir le nombre binaire 110010100 en nombre décimal (calculatrice
autorisée) et indiquer les détails du calcul effectué.


Question 5 (3 points)
==========

Compléter / corriger le programme ci-dessous pour qu'il permette de convertir une chaine de caractère formée de 0 et de 1 en un nombre décimal et affiche la réponse sur la sortie standard.

**Indication** : Si nécessaire, vous pouvez biffer des lignes et les récrire à côté correctement

..  code-block:: python 
    :linenos:

    binaire = input()
 
    
     
    position = 0
    decimal = 0
    puissance = len(binaire) - 1


    while .............................................. :
        bit = binaire[position]

        poids = 2 ** puissance
     
        decimal = poids * bit
     
        
        
        position += 1
        puissance = puissance - 1 
     
    print(decimal)


