#!/usr/bin/python3
"""Lists all states where 'name' matches the user input from the database"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect("localhost", argv[1], argv[2], argv[3])
    cur = db.cursor()

    # Exécution de la requête SQL avec format (vulnérable aux injections SQL)
    cur.execute(
        "SELECT * FROM states WHERE name = %s ORDER BY id ASC", (argv[4],)
        )

    # Affichage des résultats
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Fermeture du curseur et de la connexion
    cur.close()
    db.close()
