# SQL - Introduction

## Description
Ce projet est une introduction aux bases de données relationnelles et à MySQL. Il couvre la création et la gestion de bases de données, de tables, ainsi que l'utilisation des requêtes SQL pour manipuler les données.

## Technologies
- Langage : SQL
- SGBD : MySQL 8.0
- Environnement : Ubuntu 20.04 LTS
- Style : Conformité avec les standards SQL

## Fichiers
Chaque fichier SQL contient une instruction ou un ensemble d'instructions correspondant à une tâche spécifique du projet.

| Fichier | Description |
|---------|------------|
| `0-list_databases.sql` | Liste toutes les bases de données MySQL présentes sur le serveur. |
| `1-create_database_if_missing.sql` | Crée une base de données si elle n'existe pas. |
| `2-remove_database.sql` | Supprime une base de données si elle existe. |
| `3-list_tables.sql` | Liste toutes les tables d'une base de données donnée. |
| `4-first_table.sql` | Crée une table simple si elle n'existe pas. |
| `5-full_table.sql` | Affiche la structure de la table précédemment créée. |
| `6-list_values.sql` | Affiche toutes les lignes de la table de la base de données. |
| `7-insert_value.sql` | Ajoute une nouvelle valeur à la table. |
| `8-count_89.sql` | Compte le nombre de lignes contenant une valeur spécifique. |
| `9-full_creation.sql` | Crée une table avec des contraintes et insère des valeurs. |
| `10-top_score.sql` | Sélectionne et affiche des valeurs sous conditions. |
| `11-best_score.sql` | Affiche les valeurs triées par ordre décroissant. |
| `12-no_cheating.sql` | Met à jour une valeur spécifique d'une table. |
| `13-change_class.sql` | Met à jour plusieurs valeurs d'une table sous condition. |
| `14-average.sql` | Calcule la moyenne d'une colonne de la table. |
| `15-groups.sql` | Regroupe les résultats par catégorie et les compte. |
| `16-no_link.sql` | Sélectionne et affiche des entrées qui ne sont pas en relation avec une autre table. |

## Utilisation
Pour exécuter un fichier SQL, utilisez la commande suivante :
```bash
mysql -h localhost -u root -p < fichier.sql
```

Exemple :
```bash
mysql -h localhost -u root -p < 0-list_databases.sql
```

## Auteur

Kevin De Castro : Étudiant à la Holberton School
