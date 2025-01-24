def multiply_by_2(a_dictionary):
    # Utiliser une compréhension de dictionnaire pour multiplier chaque
    # valeur par 2
    return {
        key: value * 2  # Multiplier chaque valeur par 2
        for key, value in a_dictionary.items()  # Parcourir chaque paire
        # clé-valeur du dictionnaire
    }
