def best_score(a_dictionary):
    # Vérifier si le dictionnaire est vide
    if not a_dictionary:  # Si le dictionnaire est vide, retourner None
        return None

    # Trouver la clé ayant la plus grande valeur
    return max(a_dictionary, key=a_dictionary.get)  # Utilise la fonction
    # max pour obtenir la clé ayant la valeur maximale
