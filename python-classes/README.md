# Python - Classes et Objets

Ce projet explore les concepts fondamentaux de la programmation orientée objet (POO) en Python. Vous apprendrez à créer des classes, manipuler des objets, gérer des attributs privés, et appliquer des méthodes pour résoudre des problèmes de manière orientée objet.

## Introduction

Dans ce projet, nous explorons les bases de la programmation orientée objet en Python. Vous apprendrez à définir des classes, à gérer des attributs privés, et à créer des méthodes pour manipuler les données d'objets. Ce projet permet de comprendre comment la POO peut rendre votre code plus modulaire, réutilisable et plus facile à maintenir.

## Contenu

### Objectifs d'apprentissage

- Apprendre à définir et utiliser des classes en Python.
- Gérer des attributs privés et des méthodes d'accès.
- Manipuler les objets via leurs méthodes.
- Valider les données des objets avec des exceptions.
- Utiliser des propriétés pour un meilleur contrôle sur les attributs.

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

3. Assurez-vous que Python 3.8.5 est installé sur votre machine. Si ce n'est pas le cas, vous pouvez installer Python en suivant les instructions disponibles ici.

## Exécution

Les fichiers Python peuvent être exécutés directement à partir du terminal. Par exemple : 

   ```bash
   python3 0-square.py
   ```

Vous pouvez remplacer le nom du fichier par celui de la tâche que vous souhaitez exécuter.

### Tâches

0. **Classe Square vide**

- **Description** : Crée une classe Square sans attributs ni méthodes.
- **Prototype** : `class Square:`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('0-square').Square
   my_square = Square()
   print(type(my_square))  # <class '0-square.Square'>
   print(my_square.__dict__)  # {}
   ```

- [Code source](0-square.py)

1. **Attribut size**

- **Description** : Ajoute un attribut privé `size` à la classe Square pour représenter la taille du carré.
- **Prototype** : `def __init__(self, size):`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('1-square').Square
   my_square = Square(3)
   print(type(my_square))  # <class '1-square.Square'>
   print(my_square.__dict__)  # {'_Square__size': 3}
   ```

- [Code source](1-square.py)

2. **Validation de size**

- **Description** : Vérifie que `size` est un entier positif ou égal à zéro.
- **Prototype** : `def __init__(self, size=0):`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('2-square').Square
   my_square = Square(3)
   print(my_square.size)  # 3
   my_square = Square(-1)  # Erreur : size must be >= 0
   ```

- [Code source](2-square.py)

3. **Calcul de l'aire**

- **Description** : Ajoute une méthode `area()` pour calculer l'aire du carré.
- **Prototype** : `def area(self):`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('3-square').Square
   my_square = Square(3)
   print(my_square.area())  # 9
   ```

- [Code source](3-square.py)

4. **Propriétés et setters**

- **Description** : Utilise une propriété pour gérer l'attribut `size` et ses modifications.
- **Prototype** : `def size(self):` et `def size(self, value):`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('4-square').Square
   my_square = Square(3)
   print(my_square.size)  # 3
   my_square.size = 5
   print(my_square.size)  # 5
   ```

- [Code source](4-square.py)

5. **Affichage du carré**

- **Description** : Crée une méthode `my_print()` pour afficher un carré avec le caractère `#`.
- **Prototype** : `def my_print(self):`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('5-square').Square
   my_square = Square(3)
   my_square.my_print()
   # Affichage :
   # ###
   # ###
   # ###
   ```

- [Code source](5-square.py)

6. **Position du carré**

- **Description** : Ajoute un attribut `position` pour afficher le carré avec des espaces.
- **Prototype** : `def __init__(self, size, position=(0, 0)):`
- **Exemple d'utilisation** :
   ```bash
   Square = __import__('6-square').Square
   my_square = Square(3, (1, 1))
   my_square.my_print()
   # Affichage :
   #  ###
   #  ###
   #  ###
   ```

- [Code source](6-square.py)

### Références utiles

- Documentation Python - Classes
- Python Class and Object

---

**Dépôt GitHub :** [holbertonschool-higher_level_programming](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/tree/main/python-classes)

---

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.

---
