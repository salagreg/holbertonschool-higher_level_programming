#!/usr/bin/python3
""" Module qui crée une application Flask simple avec plusieurs routes"""


import json
import csv
import sqlite3
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

    source = request.args.get("source")
    product_id = request.args.get("id")
    products_list = []
    error_message = None

    # Récupère les produits depuis un fichier JSON et les affiche.
    if source == "json":
        try:
            with open("products.json", "r") as file:
                products_list = json.load(file)
        except FileNotFoundError:
            error_message = "JSON file not found"

    # Récupère les produits depuis un fichier CSV et les affiche.
    elif source == "csv":
        try:
            with open("products.csv", newline="", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    row["id"] = int(row["id"])
                    row["price"] = float(row["price"])
                    products_list.append(row)
        except FileNotFoundError:
            error_message = "CSV file not found"

    elif source == "sql":
        try:
            conn = sqlite3.connect("products.db")
            cursor = conn.cursor()
            cursor.execute("SELECT id, name, category, price FROM Products")
        
            rows = cursor.fetchall()
            conn.close()

            # On transforme les tuples SQLite → dictionnaires
            for r in rows:
                products_list.append({
                    "id": r[0],
                    "name": r[1],
                    "category": r[2],
                    "price": r[3]
                })

        except sqlite3.Error:
            error_message = "Database error"


    # Gestion des erreurs pour une source invalide.
    else:
        error_message = "Wrong source"
        return render_template(
            "product_display.html",
            products=None,
            error=error_message
        )


    # Filtre les produits par ID si un ID est fourni.
    if product_id:
        try:
            product_id = int(product_id)
            filtered = [p for p in products_list if p["id"] == product_id]
            if filtered:
                products_list = filtered
            else:
                error_message = "Product not found"
                products_list = None
        except ValueError:
            error_message = "Invalid ID format"
            products_list = None

    return render_template(
        "product_display.html",
        products=products_list,
        error=error_message
    )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
