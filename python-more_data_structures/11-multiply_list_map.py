#!/usr/bin/python3
# Utiliser map pour appliquer une fonction lambda qui multiplie chaque
# élément de la liste par 'number'
def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number, my_list))
# map applique la fonction à chaque élément de la liste,
# et list convertit le résultat en liste
