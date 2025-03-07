#!/usr/bin/python3
"""Lists all states where 'name' matches the user input from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Connexion à la base de données MySQL avec les arguments fournis
    db = MySQLdb.connect(
        host="localhost",  # Hôte de la base de données
        user=sys.argv[1],  # Nom d'utilisateur MySQL
        passwd=sys.argv[2],  # Mot de passe MySQL
        db=sys.argv[3],  # Nom de la base de données
        port=3306  # Port MySQL par défaut
    )

    # Création du curseur pour exécuter la requête
    cur = db.cursor()

    # Construction et exécution de la requête SQL
    query = (
        "SELECT * FROM states "
        "WHERE name LIKE BINARY '{}' "
        "ORDER BY states.id ASC"
    ).format(sys.argv[4])  # Utilisation de format() pour insérer l'entrée utilisateur

    cur.execute(query)

    # Affichage des résultats
    for row in cur.fetchall():
        print(row)

    # Fermeture du curseur et de la connexion à la base de données
    cur.close()
    db.close()
