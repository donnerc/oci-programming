Utilisation basique de *git*
############################

..	note::

	Dans ce petit cours, je vous montre comment utiliser l'utilitaire ``git``
	pour travailler avec vos codes sources en local. Le but est de ne plus
	copier vos codes sources à la main dans votre dépôt *git* par
	l'intermédiaire de GitHub, mais de travailler directement en local sur
	votre machine.


Cloner un dépôt existant
========================

En général, les développeurs ne travaillent pas en collant leur code dans
l'éditeur de GitHub, mais utilise leur machine locale pour développer le code
pour le *pousser* ensuite sur Github.

Pour cloner un dépôt, il faut connaitre son url GitHub qui ressemble à quelque
chose comme

::

	https://github.com/donnerc/oci-prog-exos.git

On peut ensuite entrer la commande suivante dans un shell :

..	clode-block:: bash

	# cloner le dépôt
	git clone https://github.com/donnerc/oci-prog-exos.git

	# se déplacer dans le dossier contenant le dépôt
	cd oci-prog-exos



..	note::

	Synchroniser votre dépôt avec le dépôt *upstream* : https://help.github.com/articles/syncing-a-fork