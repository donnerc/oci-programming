Screencasts Cours OCI : Utilisation de Koding et GitHub
#####################

Cours 01 - Introduction à l'environnement Koding.com
====================================================

*	se logger

*	onglet "Develop"

*	terminal

*	entrer les commandes suivantes :

	::

		ls

		ls -a

		ls -a -l
		ls -al

	::

		pwd

		cd Web

		pwd

		cd ..

		pwd

	::

		mkdir GitHub
		rmdir GitHub
		mkdir GitHub

		cd GitHub

Cours 02 - Installation de git
===================

Résumés
-------

Pour installer l'utilitaire *git*, il faut exécuter la commande ``apt-get``
permettant de gérer les **paquets logiciels** installés sur la machine. Vous
allez voir qu'il est bien plus simple d'installer un logiciel sous Linux
Ubuntu que sous Windows (ou Mac OS X).

Essayons de saisir la commande suivante :

::

	apt-get install git

Le retour est immédiat :

::

	E: Could not open lock file /var/lib/dpkg/lock - open (13: Permission denied)
	E: Unable to lock the administration directory (/var/lib/dpkg/), are you root?

En gros, le système nous dit ``permission denied`` pour nous signifier que
nous n'avons pas le droit d'installer un logiciel sans être administrateur.

Dans les systèmes UNIX, on peut momentanément acquérir les droits
administrateurs (on dit "super-utilisateur" dans le jargon UNIX) en faisant
précéder la commande à exécuter par ``sudo`` :

::

	sudo apt-get install git

..	note::

	Le mot de passe à entrer est le mot de passe du site Koding.com. Lorsque
	vous le taperez au clavier, il ne s'affichera pas, c'est tout-à-fait
	normal.

Et là, toute la magie de ``apt-get`` opère pour nous installer *git* en un
clin d'oeil. Essayez d'installer *git* sous Windows pour apprécier la
différence ...

Cours 03 : Modifier et exécuter un fichier sous Koding.com
===========================================================

*	Naviguer jusque dans le dossier voulu

	..	code-block:: bash

		cd GitHub/oci-prog-exos/niveau

*	montrer comment éditer le fichier avec l'éditeur Ace dans Koding

*	sauver le fichier

*	Installer Python3

*	exécuter le fichier

Cours 04 : Mettre à jour le dépôt GitHub
========================================

Une fois que des modifications ont été apportées à un fichier python, nous
aimerions pouvoir mettre à jour le dépôt sur GitHub. Nous allons voir les
commandes *git* suivantes

*	``git add <nom_fichier>`` pour prendre en compte les modifications sur le fichier ``<nom_fichier>``
*	``git add .`` pour prendre en compte toutes les modifications dans le dossier courant et ses sous-dossiers
*	``git commit -m "<message>`` pour appliquer les modifications enregistrées
*	``git push`` pour *pousser* les modifications sur le dépôt git distant sur GitHub
