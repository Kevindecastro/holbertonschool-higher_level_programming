# Python - Input/Output

## Description

Ce projet porte sur la gestion des entrées et sorties en Python, avec un accent particulier sur la lecture et l'écriture de fichiers, la manipulation du format JSON et la sérialisation/désérialisation des objets.

## Exigences

- Python 3.8.5 (ou version supérieure)
- Tous les fichiers doivent se terminer par une nouvelle ligne.
- Le code doit être exécuté sur Ubuntu 20.04 LTS avec Python 3.
- Votre code doit respecter la norme `pycodestyle` (version 2.7.*).
- Les fichiers de tests doivent être dans le dossier `tests` et avoir l'extension `.txt`.
- Le code doit inclure une documentation appropriée avec des docstrings pour chaque fonction et module.
- Les tests doivent être exécutés avec la commande : `python3 -m doctest ./tests/*`.

## Tâches

### 0. Lecture d'un fichier

Écrire une fonction qui lit un fichier texte et affiche son contenu.

Prototype : `def read_file(filename=""):`

**Exemple d'exécution** :

```python
read_file("my_file.txt")
```

### 1. Écriture dans un fichier

Écrire une fonction qui écrit une chaîne de caractères dans un fichier texte et retourne le nombre de caractères écrits.

Prototype : `def write_file(filename="", text=""):`

### 2. Ajout dans un fichier

Écrire une fonction qui ajoute une chaîne de caractères à un fichier texte et retourne le nombre de caractères ajoutés.

Prototype : `def append_write(filename="", text=""):`

### 3. Sérialisation en JSON

Écrire une fonction qui renvoie la représentation JSON d'un objet Python.

Prototype : `def to_json_string(my_obj):`

### 4. Désérialisation en objet Python

Écrire une fonction qui retourne un objet Python à partir de sa représentation JSON.

Prototype : `def from_json_string(my_str):`

### 5. Sauvegarde d'objet en fichier JSON

Écrire une fonction qui écrit un objet Python dans un fichier sous forme JSON.

Prototype : `def save_to_json_file(my_obj, filename):`

### 6. Chargement d'un fichier JSON

Écrire une fonction qui crée un objet Python à partir d'un fichier JSON.

Prototype : `def load_from_json_file(filename):`

### 7. Gestion d'arguments avec JSON

Écrire un programme qui ajoute tous les arguments de la ligne de commande à une liste, puis les enregistre dans un fichier JSON.

Fichier exécutable : `add_item.py`

### 8. Conversion d'un dictionnaire en JSON

Écrire une fonction qui renvoie le dictionnaire d'un objet pour la sérialisation JSON.

Prototype : `def class_to_json(obj):`

### 9. Classe Student

Définir une classe `Student` avec une méthode pour convertir l'objet en dictionnaire JSON.

### 10. Filtrage des attributs JSON

Modifier la classe `Student` pour permettre de sélectionner certains attributs lors de la conversion en JSON.

### 11. Création d'un objet Student à partir d'un JSON

Ajouter une méthode `reload_from_json(self, json)` à `Student` pour mettre à jour ses attributs à partir d'un dictionnaire JSON.

### 12. Triangle de Pascal

Écrire une fonction qui génère le Triangle de Pascal jusqu'à `n` lignes.

Prototype : `def pascal_triangle(n):`

## Fichiers

- `0-read_file.py` : Lecture d'un fichier texte.
- `1-write_file.py` : Écriture dans un fichier texte.
- `2-append_write.py` : Ajout de texte dans un fichier.
- `3-to_json_string.py` : Conversion d'un objet en JSON.
- `4-from_json_string.py` : Conversion JSON en objet Python.
- `5-save_to_json_file.py` : Sauvegarde d'un objet en fichier JSON.
- `6-load_from_json_file.py` : Chargement d'un fichier JSON en objet Python.
- `7-add_item.py` : Script pour sauvegarder des arguments dans un fichier JSON.
- `8-class_to_json.py` : Fonction pour convertir un objet en dictionnaire JSON.
- `9-student.py` : Classe `Student` avec méthodes de conversion JSON.
- `10-student.py` : Classe `Student` avec filtrage JSON.
- `11-student.py` : Classe `Student` avec mise à jour depuis un JSON.
- `12-pascal_triangle.py` : Fonction pour le Triangle de Pascal.

## Instructions

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/Kevindecastro/holbertonschool-higher_level_programming/python-input_output
   ```

2. Naviguer dans le répertoire du projet :
   ```bash
   cd python-input_output
   ```

3. Implémenter et tester vos fonctions.

4. Exécuter tous les tests :
   ```bash
   python3 -m doctest ./tests/*
   ```

## Auteurs

Kevin De Castro : Étudiant à la Holberton School

## License

Ce projet est sous la licence MIT.

