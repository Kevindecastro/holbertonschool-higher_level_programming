def roman_to_int(roman_string):
    """Convertit une chaîne de chiffres romains en un entier."""
    # Vérifier si l'entrée est une chaîne de caractères non vide
    if not isinstance(roman_string, str) or roman_string is None:
        return 0  # Si ce n'est pas une chaîne, retourner 0

    # Dictionnaire des valeurs des chiffres romains
    roman_dict = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0  # Variable pour accumuler la somme totale
    prev_value = 0  # Variable qui garde la valeur du chiffre romain précédent

    # Parcourir les caractères de la chaîne en sens inverse
    for char in reversed(roman_string):
        # Obtenir la valeur actuelle (0 si le caractère est invalide)
        current_value = roman_dict.get(char, 0)

        # Si la valeur actuelle est plus petite que la précédente,
        # on la soustrait
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value  # Sinon, on l'ajoute à la somme totale

        prev_value = current_value  # Mettre à jour la valeur précédente

    return total  # Retourner le total de la conversion
