import json
import csv
from flask import Flask, render_template, request

# Initialisation de l'application Flask
app = Flask(__name__)


def read_json(file_path):
    """
    Lit et retourne les données d'un fichier JSON.

    Args:
        file_path (str): Chemin du fichier JSON.

    Returns:
        list: Données lues depuis le fichier JSON.
    """
    with open(file_path, 'r') as file:
        return json.load(file)


def read_csv(file_path):
    """
    Lit et retourne les données d'un fichier CSV.

    Args:
        file_path (str): Chemin du fichier CSV.

    Returns:
        list: Données lues depuis le fichier CSV.
    """
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        return list(reader)


@app.route('/products')
def products():
    """
    Route pour afficher les produits.
    Lit les données depuis un fichier JSON ou CSV en fonction du paramètre 'source'.
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
    else:
        return render_template('product_display.html', error="Wrong source")

    # Filtre les données par 'id' si spécifié
    if product_id:
        product = next(
            (item for item in data if item['id'] == product_id), None)
        if not product:
            return render_template(
                'product_display.html', error="Product not found")
        data = [product]

    # Rend le template avec les produits
    return render_template('product_display.html', products=data)


if __name__ == '__main__':
    # Lance l'application Flask en mode debug sur le port 5000
    app.run(debug=True, port=5000)
