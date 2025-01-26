# Python - Développement dirigé par les tests (TDD)

## Description

Ce projet est axé sur le **Développement Dirigé par les Tests (TDD)** en Python. Vous allez implémenter diverses fonctions et rédiger des tests pour celles-ci avant même de coder la logique, afin de garantir que le code répond au comportement attendu et couvre tous les cas limites.

## Exigences

- Python 3.8.5 (ou version supérieure)
- Tous les fichiers doivent se terminer par une nouvelle ligne.
- Le code doit être exécuté sur Ubuntu 20.04 LTS avec Python 3.
- Votre code doit respecter la norme `pycodestyle` (version 2.7.*).
- Les fichiers de tests doivent être dans le dossier `tests` et avoir l'extension `.txt`.
- Le code doit inclure une documentation appropriée avec des docstrings pour chaque fonction et module.
- Les tests doivent être exécutés avec la commande : `python3 -m doctest ./tests/*`.

## Tâches

### 0. Addition de deux entiers

Écrire une fonction qui additionne deux entiers.

Prototype : `def add_integer(a, b=98):`

- `a` et `b` doivent être des entiers ou des flottants.
- S'ils sont des flottants, ils doivent être convertis en entiers.
- Lever une exception `TypeError` si ce ne sont pas des entiers ou des flottants, avec des messages appropriés.

**Exemple d'exécution** :

```python
print(add_integer(1, 2))        # 3
print(add_integer(100, -2))     # 98
print(add_integer(2))           # 100
print(add_integer(100.3, -2))   # 98
```

### 1. Diviser une matrice

Écrire une fonction qui divise tous les éléments d'une matrice par un nombre.

Prototype : `def matrix_divided(matrix, div):`

- `matrix` doit être une liste de listes d'entiers ou de flottants.
- Chaque ligne de la matrice doit avoir la même taille.
- `div` doit être un nombre (entier ou flottant).
- `div` ne peut pas être égal à 0.

**Exemple d'exécution** :

```python
matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
print(matrix_divided(matrix, 3))  # [[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
```

### 2. Afficher mon nom

Écrire une fonction qui affiche le nom complet.

Prototype : `def say_my_name(first_name, last_name="")`

- `first_name` et `last_name` doivent être des chaînes de caractères.
- Si l'un des paramètres n'est pas une chaîne, lever une exception `TypeError`.

**Exemple d'exécution** :

```python
say_my_name("John", "Smith")     # My name is John Smith
say_my_name("Bob")               # My name is Bob
```

### 3. Afficher un carré

Écrire une fonction qui affiche un carré avec le caractère `#`.

Prototype : `def print_square(size):`

- `size` doit être un entier.
- Si `size` est inférieur à 0, lever une exception `ValueError`.
- Si `size` est un flottant et inférieur à 0, lever une exception `TypeError`.

**Exemple d'exécution** :

```python
print_square(4)
# ####
# ####
# ####
# ####

print_square(2)
# ##
# ##
```

### 4. Indentation du texte

Écrire une fonction qui imprime un texte avec 2 nouvelles lignes après les caractères : `.`, `?`, et `:`.

Prototype : `def text_indentation(text):`

- `text` doit être une chaîne de caractères.
- Si ce n’est pas une chaîne, lever une exception `TypeError`.

**Exemple d'exécution** :

```python
text_indentation("Lorem ipsum dolor sit amet. Quonam modo?")
# Lorem ipsum dolor sit amet.
#
# Quonam modo?
```

### 5. Max integer - Unittest

Écrire des tests unitaires pour la fonction `max_integer(list=[])`.

Prototype : `def max_integer(list=[]):`

- La fonction doit retourner le plus grand entier dans la liste.
- Utiliser `unittest` pour écrire et exécuter les tests.

**Exemple d'exécution** :

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
python3 -m unittest tests.6-max_integer_test
```

## Fichiers

- `0-add_integer.py` : Fonction pour additionner deux entiers.
- `2-matrix_divided.py` : Fonction pour diviser une matrice.
- `3-say_my_name.py` : Fonction pour afficher le nom.
- `4-print_square.py` : Fonction pour afficher un carré.
- `5-text_indentation.py` : Fonction pour l'indentation du texte.
- `6-max_integer.py` : Fonction pour trouver le plus grand entier dans une liste.
- `tests/0-add_integer.txt` : Fichier de tests pour `add_integer`.
- `tests/2-matrix_divided.txt` : Fichier de tests pour `matrix_divided`.
- `tests/3-say_my_name.txt` : Fichier de tests pour `say_my_name`.
- `tests/4-print_square.txt` : Fichier de tests pour `print_square`.
- `tests/5-text_indentation.txt` : Fichier de tests pour `text_indentation`.
- `tests/6-max_integer_test.py` : Fichier de tests unitaires pour `max_integer`.

## Instructions

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Kevindecastro/holbertonschool-higher_level_programming.git
   ```

2. Naviguer dans le répertoire du projet :
   ```bash
   cd python-test_driven_development
   ```

3. Implémenter et tester vos fonctions.

4. Exécuter tous les tests :
   ```bash
   python3 -m doctest ./tests/*
   ```

5. Pour les tests unitaires :
   ```bash
   python3 -m unittest tests.6-max_integer_test
   ```

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.