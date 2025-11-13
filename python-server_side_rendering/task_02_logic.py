#!/usr/bin/python3
""" Module qui crée une application Flask simple avec plusieurs routes"""


import json
from flask import Flask, render_template


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
