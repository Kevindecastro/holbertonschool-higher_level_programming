# Python - Server-Side Rendering

Ce projet vise à implémenter le **Server-Side Rendering (SSR)** en utilisant Python et le framework Flask. Vous apprendrez à générer des pages web côté serveur et à les envoyer au client sous forme de HTML complet.

## Objectifs d'apprentissage

1. Comprendre les concepts de **Server-Side Rendering** et en quoi il diffère du **Client-Side Rendering**.
2. Apprendre les avantages du **Server-Side Rendering** dans le développement web.
3. Implémenter le SSR en Python en utilisant le framework Flask.
4. Utiliser le moteur de templating **Jinja** pour générer dynamiquement des pages HTML.
5. Lire et afficher des données à partir de diverses sources, notamment JSON, CSV et des bases de données SQLite.
6. Gérer du contenu dynamique et des entrées utilisateur dans des applications web.

## Structure du projet

Le projet est divisé en plusieurs tâches, chacune visant à vous faire progresser dans la compréhension et l'implémentation du SSR avec Flask et Jinja.

### Tâches

1. **Tâche 0** : Création d'un programme de templating simple.
2. **Tâche 1** : Création d'un Template HTML de base avec Flask.
3. **Tâche 2** : Création d'un Template Dynamique avec des Boucles et des Conditions dans Flask.
4. **Tâche 3** : Affichage de Données à partir de Fichiers JSON ou CSV dans Flask.
5. **Tâche 4** : Extension de l'Affichage de Données pour Inclure SQLite dans Flask.

### Structure du projet
```
python-server_side_rendering/
│
├── templates/                     # Dossier contenant les templates HTML
│   ├── index.html                 # Page d'accueil
│   ├── about.html                 # Page "À propos"
│   ├── contact.html               # Page "Contact"
│   ├── items.html                 # Page pour afficher les items dynamiques
│   ├── product_display.html       # Page pour afficher les produits
│   ├── header.html                # En-tête réutilisable
│   └── footer.html                # Pied de page réutilisable
│
├── data/                          # Dossier contenant les fichiers de données
│   ├── items.json                 # Fichier JSON pour les items
│   ├── products.json              # Fichier JSON pour les produits
│   ├── products.csv               # Fichier CSV pour les produits
│   └── products.db                # Base de données SQLite pour les produits
│
├── task_00_intro.py               # Script pour la tâche 0 (templating simple)
├── task_01_jinja.py               # Script pour la tâche 1 (template HTML de base)
├── task_02_logic.py               # Script pour la tâche 2 (template dynamique avec boucles et conditions)
├── task_03_files.py               # Script pour la tâche 3 (affichage de données JSON/CSV)
├── task_04_db.py                  # Script pour la tâche 4 (affichage de données SQLite)
│
├── README.md                      # Documentation du projet
└── requirements.txt               # Fichier des dépendances
```
### Installation

1. Clonez ce dépôt.
2. Installez les dépendances nécessaires :
   ```bash
   pip install Flask
   ```
3. Exécutez les fichiers Python correspondants à chaque tâche.

### Exécution

Pour exécuter l'application Flask, utilisez la commande suivante :

```bash
python3 task_01_jinja.py
```

## Auteur

Kevin De Castro : Étudiant à la Holberton School

### Licence

Ce projet est sous licence MIT. Voir le fichier LICENSE pour plus de détails.
