Affectation multiple et échange de variables
############################################

Affectation multiple
--------------------

..	note::

    Python dispose d'un raccourci syntaxique permettant d'affecter plusieurs
	variables en une seule opération d'affectation. Soient les trois affectations
	successives suivantes :

::

	>>> a=42
	>>> b=10
	>>> c=55
	>>> print(a+b+c)                            
	107                                     

Python offre un raccourci permettant d'effectuer les trois affectations en une
seule ligne :

::

	>>> a, b, c = 42, 10, 55                    
	>>> print (a+b+c)
	107 

*	**Ligne 1** : Cette affectation est dite multiple : ici, elle permet d'affecter
trois variables en une seule opération d'affectation. La syntaxe est assez
intuitive. Dans une affectation multiple, les variables à affecter sont
placées à gauche du signe = et sont séparées par des virgules. Dans le membre
de droite, les valeurs et/ou les variables qui seront affectées doivent être
en nombre égal et sont aussi séparées par des virgules.

L'affectation pourra, en première approximation, être considérée comme du
sucre syntaxique. La justification de cette syntaxe provient de la structure
de données dite de tuple, propre à Python.

Réaffectation
-------------

L'affectation multiple permet de faire facilement des réaffectations de
variables:

::

	>>> a, b, c = 42, 10, 81
	>>> a, b, c = a + b, a - b, a               
	>>> print(a, b, c)
	52 32 42                                

*	**Ligne 2** : les trois affectations sont effectuées en deux temps :

avec les valeurs initiales (ligne 1) de ``a``, ``b`` et ``c``, Python calcule
``a + b``, ``a - b`` et ``a``, ce qui donne les valeurs 52, 32 et 42 ensuite,
les affectations sont faites : ``a`` devient 52, etc. Autrement dit, ce sont les «
anciennes » valeurs des variables qui sont utilisées pour calculer les valeurs
affectées.

Le code équivalent, sans la syntaxe d'affectation multiple, serait le suivant :

..	code-block:: Python
	:linenos:

	>>> a = 42
	>>> b = 10
	>>> c = 81
	>>> x = a + b
	>>> y = a - b
	>>> z = a
	>>> a = x
	>>> b = y
	>>> c = z
	>>> print(a, b, c)                          
	52 32 42                                

Échange de variables
====================


..	note::

	**Résumé** : 

		*	Le procédé idiomatique en Python d'échange de contenus de deux variables.
		*	La méthode alternative classique.
		*	Le procédé propre à Python

La syntaxe d'affectation multiple permet très simplement d'échanger des
variables :

..	code-block:: Python
	:linenos:

	>>> a = 81
	>>> b = 31
	>>> print(a - b)                            

	>>> a, b = b, a
	>>> print(a - b)
	50
	-50                                     

*	**Ligne 5** : cette affectation multiple effectue l'échange des contenus des variables ``a`` et ``b``
*	**Lignes 7-8** : on voit que les contenus des variables ont bien été échangés.

La méthode idiomatique d'échange de variables en Python doit utiliser la
méthode ci-dessus.

La méthode classique	
--------------------

Si on n'utilise pas la syntaxe d'affectation multiple, le procédé usuel
d'échange de variables consiste à utiliser une variable temporaire :

..	code-block:: Python
	:linenos:

	>>> a = 81
	>>> b = 31
	>>> print(a, b)
	81 31

	>>> var_temp = a
	>>> a = b
	>>> b = var_temp
	>>> print(a - b)
	31 81

*	**Ligne 5** : var_temp est la variable temporaire. L'affectation var_temp = a copie en mémoire la valeur placée en a et cette copie est étiquetée par var_temp = a.
*	**Ligne 6** : Une copie de 31 est placée en mémoire et est étiquetée par a. Si on n'avait pas sauvegardé avec var_temp l'ancien contenu de a, celui-ci aurait été perdu.
*	**Ligne 7** : On place dans b le contenu initial de a, ce qui termine l'échange des contenus.