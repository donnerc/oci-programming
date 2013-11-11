Variables et types de données
#############################

..	quiz::

	Parmi les séquences d'instructions suivantes, indiquer pour lesquelles la
	valeur de la variable ``x`` est la même après l'exécution des instructions
	qu'avant. On suppose que les variables ``x`` et ``a`` sont des entiers
	quelconques avant l'exécution des instructions ::

	::

		a = int(input())
		b = int(input())

	..	qcm::

		::

			a = x
			a = a + 1

		::

			a = x
			x = a

		::

			x = x + 1
			x = x

		::

			a,x = x,a
			a,x = x,a

		::

			z = x
			a = z
			x = a

