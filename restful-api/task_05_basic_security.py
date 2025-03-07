from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from werkzeug.security import generate_password_hash, check_password_hash

# Initialisation de Flask
app = Flask(__name__)

# Configurer la clé secrète pour JWT
app.config['SECRET_KEY'] = 'supersecretkey'

# Initialisation de l'authentification de base et JWT
auth = HTTPBasicAuth()
jwt = JWTManager(app)

# Dictionnaire des utilisateurs (en mémoire)
users = {
    "user1": {"username": "user1", "password": generate_password_hash("password"), "role": "user"},
    "admin1": {"username": "admin1", "password": generate_password_hash("password"), "role": "admin"}
}

# ---------------------------------------------------
# Authentification de base
# ---------------------------------------------------

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        return user

@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"


# ---------------------------------------------------
# Authentification par JWT
# ---------------------------------------------------

@app.route('/login', methods=['POST'])
def login():
    # Récupérer les données JSON envoyées dans la requête
    data = request.get_json()
    username = data.get('username')
    password = data.get('password')

    # Vérifier si l'utilisateur existe et que le mot de passe est correct
    user = users.get(username)
    if user and check_password_hash(user['password'], password):
        # Créer un token JWT pour l'utilisateur
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200

    return jsonify({"error": "Invalid credentials"}), 401

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

# ---------------------------------------------------
# Contrôle d'accès basé sur le rôle (admin uniquement)
# ---------------------------------------------------

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    # Vérifier le rôle de l'utilisateur à partir du JWT
    current_user = get_jwt_identity()
    user = users.get(current_user)

    if user and user['role'] == 'admin':
        return "Admin Access: Granted"
    
    return jsonify({"error": "Admin access required"}), 403

# ---------------------------------------------------
# Gestion des erreurs JWT
# ---------------------------------------------------

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

# Démarrer l'application
if __name__ == '__main__':
    app.run(debug=True)
