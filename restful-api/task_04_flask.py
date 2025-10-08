#!/usr/bin/python3
"""Module qui crée une API simple avec Flask"""


from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def home():
    """Affiche un message d'accueil"""
    return "Welcome to the Flask API!"


users = {}


@app.route("/data")
def new_jsonify():
    """Retourne une liste de tout les noms d'utilisateurs"""
    username = list(users.keys())
    return jsonify(username)


@app.route("/status")
def new_status():
    """Vérifie que l'API fonctionne"""
    return "OK"


@app.route("/users/<username>")
def new_users(username):
    """Retourne les données de l'utilisateur demandé si présent,
        sinon retourne une erreur """
    if username in users:
        return jsonify(users[username])
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Reçoit des données JSON, ajoute un nouvel utilisateur
        dans un dictionnaire, retourne un message de confirmation"""
    data = request.get_json()

    if "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run()
