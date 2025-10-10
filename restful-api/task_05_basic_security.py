#!/usr/bin/python3
"""Module qui utilise deux systèmes d’authentification :
    - Authentification basique (Basic Auth) avec Flask-HTTPAuth.
    - Authentification par jeton JWT avec Flask-JWT-Extended."""


from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt


app = Flask(__name__)
auth = HTTPBasicAuth()
app.config["JWT_SECRET_KEY"] = "c2Z_q54EbJqX3YX_gnFEHBq23i9-UPCkL2d0dibFvPM"
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@auth.verify_password
def verify_password(username, password):
    """Vérifie les identifiants de l’utilisateur
          pour l’authentification basique."""
    if (
        username in users
        and check_password_hash(users[username]["password"], password)
    ):
        return True
    else:
        return False


@auth.error_handler
def unauthorized_error():
    """Gère le cas d’accès non autorisé pour l’authentification basique."""
    return jsonify({"error": "Unauthorized access"}), 401


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Route protégée par authentification basique."""

    return "Basic Auth: Access Granted"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """Gère le cas où aucun jeton JWT n’est fourni ou qu’il est invalide"""
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """Gère le cas où le jeton JWT fourni est mal formé ou invalide"""
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """Gère le cas où le jeton JWT a expiré"""
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """Gère le cas où le jeton JWT a été révoqué"""
    return jsonify({"error": "Token has been revoked"}), 401


@app.route('/login', methods=["POST"])
def login_jwt():
    """Authentifie un utilisateur et génère un jeton JWT."""

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"error": "Utilisateur introuvable"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"error": "Mot de passe invalide"}), 401

    access_token = create_access_token(
        identity=username,
        additional_claims={"role": users[username]["role"]})

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def protected_jwt():
    """Route protégée par un jeton JWT."""
    return "JWT Auth: Access Granted"


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin():
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 401

    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run(debug=True)
