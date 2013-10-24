
Devoir 07 -- pour le mardi 05.11.2013
#####################


Plateforme http://koding.com et commandes UNIX
============================

Dans cette partie, vous allez découvrir la plateforme de développement en
ligne *Koding* et l'utiliser pour mettre à jour votre dépôt GitHub avec le
code de base des problèmes du niveau 02 de France IOI.

Dans la foulée, vous allez avoir une première expérience de "Hacker" en
travaillant non plus avec une souris, mais uniquemnet au clavier en ligne de
commandes.

Taĉhes à effectuer (dans l'ordre)
------------------

#)	Suivre la vidéo :ref:`koding-tuto-01` et retenir les notions essentielles (prendre des notes dans votre cahier). Effectuer les opérations montrées dans la vidéo sur la plateforme http://koding.com

#)	Idem pour la section :ref:`koding-tuto-02`

#)	Suivre la vidéo :ref:`koding-tuto-03` pour voir comment éditer votre
	code Python directement sur la plateforme koding.

	..	note::

		Après cette partie, vous devriez avoir installé Python 3
		sur votre machine virtuelle Koding à l'aide de la commande

		::

			sudo apt-get install python3

#)	Mettre à jour votre dépôt GitHub en effectuant les opérations suivantes. Je vous conseille de copier-coller la troisième ligne qui doit être exactement recopiée et exécutée dans le Terminal et ce qui vous évitera de chercher comment faire le caractère spécial ``|`` nécessaires à la troisième ligne : 

	.. code-block:: bash
		:linenos:

		cd
		cd GitHub/oci-prog-exos
		curl https://raw.github.com/donnerc/oci-prog-exos/master/niveau-02/create.sh | sh

#)	À ce stade votre dossier ``oci-prog-exos`` devrait contenir les éléments suivants si vous y exécutez la commande ``ls -al``, en particulier le dossier  ``ǹiveau-02`` dans lequel vous trouverez les données des exercices pour le niveau 2 de France IOI :

	::

		total 32
		drwxrwxr-x  6 donnerc donnerc 4096 oct 24 00:22 .
		drwxrwxr-x  5 donnerc donnerc 4096 oct 23 23:43 ..
		drwxrwxr-x  8 donnerc donnerc 4096 oct 24 00:24 .git
		-rw-rw-r--  1 donnerc donnerc  303 oct 23 23:43 .gitignore
		drwxrwxr-x 10 donnerc donnerc 4096 oct 23 23:43 niveau-01
		drwxrwxr-x  6 donnerc donnerc 4096 oct 24 00:24 niveau-02
		-rw-rw-r--  1 donnerc donnerc   28 oct 23 23:43 README.md
		drwxrwxr-x  2 donnerc donnerc 4096 oct 23 23:43 tmp


#)	Suivre la vidéo :ref:`koding-tuto-04` et mettre votre dépôt GitHub à jour
	à l'aide des commandes suivantes :

	..	code-block:: bash
		:linenos:

		# se rendre dans le dossier personnel
		cd 
		# se rendre dans le dossier du dépôt git
		cd GitHub/oci-prog-exos

		# ajouter les changements effectués sur les fichiers Python dans la
		# zone de transit (staging area)
		git add .

		# appliquer les changements dans l'historique des révisions
		git commit -m "devoirs 07"

		# pousser les changements sur GitHub
		git push

..
	Programmation (France IOI)
	==========================

	*	Terminer le chapitre 01 du niveau 02 de France IOI
