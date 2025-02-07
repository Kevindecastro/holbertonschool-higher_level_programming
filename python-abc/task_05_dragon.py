#!/usr/bin/env python3
"""Module définissant des mixins pour le vol et la nage, 
ainsi qu'une classe Dragon combinant ces capacités.
"""


class SwimMixin:
    """Mixin ajoutant la capacité de nager."""

    def swim(self):
        """Affiche un message indiquant que la créature nage."""
        print("The creature swims!")


class FlyMixin:
    """Mixin ajoutant la capacité de voler."""

    def fly(self):
        """Affiche un message indiquant que la créature vole."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Classe représentant un dragon pouvant nager et voler."""

    def roar(self):
        """Affiche un message indiquant que le dragon rugit."""
        print("The dragon roars!")
