#!/usr/bin/python3
"""Module qui traite les donnees d'une API"""


import requests
import csv


def fetch_and_print_posts():
    """Récupère et affiche les titres des posts depuis JSONPlaceholder"""
    r = requests.get("https://jsonplaceholder.typicode.com/posts")
    if r.status_code == 200:
        print("Status Code:", r.status_code)
    else:
        return None
    posts = r.json()
    for i in posts:
        print(i["title"])


def fetch_and_save_posts():
    """Récupère les posts et les enregistre dans un fichier CSV"""
    res = requests.get("https://jsonplaceholder.typicode.com/posts")
    if res.status_code == 200:
        print("Status Code:", res.status_code)
    else:
        return None
    posts = res.json()
    with open("posts.csv", "w", encoding="utf-8", newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
        writer.writeheader()
        for post in posts:
            writer.writerow({
                'id': post['id'],
                'title': post['title'],
                'body': post['body']})
