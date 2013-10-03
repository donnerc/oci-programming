Introduction au débogage de programmes
######################################

L'activité de programmation consiste très souvent, après avoir implémenté un
algorithme qui fonctionne en théorie, à déterminer ce qui empêche le programme
de bien tourner.

On distingue plusieurs types d'erreurs qui peuvent survenir à différents
moments du développement d'un programme :

#)	Les erreurs de syntaxes (Syntax errors)
#)	Les erreurs d'exécution (Runtime errors)
#)	Erreurs de logique / erreurs sémantiques

Erreurs de syntaxes
===================

Les erreurs de syntaxes sont les erreurs les plus faciles à remarquer
puisqu'elles empêchent la compréhension du programme par l'interpréteur
Python. Lorsqu'une telle erreur survient, l'interpréteur refuse de lancer le
programme en renvoie un message d'erreur qui ressemble à ceci :

..	sidebar:: Erreur de syntaxe

	Une erreur de syntaxe survient lorsque l'interpréteur ne peut pas
	comprendre le programme parce que ce dernier ne suit pas les règles de
	grammaire du langage Python.

::
	
	>>> salut = 1
	>>> 2 = salut
	  File "<stdin>", line 1
	SyntaxError: can't assign to literal

Il y a différents types d'erreurs de syntaxes qui peuvent se produire, mais
Python saura dans tous les cas identifier la ligne exacte qui pose problème.

..	note::

	Il est capital de bien analyser le message d'erreur produit par
	l'interpréteur Python et de déterminer s'il s'agit d'une erreur de
	syntaxe, d'exécution ou de logique.

	Il faut également prendre le temps d'identifier où l'erreur s'est produite
	(numéro de la ligne) et quelle partie de la ligne pose problème.

Erreurs d'exécution
===================

Lorsque le programme ne comporte pas d'erreur de syntaxe, il va pouvoir être
exécuté par l'interpréteur instruction après instruction. Une **erreur
d'exécution** peut alors survenir si une des instructions exécutée demande de
réaliser une action qui pose problème. En jargon de la programmation, on dit
que "le code lève une exception".

Exemples d'exceptions courantes
-------------------------------

*	``IndexError`` : Survient lorsqu'on essaie d'accéder à un élément d'une
	liste ou autre structure de données qui n'existe pas.

*	``EOFError`` : Survient lorsque le programme essaie de lire des données
	alors qu'il a atteint la fin de la source de données (fichier, ligne). Dans 
	le contexte de la plateforme d'entrainement IOI, cela arrive souvent lorsque
	le programme cherche à lire une valeur sur l'entrée standard avec ``input()`` 
	alors que le serveur d'évaluation n'a pas fourni de données à lire.

*	``NameError``: Cette erreur survient lorsqu'on
	essaie d'accéder à une variable ou une fonction qui n'a pas encore été définie à
	ce stade dans le programme.

*	etc ...

Les erreurs d'exécution (exceptions) sont les erreurs les plus fréquemment
rencontrées en informatique et sont souvent difficiles à réparer. Elles
demandent une attention toute particulière au message d'erreur renvoyé par
Python et souvent une bonne dose de patience. Ces erreurs sont
particulièrement gênantes en informatique puisqu'elles surviennent souvent
lors de l'utilisation du programme et perturbent sont fonctionnement normal.

..	tip::

	Les bons réflexes à avoir en présence d'une telle erreur sont les suivants :

	*	Lire de manière attentive et plusieurs fois le message d'erreur
		renvoyé par Python. La description de l'erreur se trouvent tout
		à la fin du message d'erreur, dans les toutes dernières lignes.

	*	Copier la dernière ligne du message d'erreur et effectuer une recherche Google
		en copiant tel quel la partie pertinente du message.

	*	Consulter les forums spécialisés (souvent en anglais) où les
		développeurs échangent sur leurs développements et posent des questions
		à la communauté.


Exemple concret
---------------

On donne le programme suivant qui lève une exception :

..	code-block:: python
	:linenos:

	nbCible=int(input())
	nbEnfant=int(input())
	nbEssais=0
	trouve=False

	while not trouve:
	   
	   nbEssais=nbEssais+1
	   
	   if nbCible==nbEnfant:
	      trouve=True
	   if nbCible>nbEnfant:
	      print("c'est plus")
	   if nbCible<nbEnfant:
	      print("c'est moins")
	   nbEnfant=int(input())
	   
	print("Nombre d'essais nécessaires : ")
	print(nbEssais)


..	admonition:: Message d'erreur

	::

		Traceback (most recent call last):
		  File "./run/exe", line 2, in 
		    nbEnfant=int(input())
		EOFError: EOF when reading a line

Démarche
++++++++

#)	Bien lire le message d'erreur, surtout la dernière ligne, pour
	déterminer de quel type d'erreur il s'agit

	::
		
		EOFError: EOF when reading a line

#)	Chercher à quelle ligne et dans quel fichier l'erreur se produit. 
	Comme nos programmes n'utilisent pour le moment qu'un seul fichier Python,
	seul le numéro de ligne nous intéresse 

	::

		File "./run/exe", line 16, in 
		    nbEnfant=int(input())

	L'erreur se produit donc à la ligne 16 du programme.

#) 	On consulte la documentation officielle Python pour avoir une explication sur
	la signification de l'erreur. À cette fin, il est bon d'ajouter la page concernant
	les exceptions "buit-in" de Python dans les favoris

	..	note::

		**Page officielle sur les exceptions buit-in** :
		http://docs.python.org/3.3/library/exceptions.html

	Dans cette page, on utilise la fonctionnalité de recherche du navigateur
	Web, souvent avec le raccourci ``Ctrl + F`` sur un PC ou  ``⌘ + F`` sur un
	Mac, pour  trouver la bonne erreur. En l'occurrence, on cherchera
	"EOFError".

	On tombe alors sur l'explication suivante :

		**exception EOFError** : Raised when one of the built-in functions (input() or raw_input()) hits an end-of-file condition (EOF) without reading any data. (N.B.: the file.read() and file.readline() methods return an empty string when they hit EOF.)

#)	Il faut bien entendu traduire l'explication depuis l'anglais ... et la
	comprendre. Ici, le message dit essentiellement que cette erreur est produite
	par la fonction ``ìnput()`` de la ligne 16. Elle survient parce que la fonction
	``input()`` tente de lire une valeur sur l'entrée standard
	(standart input, souvent abbrégé **stdin**) alors que cette valeur n'existe pas.

	..	note::

		Dans le cadre de France IOI, cela arrive lorsque le programme tente de lire
		une valeur alors que toutes les valeurs fournies par le système d'évaluation
		ont déjà été lues.

Correction du bug
+++++++++++++++++

Dans notre exemple, il faut se demander pourquoi notre fonction ``input()``
lit une valeur alors qu'aucune valeur n'est fournie et comment on peut éviter 
ce problème.

**Cause du problème** : la ligne 16 ``nbEnfant=int(input())`` lit une valeur qui n'a
pas été fournie.

Pour résoudre ce problème, il faut imaginer dans quel(s) cas cela peut se
produire. Par exemple, que ce produit-il avec l'entrée suivante donnée dans
l'exemple du problème sur France IOI :

..	admonition:: Entrée

	::

		10
		5
		15
		8
		12
		11
		10

Un outil particulièrement utile pour analyser le programme étant donné un jeu
de données en entrée est d'utiliser cette version de PythonTutor : http://cscircles.cemc.uwaterloo.ca/visualize.

	* **Lien d'analyse de cet exemple** : http://cscircles.cemc.uwaterloo.ca/visualize#code=nbCible%3Dint(input())%0AnbEnfant%3Dint(input())%0AnbEssais%3D0%0Atrouve%3DFalse%0A%0Awhile+not+trouve%3A%0A%0A+++nbEssais%3DnbEssais%2B1%0A%0A+++if+nbCible%3D%3DnbEnfant%3A%0A++++++trouve%3DTrue%0A+++if+nbCible%3EnbEnfant%3A%0A++++++print(%22c'est+plus%22)%0A+++if+nbCible%3CnbEnfant%3A%0A++++++print(%22c'est+moins%22)%0A+++nbEnfant%3Dint(input())%0A%0Aprint(%22Nombre+d'essais+n%C3%A9cessaires+%3A+%22)%0Aprint(nbEssais)&mode=&raw_input=10%0A5%0A15%0A8%0A12%0A11%0A10

L'analyse de cet exemple permet de déterminer que la ligne 16 du code lit une
valeur alors qu'on a déjà lu toutes les valeurs de l'entrée standard. Il faut
donc réfléchir à une meilleure façon de code la boucle. Le problème vient du
fait qu'on lit le premier nombre de l'enfant avant de rentrer dans la boucle
et encore une deuxième fois à la fin de la boucle avant que la condition
``while not True`` ait eu le temps d'éviter de repasser dans la boucle.

**Correction** du bug : je vous laisse corriger ce code pour qu'il fonctionne.
