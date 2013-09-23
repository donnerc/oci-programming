#####################
Devoir 03 -- pour le mardi 24.09.2013
#####################

Programmation (France IOI)
==========================

*   Effectuer tous les problèmes du niveau 1, chapitre 5
    "Tests et conditions" et lire tous les éléments de théorie

Programme à réaliser (fait en cours)
====================

Développez un programme qui lit en entrée le nom et le prénom de l'utilisateur sur **l'entrée standard** et qui écrit sur la **sortie standard** le message

::

    Salut <prénom> <nom>, tu es âgé de ... ans

..  admonition:: Corrigé

    ..  code-block:: python
        :linenos:

        prenom = input("Entre ton prénom : ")
        nom = input("Entre ton nom de famille : ")
        anneeNaissance = int(input("Année de naissance : "))

        print("Salut " + prenom + " " + nom + "! Tu es âgé(e) de " + str(2013 - anneeNaissance) )

..  admonition:: Remarque

    On aurait pu remplacer la ligne 5 par 

    ::

        print("salut", prenom, nom, "Tu es âgé(e) de", 2013 - anneeNaissance)

Déroulement du programme
------------------------

..  admonition:: Entrée

    ::

        Entre ton prénom : Guido (entré au clavier)

        Entre ton nom de famille : Van Rossum (entré au clavier)

        Année de naissance : 1956

..  admonition:: Sortie du programme

    ::

        Salut Guido Van Rossum, tu es âgé de 57 ans

Contrainte
----------

Vous ne devez faire appel à la fonction  ``print()`` qu'une seule fois dans le programme.

..  tip:: Concaténation de chaines de caractères

    *  Pour n'utiliser qu'une seule instruction ``print``, il faudra utiliser l'opération de **concaténation**. Pour rappel, concaténer deux chaines de caractères consiste à les "coller ensemble". 

    *   Pour concaténer deux chaines de caractères, il suffit de les "additionner" avec l'opérateur ``+`` :

    ::

        >>> print('Guido' + ' ' + 'Van Rossum')
        Guido Van Rossum

        >>> prenom = 'Guido'
        >>> nom = 'Van Rossum'
        >>> print(prenom + ' ' + nom)
        Guido Van Rossum


Quiz théorie (tests et conditions)
==================================

..  only:: prof

    *   il faut rajouter un quiz qui permet de tester dans quelle mesure ils
        ont compris le sujet difficile des conditions

    *   ce n'est pas suffisant qu'ils fassent les exercices dans france ioi à
        mon sens

