#!/usr/bin/python3
def text_indentation(text):
    """
    Indente un texte en fonction des caractères de ponctuation suivants : .,
    ?, et :. Si le texte n'est pas une chaîne de caractères, une exception
    TypeError est levée.
    """

    # Vérifie si l'argument 'text' est bien une chaîne de caractères
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    # Variable 'flag' utilisée pour savoir si un espace doit être ignoré avant
    # d'afficher un caractère
    flag = 1

    # Parcours chaque caractère dans le texte
    for letter in text:

        # Si 'flag' est à 1, cela signifie que l'on est soit dans un espace
        # soit après une ponctuation
        if flag == 1:
            if letter == ' ':
                continue  # Ignore les " " au début ou après une ponctuation
            else:
                # Si le caractère n'est pas un espace, commence à afficher
                flag = 0

        # Affiche le caractère sans ajouter de nouvelle ligne
        print(letter, end="")

        # Si le caractère est une ponctuation (., ?, ou :), ajoute une nouvelle
        # ligne après
        if letter in ".?:":
            print("\n")  # Nouvelle ligne après la ponctuation
            flag = 1  # Prépare à ignorer les espaces après une ponctuation
