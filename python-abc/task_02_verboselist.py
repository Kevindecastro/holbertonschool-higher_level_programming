#!/usr/bin/env python3

class VerboseList(list):
    """
    Classe héritant de la classe list avec des notifications
    lors de l'ajout ou du retrait d'éléments.
    """
    
    def append(self, item):
        """
        Ajoute un élément à la liste et affiche une notification.
        
        Args:
            item: L'élément à ajouter à la liste.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """
        Étend la liste avec plusieurs éléments et affiche une notification.
        
        Args:
            items: Liste des éléments à ajouter à la liste.
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """
        Retire un élément de la liste et affiche une notification.
        
        Args:
            item: L'élément à retirer de la liste.
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        Retire et renvoie un élément à l'index donné (ou dernier par défaut)
        de la liste et affiche une notification.
        
        Args:
            index (int): L'index de l'élément à retirer. Par défaut, -1 (dernier).
        
        Returns:
            L'élément retiré de la liste.
        """
        item = super().pop(index)
        print(f"Popped [{item}] from the list.")
        return item
