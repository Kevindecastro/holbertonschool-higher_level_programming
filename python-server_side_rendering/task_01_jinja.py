from flask import Flask, render_template

# Initialisation de l'application Flask
app = Flask(__name__)


@app.route('/')
def home():
    """
    Route pour la page d'accueil.
    Rend le template 'index.html'.
    """
    return render_template('index.html')


@app.route('/about')
def about():
    """
    Route pour la page "À propos".
    Rend le template 'about.html'.
    """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """
    Route pour la page "Contact".
    Rend le template 'contact.html'.
    """
    return render_template('contact.html')


if __name__ == '__main__':
    # Lance l'application Flask en mode debug sur le port 5000
    app.run(debug=True, port=5000)
