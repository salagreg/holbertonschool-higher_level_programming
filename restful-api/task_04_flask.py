#!/usr/bin/python3
"""Module qui crée une API simple avec Flask"""


from flask import Flask
from flask import jsonify
from flask import request
app = Flask(__name__)


@app.route("/")
def home():
    """Affiche un message d'accueuil"""
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
        return "404 Not Found"


@app.route("/add_user", methods=["POST"])
def add_user():
    """Reçoit des données JSON, ajoute un nouvel utilisateur
        dans un dictionnaire, retourne un message de confirmation"""
    data = request.get_json()
    username = data["username"]
    users[username] = {
        "name": data["name"],
        "age": data["age"],
        "city": data["city"]
    }
    return jsonify({"message": "User added", "user": users[username]})


if __name__ == "__main__":
    app.run()
