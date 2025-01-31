# Python - Plus de Classes et d'Objets

![Python](https://img.shields.io/badge/Python-3.8.5-blue.svg)

## Description

Ce projet fait partie du programme de l'école Holberton et vise à approfondir la compréhension de la Programmation Orientée Objet (POO) en Python. L'objectif est d'implémenter une classe `Rectangle` avec diverses fonctionnalités avancées, incluant des attributs, des méthodes, des propriétés, des attributs de classe et des méthodes spéciales.

## Table des Matières

- [Requirements](#requirements)
- [Tâches](#tâches)
- [Fichiers](#fichiers)
- [Utilisation](#utilisation)
- [Auteur](#auteur)

## Requirements

- **Version de Python** : 3.8.5
- **Guide de style** : PEP 8 (pycodestyle)
- **Format des fichiers** : Chaque fichier doit se terminer par une nouvelle ligne.
- **Fichiers exécutables** : Tous les fichiers doivent être exécutables.
- **Shebang** : La première ligne de tous les fichiers doit être `#!/usr/bin/python3`.

## Tâches

### 0. Rectangle Simple
- **Fichier** : `0-rectangle.py`
- **Description** : Crée une classe `Rectangle` vide.

### 1. Définition Réelle d'un Rectangle
- **Fichier** : `1-rectangle.py`
- **Description** : Définis une classe `Rectangle` avec des attributs privés `width` (largeur) et `height` (hauteur), ainsi que des getters et setters.

### 2. Aire et Périmètre
- **Fichier** : `2-rectangle.py`
- **Description** : Ajoute des méthodes pour calculer l'aire et le périmètre du rectangle.

### 3. Représentation en Chaîne de Caractères
- **Fichier** : `3-rectangle.py`
- **Description** : Implémente les méthodes `__str__` et `__repr__` pour afficher le rectangle sous forme de chaîne de caractères.

### 4. `eval` est Magique
- **Fichier** : `4-rectangle.py`
- **Description** : Modifie `__repr__` pour permettre la recréation de l'objet avec `eval`.

### 5. Détection de la Suppression d'une Instance
- **Fichier** : `5-rectangle.py`
- **Description** : Ajoute un destructeur pour afficher un message lors de la suppression d'une instance.

### 6. Compter les Instances
- **Fichier** : `6-rectangle.py`
- **Description** : Ajoute un attribut de classe pour compter le nombre d'instances de `Rectangle`.

### 7. Changer la Représentation
- **Fichier** : `7-rectangle.py`
- **Description** : Ajoute un attribut de classe `print_symbol` pour personnaliser l'affichage du rectangle.

### 8. Comparer des Rectangles
- **Fichier** : `8-rectangle.py`
- **Description** : Ajoute une méthode statique pour comparer deux rectangles en fonction de leur aire.

### 9. Un Carré est un Rectangle
- **Fichier** : `9-rectangle.py`
- **Description** : Ajoute une méthode de classe pour créer un carré (rectangle avec `width == height`).


## Utilisation

Pour exécuter les scripts, utilise la commande suivante dans ton terminal :

```bash
./<nom_du_fichier>.py
```

Par exemple, pour exécuter le script `0-rectangle.py` :

```bash
./0-main.py
```

---

**Dépôt GitHub :** [holbertonschool-higher_level_programming](https://github.com/Kevindecastro/holbertonschool-higher_level_programming/tree/main/python-more_classes)

---

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.

---
