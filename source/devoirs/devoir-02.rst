#####################
Devoir 02 -- pour le mardi 17.09.2013
#####################

Révisions (boucles)
====================

Déterminer ce que chacun des programmes suivants affiche sur la **sortie standard** :

* Programme 1 (déjà fait en cours)::
    
    for loop in range(15):
        print("salut")
        print("tout le monde")

* Programme 2 (déjà fait en cours) ::

    for loop in range(15):
        print("salut")
    print("tout le monde")

* Programme 3 (pas fait en cours) ::

    for loop in range(15):
        print("salut", end = ' ')
    print("tout le monde")




Programmation (France IOI)
==========================

*   Effectuer tous les problèmes du niveau 1, chapitre 3
    "Calculs et découverte des variables"

*   Effectuer tous les problèmes du niveau 1, chapitre 4
    "Lecture de l'entrée"


Installation de Python
======================

Pour réaliser plus efficacemet vos programmes, vous allez installer Python sur votre machine afin de pouvoir programmer en local sans connexion au site de France IOI.

Instructions d'installation
---------------------------

Toutes les instructions sont indiquées (en anglais) sur le site de Python (http://www.python.org) sur lequel il est possible de télécharger l'interpréteur Python pour Windows ou Mac OS.

..  admonition:: Attention

    Il faut prendre garde aux éléments suivants :

    *   Si votre machine est récente et si vous avez Windows 7 ou 8 en 64 bits, il faudra télécharger la version 64 bits de Python, tandis qu'il faut télécharger la version 32 bits si votre machine tourne encore sous Windows XP ou une version 32 bits de Windows 7.

..  tip::

    Tous les programmes nécessitant une ligne telle que ::

        from robot import *

    ne peuvent pas être exécutés dans IDLE car ils utilisent le module ``robot`` qui n'est pas disponible en local, mais uniquement sur le serveur d'évaluation de France IOI.


Outil Python Tutor
==================

Python Tutor (http://www.pythontutor.com/) permet de visualiser l'exécution d'un programme Python. Maintenant que vous allez commencer à utiliser les variables, cet outil pourra vous être très utile pour repérer les erreurs fréquentes liées à l'utilisation des variables.

Pour analyer un programme, il suffit de le taper (ou d'en coller le code) dans http://www.pythontutor.com/visualize.html en remplaçant le code qui y figure par votre propre code.

Exercice
--------

#)  Expliquer le fonctionnement du programme suivant en l'analysant avec Python Tutor. 

    ::

        maximum = 1
        val = 0
        for loop in range(5):
            i = 1
            for loop in range(maximum):
                val = val + i
                i = i + 1

            maximum = maximum + 1
        print(val)

#)  Sans exécuter le programme dans IDLE, 
    déterminer la sortie du programme
    si on remplaçait la ligne ::

        for loop in range(5):

    par ::

        for loop in range(6):



