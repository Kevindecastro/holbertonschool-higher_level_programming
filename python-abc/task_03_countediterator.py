#!/usr/bin/env python3
"""Module définissant une classe CountedIterator qui suit le nombre 
d'éléments itérés dans un itérable donné.
"""


class CountedIterator:
    """Classe qui étend un itérateur et compte les éléments parcourus."""

    def __init__(self, iterable):
        """Initialise un itérateur basé sur l'itérable donné et 
        un compteur à zéro.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """Retourne l'élément suivant et incrémente le compteur.
        Soulève StopIteration lorsqu'il n'y a plus d'éléments.
        """
        item = next(self.iterator)  # Peut lever StopIteration
        self.count += 1
        return item

    def get_count(self):
        """Retourne le nombre d'éléments déjà itérés."""
        return self.count
