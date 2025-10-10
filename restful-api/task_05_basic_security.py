#!/usr/bin/python3
"""Module qui utilise deux systèmes d’authentification :
    - Authentification basique (Basic Auth) avec Flask-HTTPAuth.
    - Authentification par jeton JWT avec Flask-JWT-Extended."""


from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, create_access_token
from flask_jwt_extended import jwt_required, get_jwt_identity


app = Flask(__name__)
auth = HTTPBasicAuth()


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


@app.route('/basic-protected', methods=['GET'])
@auth.login_required
def basic_protected():
    """Route protégée par authentification basique."""

    return jsonify({"message": "Basic Auth: Access Granted"}), 200


app.config["JWT_SECRET_KEY"] = "c2Z_q54EbJqX3YX_gnFEHBq23i9-UPCkL2d0dibFvPM"
jwt = JWTManager(app)


@app.route('/login', methods=["POST"])
def login_jwt():
    """Authentifie un utilisateur et génère un jeton JWT."""

    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    if username not in users:
        return jsonify({"Erreur": "Utilisateur introuvable"}), 401

    if not check_password_hash(users[username]["password"], password):
        return jsonify({"Erreur": "Mot de passe invalide"}), 401

    access_token = create_access_token(
        identity={
            "username": username,
            "role": users[username]["role"]
        }
    )

    return jsonify({"access_token": access_token}), 200


@app.route('/jwt-protected', methods=["GET"])
@jwt_required()
def protected_jwt():
    """Route protégée par un jeton JWT."""

    identity = get_jwt_identity()
    username = identity["username"]
    return jsonify({"msg": f"JWT Auth: Access Granted for {username}"}), 200


@app.route('/admin-only', methods=["GET"])
@jwt_required()
def admin():
    """Route réservée uniquement aux administrateurs."""

    identity = get_jwt_identity()
    if identity["role"] != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return jsonify({"message": "Admin Access: Granted"}), 200


if __name__ == "__main__":
    app.run(debug=True)
