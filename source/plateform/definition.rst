Définition du projet
####################

Besoins
=======

Il faut que je parvienne à pouvoir suivre les étudiants et leur progression
pour les programmes informatiques. Le problème de France-IOI, c'est que je ne
peux pas voir les codes sources et que le suivi s'arrête au niveau 1 ...

Fonctionnalités nécessaires
---------------------------

*	Identification des étudiants et navigation dans les tentatives des différents
	problèmes

*	pas seulement une seule sorte de grader. Il faudrait pouvoir tester les
	différentes fonctions définies dans un module (important pour le développement
	Web qui ne peut pas juste prendre l'entrée et la sortie d'un programme).

*	Programme d'évaluation qui tourne en local sur la machine des élèves ou sur
	leur VM koding (permet d'éviter tout le problème des performances et la
	nécessité d'installer un bac à sâble). Le programme d'évaluation envoie le
	code et un status code via une requête HTTP sur une application Web qui tourne
	sur http://www.donner-online.ch relié à une base de données *sqlite*.

