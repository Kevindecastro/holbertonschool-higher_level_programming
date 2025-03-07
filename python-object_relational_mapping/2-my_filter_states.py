#!/usr/bin/python3
"""Lists all states where 'name' matches the user input from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    # Récupération des arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Connexion à la base de données
    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
    cursor = db.cursor()
    
    # Exécution de la requête SQL avec format (vulnérable aux injections SQL)
    query = "SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name)
    cursor.execute(query)

    # Affichage des résultats
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cursor.close()
    db.close()
