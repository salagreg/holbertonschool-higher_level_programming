#!/usr/bin/python3
""" Module qui crée une application Flask simple avec plusieurs routes"""


import json
import csv
from flask import Flask, render_template, request, jsonify


app = Flask(__name__)


@app.route('/')
def home():
    """ Récupère et affiche la page d'accueil. """
    return render_template('index.html')


@app.route('/about')
def about():
    """ Récupère et affiche la page 'À propos'. """
    return render_template('about.html')


@app.route('/contact')
def contact():
    """ Récupère et affiche la page de contact. """
    return render_template('contact.html')


@app.route('/items')
def items():
    """ Récupère les items depuis un fichier JSON et les affiche. """
    try:
        with open('items.json', 'r') as file:
            data = json.load(file)
            items = data.get("items", [])
    except FileNotFoundError:
        items = []

    return render_template('items.html', items=items)


@app.route('/products')
def products():
    """Récupère les produits depuis un fichier JSON ou CSV
            selon le paramètre 'source'."""
    source = request.args.get("source")

    if source == "json":
        try:
            with open("products.json", "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            return "JSON file not found", 404

    elif source == "csv":
        data = []
        try:
            with open("products.csv", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    data.append(row)
        except FileNotFoundError:
            return "CSV file not found", 404

    else:
        return "Wrong source", 400

    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
