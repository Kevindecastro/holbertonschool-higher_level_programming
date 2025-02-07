```markdown
# Python - Inheritance

## Description

Ce projet explore l'héritage en Python, un concept clé de la programmation orientée objet. Vous apprendrez à créer des classes qui héritent d'autres classes, à manipuler des méthodes et des attributs hérités, et à comprendre l'utilisation des fonctions intégrées comme `isinstance`, `issubclass`, `super` et bien d'autres.

## Learning Objectives

À la fin de ce projet, vous devriez être capable d'expliquer les concepts suivants :

- Qu'est-ce qu'une classe parente (superclasse, baseclass) ?
- Qu'est-ce qu'une classe enfant (subclass) ?
- Comment lister les attributs et méthodes d'une classe ou d'une instance ?
- Quand une instance peut-elle avoir de nouveaux attributs ?
- Comment hériter d'une classe ?
- Comment définir une classe avec plusieurs classes de base ?
- Quelle est la classe par défaut dont chaque classe hérite ?
- Comment redéfinir une méthode ou un attribut hérité ?
- Quelles sont les méthodes et attributs accessibles par héritage ?
- À quoi sert l'héritage ?
- Comment utiliser `isinstance`, `issubclass`, `type` et `super` ?

## Requirements

- Python 3.8.5
- Éditeurs autorisés : vi, vim, emacs
- Le premier caractère de chaque fichier doit être `#!/usr/bin/python3`
- Chaque fichier doit se terminer par une nouvelle ligne
- La documentation doit être présente pour chaque module, classe et fonction
- Le code doit être conforme au style PEP8

## Tasks

### 0. Lookup

Écrire une fonction `lookup()` qui retourne la liste des attributs et méthodes disponibles pour un objet donné.

#### Prototype : 
```python
def lookup(obj):
```

### 1. My List

Créer une classe `MyList` qui hérite de `list` et implémente une méthode `print_sorted()` pour imprimer la liste triée par ordre croissant.

#### Prototype : 
```python
def print_sorted(self):
```

### 2. Exact same object

Écrire une fonction `is_same_class()` qui retourne `True` si l'objet est exactement une instance de la classe spécifiée, sinon `False`.

#### Prototype : 
```python
def is_same_class(obj, a_class):
```

### 3. Same class or inherit from

Écrire une fonction `is_kind_of_class()` qui retourne `True` si l'objet est une instance de la classe spécifiée ou d'une classe héritée de cette classe.

#### Prototype : 
```python
def is_kind_of_class(obj, a_class):
```

### 4. Only sub class of

Écrire une fonction `inherits_from()` qui retourne `True` si l'objet est une instance d'une classe héritée directement ou indirectement de la classe spécifiée.

#### Prototype : 
```python
def inherits_from(obj, a_class):
```

### 5. Geometry module

Créer une classe `BaseGeometry` vide.

#### Prototype : 
```python
class BaseGeometry:
```

### 6. Improve Geometry

Étendre `BaseGeometry` en y ajoutant la méthode `area()`, qui lève une exception avec le message `"area() is not implemented"`.

#### Prototype : 
```python
def area(self):
```

### 7. Integer validator

Ajouter à la classe `BaseGeometry` la méthode `integer_validator()`, qui valide un entier en vérifiant que :
- La valeur est un entier
- La valeur est strictement supérieure à 0

#### Prototype : 
```python
def integer_validator(self, name, value):
```

## Test Cases

Tous les tests sont dans le dossier `tests/` et utilisent la commande `python3 -m doctest ./tests/*` pour les exécuter.

## Repo

- GitHub repository: [holbertonschool-higher_level_programming](https://github.com/Kevindecastro/holbertonschool-higher_level_programming)
- Directory: python-inheritance

## Installation et Exécution

Aucune installation supplémentaire n'est requise. Ce projet utilise uniquement Python3.

```bash
python3 -m doctest ./tests/*
```

## Auteurs

- **Kevin De Castro** : Étudiant à la Holberton School.

## License

Ce projet est sous la licence [MIT](https://opensource.org/licenses/MIT).
