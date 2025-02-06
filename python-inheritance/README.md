# Projet Python : Héritage des Classes

## Description
Ce projet explore le concept d'héritage en Python en développant une classe de base `Person` et une classe dérivée `Student`. L'objectif est de comprendre comment utiliser l'héritage pour éviter la redondance du code et enrichir les fonctionnalités d'une classe en la spécialisant.

## Fichiers
- `person.py` : Contient la définition de la classe `Person`.
- `student.py` : Contient la définition de la classe `Student`, qui hérite de `Person`.
- `tests/test_student.txt` : Contient des tests pour valider le bon fonctionnement des classes.

## Installation et Exécution
Aucune installation supplémentaire n'est requise. Ce projet utilise uniquement Python3.

```bash
python3 -m doctest ./tests/*
```

## Classes et Méthodes

### `Person`
Classe de base représentant une personne.

#### Attributs :
- `name` (str) : Nom de la personne.
- `age` (int) : Age de la personne.

#### Méthodes :
- `__init__(self, name, age)`: Initialise un objet `Person`.
- `introduce(self)`: Retourne une chaîne de caractères présentant la personne.

Exemple d'utilisation :
```python
p = Person("Alice", 30)
print(p.introduce())  # Bonjour, je m'appelle Alice et j'ai 30 ans.
```

---

### `Student`
Classe dérivée de `Person`, représentant un étudiant.

#### Attributs :
- `name` (str) : Nom de l'étudiant.
- `age` (int) : Age de l'étudiant.
- `school` (str) : École de l'étudiant.

#### Méthodes :
- `__init__(self, name, age, school)`: Initialise un objet `Student`.
- `introduce(self)`: Redéfinit la méthode pour inclure l'école de l'étudiant.

Exemple d'utilisation :
```python
s = Student("Bob", 22, "Holberton School")
print(s.introduce())  # Bonjour, je m'appelle Bob et j'ai 22 ans. Je suis étudiant à Holberton School.
```

## Tests
Les tests sont définis dans `tests/test_student.txt` et peuvent être exécutés avec doctest :

```
>>> s = Student("Alice", 22, "Holberton School")
>>> s.introduce()
"Bonjour, je m'appelle Alice et j'ai 22 ans. Je suis étudiant à Holberton School."
```

## Auteur
Projet réalisé dans le cadre du programme Holberton School.

## Licence
Ce projet est sous licence MIT.

