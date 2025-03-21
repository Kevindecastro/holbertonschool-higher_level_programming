import json
from flask import Flask, render_template

# Initialisation de l'application Flask
app = Flask(__name__)


@app.route('/items')
def items():
    """
    Route pour afficher une liste d'items.
    Lit les données depuis un fichier JSON et les passe au template 'items.html'.
    """
    # Ouvre et lit le fichier JSON
    with open('data/items.json', 'r') as file:
        data = json.load(file)
    # Rend le template avec les items
    return render_template('items.html', items=data.get('items', []))


if __name__ == '__main__':
    # Lance l'application Flask en mode debug sur le port 5000
    app.run(debug=True, port=5000)
