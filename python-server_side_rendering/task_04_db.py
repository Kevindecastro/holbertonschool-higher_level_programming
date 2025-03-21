import sqlite3
from flask import Flask, render_template, request

# Initialisation de l'application Flask
app = Flask(__name__)


def read_sqlite(product_id=None):
    """
    Lit et retourne les données depuis une base de données SQLite.

    Args:
        product_id (str, optional): ID du produit à filtrer. Par défaut à None.

    Returns:
        list: Données lues depuis la base de données.
    """
    conn = sqlite3.connect('data/products.db')
    cursor = conn.cursor()
    # Exécute la requête SQL en fonction de l'ID
    if product_id:
        cursor.execute('SELECT * FROM Products WHERE id = ?', (product_id,))
    else:
        cursor.execute('SELECT * FROM Products')
    data = cursor.fetchall()
    conn.close()
    # Convertit les données en liste de dictionnaires
    return [dict(id=row[0], name=row[1], category=row[2], price=row[3])
            for row in data]


@app.route('/products')
def products():
    """
    Route pour afficher les produits.
    Lit les données depuis un fichier JSON, CSV ou une base de données SQLite.
    Filtre les produits par 'id' si spécifié.
    """
    # Récupère les paramètres de la requête
    source = request.args.get('source')
    product_id = request.args.get('id')

    # Lit les données en fonction de la source
    if source == 'json':
        data = read_json('data/products.json')
    elif source == 'csv':
        data = read_csv('data/products.csv')
    elif source == 'sql':
        data = read_sqlite(product_id)
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtre les données par 'id' si spécifié
    if product_id and not data:
        return render_template(
            'product_display.html', error="Product not found")

    # Rend le template avec les produits
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    # Lance l'application Flask en mode debug sur le port 5000
    app.run(debug=True, port=5000)
