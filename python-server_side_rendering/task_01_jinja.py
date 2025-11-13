#!/usr/bin/python3
""" Module qui crée une application Flask simple avec plusieurs routes"""


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


if __name__ == '__main__':
    app.run(debug=True, port=5000)
