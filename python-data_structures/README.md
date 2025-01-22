# Python - Structures de Données : Listes, Tuples

## Description

Bienvenue dans le projet **Python - Structures de Données : Listes, Tuples** ! Ce projet contient une série d'exercices visant à pratiquer l'utilisation des listes et des tuples en Python. L'objectif est d'améliorer vos compétences en manipulation de structures de données de base.

### Objectifs d'apprentissage

À la fin de ce projet, vous serez capable d'expliquer les éléments suivants :

- Ce que sont les listes et comment les utiliser.
- Les différences et similarités entre les chaînes de caractères et les listes.
- Les méthodes les plus courantes des listes et comment les utiliser.
- Comment utiliser les listes comme piles et files d'attente.
- Ce que sont les compréhensions de listes et comment les utiliser.
- Ce que sont les tuples et comment les utiliser.
- Quand utiliser des tuples par rapport à des listes.
- Ce qu'est une séquence.
- Ce qu'est le "tuple packing".
- Ce qu'est le "sequence unpacking".
- Ce qu'est l'instruction `del` et comment l'utiliser.

## Prérequis

- Python 3.8+ installé.
- Compétences de base en programmation Python.
- Un éditeur de texte comme `vim`, `emacs` ou `vi`.

## Tâches

### 0. Imprimer une liste d'entiers
Un programme qui imprime tous les entiers d'une liste.

- Prototype : `def print_list_integer(my_list=[]):`
- Format : un entier par ligne.
- Vous n'êtes pas autorisé à importer de module.
- Vous pouvez supposer que la liste ne contient que des entiers.
- Vous ne devez pas convertir les entiers en chaînes de caractères.
- Vous devez utiliser `str.format()` pour imprimer les entiers.

### 1. Accès sécurisé à un élément dans une liste
Un programme qui récupère un élément d'une liste.

- Prototype : `def element_at(my_list, idx):`
- Si `idx` est négatif, la fonction doit retourner `None`.
- Si `idx` est hors limite (> nombre d'éléments dans `my_list`), la fonction doit retourner `None`.
- Vous n'êtes pas autorisé à importer de module.
- Vous n'êtes pas autorisé à utiliser `try/except`.

### 2. Remplacer un élément
Un programme qui remplace un élément d'une liste à une position spécifique.

- Prototype : `def replace_in_list(my_list, idx, element):`
- Si `idx` est négatif, la fonction ne doit rien modifier et retourne la liste originale.
- Si `idx` est hors limite (> nombre d'éléments dans `my_list`), la fonction ne doit rien modifier et retourne la liste originale.
- Vous n'êtes pas autorisé à importer de module.
- Vous n'êtes pas autorisé à utiliser `try/except`.

### 3. Imprimer une liste d'entiers... à l'envers !
Un programme qui imprime tous les entiers d'une liste, dans l'ordre inverse.

- Prototype : `def print_reversed_list_integer(my_list=[]):`
- Format : un entier par ligne.
- Vous n'êtes pas autorisé à importer de module.
- Vous pouvez supposer que la liste ne contient que des entiers.
- Vous ne devez pas convertir les entiers en chaînes de caractères.
- Vous devez utiliser `str.format()` pour imprimer les entiers.

### 4. Remplacer dans une copie
Un programme qui remplace un élément dans une liste à une position spécifique sans modifier la liste originale.

- Prototype : `def new_in_list(my_list, idx, element):`
- Si `idx` est négatif, la fonction doit retourner une copie de la liste originale.
- Si `idx` est hors limite (> nombre d'éléments dans `my_list`), la fonction doit retourner une copie de la liste originale.
- Vous n'êtes pas autorisé à importer de module.
- Vous n'êtes pas autorisé à utiliser `try/except`.

### 5. Pouvez-vous me voir maintenant ?
Un programme qui supprime tous les caractères `c` et `C` d'une chaîne de caractères.

- Prototype : `def no_c(my_string):`
- La fonction doit retourner la nouvelle chaîne.
- Vous n'êtes pas autorisé à importer de module.
- Vous n'êtes pas autorisé à utiliser `str.replace()`.

### 6. Listes de listes = Matrice
Un programme qui imprime une matrice d'entiers.

- Prototype : `def print_matrix_integer(matrix=[[]]):`
- Format : voir l'exemple.
- Vous n'êtes pas autorisé à importer de module.
- Vous pouvez supposer que la liste ne contient que des entiers.
- Vous ne devez pas convertir les entiers en chaînes de caractères.
- Vous devez utiliser `str.format()` pour imprimer les entiers.

### 7. Addition de tuples
Un programme qui ajoute 2 tuples.

- Prototype : `def add_tuple(tuple_a=(), tuple_b=()):`
- Retourne un tuple avec 2 entiers :
  - Le premier élément doit être la somme du premier élément de chaque argument.
  - Le second élément doit être la somme du second élément de chaque argument.
- Vous n'êtes pas autorisé à importer de module.
- Vous pouvez supposer que les deux tuples ne contiennent que des entiers.
- Si un tuple est plus petit que 2, utilisez la valeur 0 pour chaque entier manquant.
- Si un tuple est plus grand que 2, utilisez uniquement les 2 premiers entiers.

### 8. Plus de retours !
Un programme qui retourne un tuple avec la longueur d'une chaîne et son premier caractère.

- Prototype : `def multiple_returns(sentence):`
- Si la chaîne est vide, le premier caractère doit être égal à `None`.
- Vous n'êtes pas autorisé à importer de module.

### 9. Trouver le max
Un programme qui trouve le plus grand entier d'une liste.

- Prototype : `def max_integer(my_list=[]):`
- Si la liste est vide, retournez `None`.
- Vous pouvez supposer que la liste ne contient que des entiers.
- Vous n'êtes pas autorisé à importer de module.
- Vous n'êtes pas autorisé à utiliser la fonction `max()` intégrée.

### 10. Seulement par 2
Un programme qui trouve tous les multiples de 2 dans une liste.

- Prototype : `def divisible_by_2(my_list=[]):`
- Retourne une nouvelle liste avec `True` ou `False`, en fonction de si l'entier à la même position dans la liste originale est un multiple de 2.
- La nouvelle liste doit avoir la même taille que la liste originale.
- Vous n'êtes pas autorisé à importer de module.

### 11. Supprimer à
Un programme qui supprime l'élément à une position spécifique dans une liste.

- Prototype : `def delete_at(my_list=[], idx=0):`
- Si `idx` est négatif ou hors limite, rien ne change (retourne la même liste).
- Vous n'êtes pas autorisé à utiliser `pop()`.
- Vous n'êtes pas autorisé à importer de module.

### 12. Switch
Complétez le code source pour intervertir les valeurs de `a` et `b`.

- Votre code doit être inséré là où se trouve le commentaire (ligne 4).
- Votre programme doit être exactement de 5 lignes.

## Exigences

- Tous les scripts doivent être exécutés avec Python 3.
- Tous les fichiers doivent se terminer par une nouvelle ligne.
- La première ligne de chaque fichier doit être exactement `#!/usr/bin/python3`.
- Le style de codage doit respecter la norme PEP8 (utilisez `pycodestyle` pour vérifier votre code).
- Un fichier `README.md` à la racine du projet est obligatoire.
- Les fichiers doivent être exécutables.
- La longueur des fichiers sera testée avec la commande `wc`.

## Exécution du Code

Pour exécuter les programmes :

1. Clonez ce dépôt GitHub dans votre répertoire local.
2. Exécutez chaque fichier Python avec la commande suivante :

```bash
chmod +x <fichier.py>  # Rendre le fichier exécutable
./<fichier.py>          # Exécuter le fichier
```

## Auteurs

- **Kevin De Castro** : Étudiant à la Holberton School

## License

Ce projet est sous la licence [MIT](https://opensource.org/licenses/MIT).
