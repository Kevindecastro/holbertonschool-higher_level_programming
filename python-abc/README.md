# Python - Abstract Classes and Interfaces

---

## Description
Ce projet explore des concepts avancés de la programmation orientée objet (POO) en Python, notamment les classes abstraites, les interfaces, le duck typing et l'héritage. L'objectif est de renforcer la compréhension et l'application de ces principes pour concevoir, implémenter et tester des programmes Python robustes.

## Objectifs d'apprentissage
- **Classes Abstraites** : Comprendre et utiliser les classes abstraites pour imposer des interfaces communes et structurer le code.
- **Interfaces et Duck Typing** : Appliquer le concept de duck typing pour créer des objets respectant un contrat spécifique sans vérification explicite du type.
- **Sous-classage des classes standards** : Étendre des classes de base comme `list`, `dict` et `iterator` pour créer des structures de données personnalisées.
- **Surcharge de méthodes** : Modifier ou étendre le comportement des méthodes d'une classe mère.
- **Héritage multiple** : Comprendre et appliquer l'héritage multiple pour modéliser des relations complexes entre classes.
- **Mixins** : Utiliser des mixins pour ajouter des fonctionnalités de manière modulaire.

## Ressources
- [Python 3 Object-Oriented Programming](https://docs.python.org/3/tutorial/classes.html)
- [ABC — Abstract Base Classes](https://docs.python.org/3/library/abc.html)
- [Real Python - OOP in Python 3](https://realpython.com/python3-object-oriented-programming/)
- [Corey Schafer - OOP Playlist](https://www.youtube.com/playlist?list=PL-osiE80TeTt2d9bfVyTiXJA-UTHn6WwU)
- [sentdex - Python OOP Tutorial](https://www.youtube.com/playlist?list=PLQVvvaa0QuDfV1MIRBOcqClP6VZXsvyZS)

---

## Tâches

---

### 0. Classe Abstraite Animal et ses sous-classes
**Objectif :** Créer une classe abstraite `Animal` avec une méthode abstraite `sound`, puis implémenter les classes `Dog` et `Cat` qui en héritent.

**Fichier :** `task_00_abc.py`

---

### 1. Formes, Interfaces et Duck Typing
**Objectif :** Définir une classe abstraite `Shape` avec les méthodes `area` et `perimeter`, puis implémenter `Circle` et `Rectangle`. Une fonction `shape_info` affichera les informations sur ces formes en utilisant le duck typing.

**Fichier :** `task_01_duck_typing.py`

---

### 2. Extension de `list` avec Notifications
**Objectif :** Créer une classe `VerboseList` qui hérite de `list` et affiche des messages lorsqu'on ajoute ou supprime des éléments (`append`, `extend`, `remove`, `pop`).

**Fichier :** `task_02_verboselist.py`

---

### 3. Itérateur Compté
**Objectif :** Implémenter `CountedIterator`, une classe qui suit le nombre d'éléments itérés en surchargeant la méthode `__next__`.

**Fichier :** `task_03_countediterator.py`

---

### 4. Poisson-Volant et Héritage Multiple
**Objectif :** Créer une classe `FlyingFish` qui hérite à la fois de `Fish` et `Bird`, et explore l'ordre de résolution des méthodes (MRO).

**Fichier :** `task_04_flyingfish.py`

---

### 5. Le Dragon Mystique et les Mixins
**Objectif :** Implémenter `SwimMixin` et `FlyMixin` pour ajouter les méthodes `swim` et `fly` à une classe `Dragon`, qui aura aussi une méthode `roar`.

**Fichier :** `task_05_dragon.py`

---

## Organisation du projet
- **Dépôt GitHub** : [holbertonschool-higher_level_programming](https://github.com/Kevindecastro/holbertonschool-higher_level_programming)
- **Répertoire du projet** : `python-abc`
- **Tests** : Tous les tests sont situés dans le répertoire `tests/` et peuvent être exécutés avec :
  ```bash
  python3 -m doctest ./tests/*
  ```
- **Normes de code** :
  - Respect du style PEP8 (`pycodestyle`)
  - Documentation complète pour chaque module, classe et fonction (`__doc__`)
  - Ligne vide à la fin de chaque fichier
  - Longueur des lignes limitée à 79 caractères

---

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.

---
