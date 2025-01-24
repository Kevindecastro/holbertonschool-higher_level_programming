# Python - More Data Structures: Set, Dictionary

Ce projet explore les structures de données avancées en Python, notamment les ensembles (sets) et les dictionnaires (dictionaries). Vous apprendrez à utiliser ces structures pour résoudre des problèmes complexes de manière efficace et pythonique.

## Introduction

Dans ce projet, nous nous concentrons sur les ensembles et les dictionnaires, deux des structures de données les plus utilisées en Python. Vous découvrirez leurs applications dans des scénarios variés, apprendrez à manipuler ces structures, et explorerez des concepts supplémentaires comme les fonctions lambda et les fonctions `map`, `filter`, et `reduce`. À travers des exercices pratiques, vous vous familiariserez avec les meilleures pratiques pour manipuler ces structures de manière optimale.

## Contenu

### Objectifs d'apprentissage

- Comprendre pourquoi Python est un langage de programmation puissant.
- Apprendre à utiliser les ensembles (élimination des doublons, opérations sur des ensembles).
- Comprendre les différences entre les ensembles, les listes et les dictionnaires, et savoir quand les utiliser.
- Explorer les fonctions lambda, ainsi que les fonctions `map`, `filter` et `reduce`.
- Apprendre les méthodes les plus courantes pour manipuler les ensembles et les dictionnaires.

### Prérequis

- Utilisation des éditeurs de texte : `vi`, `vim`, `emacs`.
- Tous les fichiers seront écrits pour Python 3.8.5 sur Ubuntu 20.04 LTS.
- Respect des normes de style Python (pycodestyle version 2.7).

## Installation

1. Clonez le dépôt GitHub sur votre machine locale :
   ```bash
   git clone https://github.com/Kevindecastro/holbertonschool-higher_level_programming.git
   ```

2. Accédez au répertoire contenant les fichiers Python du projet.

3. Assurez-vous que Python 3.8.5 est installé sur votre machine. Si ce n'est pas le cas, vous pouvez installer Python en suivant les instructions disponibles [ici](https://www.python.org/downloads/).

## Exécution

Les fichiers Python peuvent être exécutés directement à partir du terminal. Par exemple :

```bash
python3 0-square_matrix_simple.py
```

Vous pouvez remplacer le nom du fichier par celui de la tâche que vous souhaitez exécuter.

### Tâches

0. **Squared simple**

   - **Description** : Cette fonction prend une matrice (liste de listes) et renvoie une nouvelle matrice où chaque élément est élevé au carré.
   - **Prototype** : `def square_matrix_simple(matrix=[]):`
   - **Exemple d'utilisation** :
     ```python
     matrix = [
         [1, 2, 3],
         [4, 5, 6]
     ]
     print(square_matrix_simple(matrix))
     # Résultat : [[1, 4, 9], [16, 25, 36]]
     ```
   - [Code source](0-square_matrix_simple.py)

1. **Search and replace**

   - **Description** : Remplace toutes les occurrences d'une valeur dans une liste par une autre.
   - **Prototype** : `def search_replace(my_list, search, replace):`
   - **Exemple d'utilisation** :
     ```python
     my_list = [1, 2, 3, 2, 4]
     print(search_replace(my_list, 2, 10))
     # Résultat : [1, 10, 3, 10, 4]
     ```
   - [Code source](1-search_replace.py)

2. **Unique addition**

   - **Description** : Calcule la somme de tous les éléments uniques dans une liste.
   - **Prototype** : `def uniq_add(my_list=[]):`
   - **Exemple d'utilisation** :
     ```python
     my_list = [1, 2, 3, 1, 4]
     print(uniq_add(my_list))
     # Résultat : 10
     ```
   - [Code source](2-uniq_add.py)

3. **Present in both**

   - **Description** : Retourne un ensemble contenant les éléments communs à deux ensembles donnés.
   - **Prototype** : `def common_elements(set_1, set_2):`
   - **Exemple d'utilisation** :
     ```python
     set_1 = {1, 2, 3}
     set_2 = {2, 3, 4}
     print(common_elements(set_1, set_2))
     # Résultat : {2, 3}
     ```
   - [Code source](3-common_elements.py)

4. **Only differents**

   - **Description** : Retourne un ensemble des éléments présents dans un seul des ensembles donnés.
   - **Prototype** : `def only_diff_elements(set_1, set_2):`
   - **Exemple d'utilisation** :
     ```python
     set_1 = {1, 2, 3}
     set_2 = {2, 3, 4}
     print(only_diff_elements(set_1, set_2))
     # Résultat : {1, 4}
     ```
   - [Code source](4-only_diff_elements.py)

5. **Number of keys**

   - **Description** : Retourne le nombre de clés dans un dictionnaire.
   - **Prototype** : `def number_keys(a_dictionary):`
   - **Exemple d'utilisation** :
     ```python
     a_dictionary = {"a": 1, "b": 2, "c": 3}
     print(number_keys(a_dictionary))
     # Résultat : 3
     ```
   - [Code source](5-number_keys.py)

6. **Print sorted dictionary**

   - **Description** : Affiche les clés et leurs valeurs dans l'ordre alphabétique des clés.
   - **Prototype** : `def print_sorted_dictionary(a_dictionary):`
   - **Exemple d'utilisation** :
     ```python
     a_dictionary = {"b": 2, "a": 1, "c": 3}
     print_sorted_dictionary(a_dictionary)
     # Résultat :
     # a: 1
     # b: 2
     # c: 3
     ```
   - [Code source](6-print_sorted_dictionary.py)

7. **Update dictionary**

   - **Description** : Ajoute ou met à jour une clé dans un dictionnaire avec une valeur donnée.
   - **Prototype** : `def update_dictionary(a_dictionary, key, value):`
   - **Exemple d'utilisation** :
     ```python
     a_dictionary = {"a": 1, "b": 2}
     update_dictionary(a_dictionary, "c", 3)
     print(a_dictionary)
     # Résultat : {"a": 1, "b": 2, "c": 3}
     ```
   - [Code source](7-update_dictionary.py)

8. **Simple delete by key**

   - **Description** : Supprime une clé spécifique dans un dictionnaire.
   - **Prototype** : `def simple_delete(a_dictionary, key=""):`
   - **Exemple d'utilisation** :
     ```python
     a_dictionary = {"a": 1, "b": 2}
     simple_delete(a_dictionary, "a")
     print(a_dictionary)
     # Résultat : {"b": 2}
     ```
   - [Code source](8-simple_delete.py)

9. **Multiply by 2**

   - **Description** : Crée un nouveau dictionnaire avec les valeurs multipliées par 2.
   - **Prototype** : `def multiply_by_2(a_dictionary):`
   - **Exemple d'utilisation** :
     ```python
     a_dictionary = {"a": 1, "b": 2}
     print(multiply_by_2(a_dictionary))
     # Résultat : {"a": 2, "b": 4}
     ```
   - [Code source](9-multiply_by_2.py)

10. **Best score**

    - **Description** : Trouve la clé associée à la plus grande valeur dans un dictionnaire.
    - **Prototype** : `def best_score(a_dictionary):`
    - **Exemple d'utilisation** :
      ```python
      a_dictionary = {"Alice": 90, "Bob": 95, "Charlie": 85}
      print(best_score(a_dictionary))
      # Résultat : "Bob"
      ```
    - [Code source](10-best_score.py)

11. **Multiply by using map**

    - **Description** : Multiplie tous les éléments d'une liste par un nombre donné en utilisant `map`.
    - **Prototype** : `def multiply_list_map(my_list=[], number=0):`
    - **Exemple d'utilisation** :
      ```python
      my_list = [1, 2, 3]
      print(multiply_list_map(my_list, 2))
      # Résultat : [2, 4, 6]
      ```
    - [Code source](11-multiply_list_map.py)

12. **Roman to Integer**

    - **Description** : Convertit un chiffre romain donné sous forme de chaîne en entier.
    - **Prototype** : `def roman_to_int(roman_string):`
    - **Exemple d'utilisation** :
      ```python
      print(roman_to_int("XIV"))
      # Résultat : 14
      ```
    - [Code source](12-roman_to_int.py)

### Références utiles

- [Data structures](https://docs.python.org/3/tutorial/datastructures.html)
- [Lambda, filter, reduce and map](https://www.learnpython.org/en/Map,_Filter,_Reduce)
- [Learn to Program 12 Lambda Map Filter Reduce](https://www.youtube.com/watch?v=hYzwCsKGRrg)

---

**Dépôt GitHub :** [holbertonschool-higher\_level\_programming](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/tree/main/python-more_data_structures)

---

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.

