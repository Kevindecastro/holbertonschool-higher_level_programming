#!/usr/bin/env python3
"""Module définissant les classes Fish, Bird et FlyingFish pour 
illustrer l'héritage multiple en Python.
"""


class Fish:
    """Classe représentant un poisson."""

    def swim(self):
        """Affiche un message indiquant que le poisson nage."""
        print("The fish is swimming")

    def habitat(self):
        """Affiche l'habitat naturel du poisson."""
        print("The fish lives in water")


class Bird:
    """Classe représentant un oiseau."""

    def fly(self):
        """Affiche un message indiquant que l'oiseau vole."""
        print("The bird is flying")

    def habitat(self):
        """Affiche l'habitat naturel de l'oiseau."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Classe représentant un poisson volant, héritant de Fish et Bird."""

    def fly(self):
        """Affiche un message indiquant que le poisson volant s'élève."""
        print("The flying fish is soaring!")

    def swim(self):
        """Affiche un message indiquant que le poisson volant nage."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Affiche l'habitat du poisson volant."""
        print("The flying fish lives both in water and the sky!")
