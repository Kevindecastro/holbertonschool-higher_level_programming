from flask import Flask, jsonify, request

app = Flask(__name__)

# Dictionnaire pour stocker les utilisateurs
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Point de terminaison racine
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Point de terminaison pour obtenir les utilisateurs
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# Point de terminaison pour vérifier l'état
@app.route('/status')
def status():
    return "OK"

# Point de terminaison pour obtenir un utilisateur spécifique
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Point de terminaison pour ajouter un utilisateur
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()

    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data['username']
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get('name', ''),
        "age": data.get('age', ''),
        "city": data.get('city', '')
    }

    return jsonify({
        "message": "User added",
        "user": users[username]
    }), 201

# Démarrage de l'application
if __name__ == "__main__":
    app.run(debug=True)
