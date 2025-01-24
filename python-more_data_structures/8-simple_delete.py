#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Vérifier si la clé existe dans le dictionnaire
    if key in a_dictionary:  # Si la clé est présente dans le dictionnaire
        del a_dictionary[key]  # Supprimer l'élément correspondant à la clé

    # Retourner le dictionnaire après la suppression (ou sans modification
    # si la clé n'existe pas)
    return a_dictionary  # Retourne le dictionnaire, modifié ou non
