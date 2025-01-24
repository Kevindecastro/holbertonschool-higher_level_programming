# Python - Exceptions

Ce projet vise à introduire et à manipuler les exceptions en Python, en utilisant des techniques telles que le `try`, `except`, `finally`, et en abordant des cas spécifiques comme les erreurs de type, les divisions par zéro, etc.

## Introduction

Dans ce projet, nous abordons la gestion des erreurs en Python à travers les exceptions. Vous apprendrez à utiliser les structures `try`, `except`, `else` et `finally`, et à lever des exceptions personnalisées. L'objectif est de rendre votre code plus robuste en anticipant et en gérant correctement les erreurs qui peuvent survenir lors de l'exécution.

## Contenu

### Objectifs d'apprentissage

- Comprendre la différence entre les erreurs et les exceptions.
- Apprendre à utiliser les exceptions pour rendre le code plus robuste.
- Utiliser les structures `try`, `except`, `else` et `finally` de manière efficace.
- Lever des exceptions personnalisées pour des cas spécifiques.

### Prérequis

- Utilisation des éditeurs de texte : `vi`, `vim`, `emacs`.
- Tous les fichiers seront écrits pour Python 3.x.
- Respect des normes de style Python (pycodestyle version 2.7).

## Installation

1. Clonez le dépôt GitHub sur votre machine locale :
   ```bash
   git clone https://github.com/Kevindecastro/holbertonschool-higher_level_programming.git
   ```

2. Accédez au répertoire contenant les fichiers Python du projet.

3. Assurez-vous que Python 3.x est installé sur votre machine. Si ce n'est pas le cas, vous pouvez installer Python en suivant les instructions disponibles [ici](https://www.python.org/downloads/).

## Exécution

Les fichiers Python peuvent être exécutés directement à partir du terminal. Par exemple :

```bash
python3 0-safe_print_list.py
```

Vous pouvez remplacer le nom du fichier par celui de la tâche que vous souhaitez exécuter.

### Tâches

#### 0. Safe list printing

- **Description** : Cette fonction imprime les `x` premiers éléments d'une liste. Elle gère les erreurs liées aux indices et imprime les éléments de manière sécurisée.
- **Prototype** : `def safe_print_list(my_list=[], x=0):`
- **Exemple d'utilisation** :
  ```python
  my_list = [1, 2, 3, 4, 5]
  nb_print = safe_print_list(my_list, 2)
  print("nb_print: {:d}".format(nb_print))
  # Résultat :
  # 12
  # nb_print: 2
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/0-safe_print_list.py)

#### 1. Safe printing of an integers list

- **Description** : Cette fonction imprime les éléments d'une liste, mais seulement ceux qui sont des entiers. Si l'élément n'est pas un entier, il est ignoré.
- **Prototype** : `def safe_print_integer(value):`
- **Exemple d'utilisation** :
  ```python
  value = 89
  has_been_print = safe_print_integer(value)
  if not has_been_print:
      print("{} is not an integer".format(value))
  # Résultat :
  # 89
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/1-safe_print_integer.py)

#### 2. Print and count integers

- **Description** : Cette fonction imprime les premiers `x` éléments d'une liste, mais uniquement les entiers. Les autres types sont ignorés.
- **Prototype** : `def safe_print_list_integers(my_list=[], x=0):`
- **Exemple d'utilisation** :
  ```python
  my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
  nb_print = safe_print_list_integers(my_list, len(my_list))
  print("nb_print: {:d}".format(nb_print))
  # Résultat :
  # 12345
  # nb_print: 5
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/2-safe_print_list_integers.py)

#### 3. Integers division with debug

- **Description** : Cette fonction effectue une division entre deux entiers et affiche le résultat dans le bloc `finally`, après avoir géré les exceptions.
- **Prototype** : `def safe_print_division(a, b):`
- **Exemple d'utilisation** :
  ```python
  a = 12
  b = 2
  result = safe_print_division(a, b)
  print("{:d} / {:d} = {}".format(a, b, result))
  # Résultat :
  # Inside result: 6.0
  # 12 / 2 = 6.0
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/3-safe_print_division.py)

#### 4. Divide a list

- **Description** : Cette fonction divise élément par élément deux listes, en gérant les erreurs liées aux types, à la division par zéro, et aux indices hors limites.
- **Prototype** : `def list_division(my_list_1, my_list_2, list_length):`
- **Exemple d'utilisation** :
  ```python
  my_l_1 = [10, 8, 4]
  my_l_2 = [2, 4, 4]
  result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
  print(result)
  # Résultat : [5.0, 2.0, 1.0]
  ```
  ```python
  my_l_1 = [10, 8, 4, 4]
  my_l_2 = [2, 0, "H", 2, 7]
  result = list_division(my_l_1, my_l_2, max(len(my_l_1), len(my_l_2)))
  print(result)
  # Résultat :
  # division by 0
  # wrong type
  # out of range
  # [5.0, 0, 0, 2.0, 0]
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/4-list_division.py)

#### 5. Raise exception

- **Description** : Cette fonction soulève une exception de type `TypeError`.
- **Prototype** : `def raise_exception():`
- **Exemple d'utilisation** :
  ```python
  try:
      raise_exception()
  except TypeError as te:
      print("Exception raised")
  # Résultat :
  # Exception raised
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/5-raise_exception.py)

#### 6. Raise a message

- **Description** : Cette fonction soulève une exception `NameError` avec un message spécifié.
- **Prototype** : `def raise_exception_msg(message=""):`
- **Exemple d'utilisation** :
  ```python
  try:
      raise_exception_msg("C is fun")
  except NameError as ne:
      print(ne)
  # Résultat :
  # C is fun
  ```
- [Code source](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/blob/main/python-exceptions/6-raise_exception_msg.py)

---

## Références utiles

- [Les structures de données en Python](https://docs.python.org/3/tutorial/datastructures.html)
- [Les fonctions lambda, filter, reduce et map](https://www.learnpython.org/en/Map,_Filter,_Reduce)

---

**Dépôt GitHub :** [holbertonschool-higher_level_programming](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/tree/main/python-exceptions)

---

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.
```