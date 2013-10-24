.. |koding| replace:: http://koding.com

..  _koding-tuto-01:

Prise en mains de la plateforme |koding|
########################################

Dans ce tutoriel, vous allez découvrir comment utiliser la plateforme de développement en ligne |koding|.

La plateforme |koding| met essentiellement à disposition via son site Web une
**machine virtuelle** Linux Ubuntu. Il s'agit d'un véritable ordinateur,
directement connecté à Internet et sur lequel il est possible de développer et d'héberger des applications Web.

Vous allez surtout l'utiliser dans un premier temps pour gérer votre dépôt git.

Création d'un compte
====================

Pour commencer, il faut créer un compte sur la plateforme |koding| si vous ne
l'avez pas fait. Il est conseillé d'utiliser un compte GitHub existant pour
créer le compte |koding|, ce qui permettra de lier votre compte koding et
votre compte GitHub.

..  admonition:: TODO

    Créer un compte |koding| en cliquant sur le bouton "Sign up with GitHub"
    si vous avez un compte GitHub ou "Sign up with email" dans le cas
    contraire.

Terminal et premières commandes shell
=====================================

..  only:: html

    Démonstration vidéo
    -------------------

    ..  tip::

        Une bonne partie du cours sera donné sous forme de vidéos YouTube.
        Pour en tirer le plein profit, il faut effectuer les opérations
        montrées et ne pas seulement faire le spectateur.

        Il est également nécessaire de prendre des notes des éléments les plus importants.

        *   Il est conseillé de visionner la vidéo en plein écran et en haute
            résolution sur YouTube pour voir tous les détails.

        *   N'hésitez pas à faire des commentaires ou poser des questions sur
            YouTube.

    ..  youtube:: GiZu1_4qB6A
        :width: 100%

Résumé
------

La vidéo explique les éléments suivants :

*   se logger sur |koding|

*   utilisation de l'onglet *Develop*

*   notion de machine virtuelle

*   utilisation du terminal pour effectuer les opérations suivantes :

    *   afficher le contenu d'un dossier

    *   connaitre le dossier de travail (dossier courant)

    *   naviguer dans le système de fichiers (arborescence de dossiers)

    *   création, suppression et renommage d'un dossier

Commandes shell expliquées dans cette vidéo
+++++++++++++++++++++++++++++++++++++++++++

..  admonition:: Commande ``ls``

    La commande ``ls`` permet de lister les fichiers et répertoires présents dans
    le répertoire courant.

    ::

        ls

        # l'option -a permet d'afficher les fichiers cachés dont le nom
        # commence par un .
        ls -a

        # l'option -l permet d'afficher le détail des fichiers et dossiers
        ls -a -l
        ls -al

..  admonition:: Commande ``pwd``

    La commande ``pwd`` permet de connaitre dans quel dossier on se trouve
    actuellement (dossier courant).

    La commande ``cd`` permet de naviguer dans l'arborescence de dossiers. 

    *   ``cd <dossier>`` : se rendre dans le dossier ``<dossier>`` présent dans     le dossier courant

    *   ``cd ..`` : se rendre dans le dossier parent

    ..  note::

        *   ``pwd`` = Process Working Directory

        *   ``cd`` = Change Directory

        *   Directory = Dossier

    Commandes montrées dans la vidéo :

    ::

        pwd
        cd Web
        pwd
        cd ..
        pwd

..  admonition:: Commandes ``mkdir`` et ``rmdir``

    La commande ``mkdir <dossier>`` permet de créer le dossier ``<dossier>``. Si le dossier existe déjà, la commande échoue.

    La commande ``rmdir <dossier>`` permet de supprimer le dossier
    ``<dossier>``. La commande échoue si le dossier ``<dossier>`` n'est pas vide

    ..  note::

        *   ``mkdir`` = Make Directory

        *   ``rmdir`` = Remove Directory

    ::

        mkdir GitHub
        rmdir GitHub
        mkdir GitHub
        cd GitHub





Installater *git* et clôner le dépôt ``oci-prog-exos``
======================================================




