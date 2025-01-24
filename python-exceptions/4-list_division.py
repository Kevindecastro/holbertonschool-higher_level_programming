#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """
    Divise les éléments de deux listes de manière sécurisée.

    Args:
        my_list_1 (list): Première liste de nombres.
        my_list_2 (list): Deuxième liste de nombres.
        list_length (int): Nombre d'éléments à traiter.

    Returns:
        list: Liste des résultats des divisions ou des erreurs (0).
    """
    result = []
    for i in range(list_length):
        try:
            if i >= len(my_list_1) or i >= len(my_list_2):
                raise IndexError  # Indique que l'index est hors de portée
            if (not isinstance(my_list_1[i], (int, float)) or
                    not isinstance(my_list_2[i], (int, float))):
                raise TypeError  # Type incorrect
            result.append(my_list_1[i] / my_list_2[i])  # Division des éléments
        except IndexError:
            print("out of range")  # Erreur d'index hors de portée
            result.append(0)
        except TypeError:
            print("wrong type")  # Type d'élément incorrect
            result.append(0)
        except ZeroDivisionError:
            print("division by 0")  # Division par zéro
            result.append(0)
        finally:
            continue
    return result
