#!/usr/bin/python3
"""
Mmodule that takes arguments and prints all values
in the hbtn_0e_0_usa state table where the name
matches the argument and is safe from MySQL injections
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    # Connexion à la base de données
    db = MySQLdb.connect(
        host="localhost",
        user=argv[1],
        passwd=argv[2],
        db=argv[3],
        port=3306,
    )

    # Création d'un curseur
    cur = db.cursor()

    # Exécution de la requête SQL
    cur.execute("""SELECT *
                FROM states
                WHERE name = %(state)s
                ORDER BY id ASC""", {'state': argv[4]})
    rows = cur.fetchall()

    # Récupération et affichage des résultats
    for row in rows:
        if row[1] == argv[4]:
            print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
