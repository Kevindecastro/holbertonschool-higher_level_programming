#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    # Vérifier que le bon nombre d'arguments a été passé
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_state.py <mysql username> <mysql password> <database name>")
        sys.exit(1)

    # Récupérer les arguments
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connexion à la base de données MySQL
    db = MySQLdb.connect(
        host="localhost", 
        port=3306, 
        user=username, 
        passwd=password, 
        db=db_name
    )

    # Créer un curseur pour exécuter la requête
    cursor = db.cursor()

    # Exécuter la requête SQL pour récupérer les villes et les états
    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cursor.execute(query)

    # Récupérer les résultats et les afficher
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Fermer le curseur et la connexion
    cursor.close()
    db.close()
