#!/usr/bin/python3
""" Module de sérialisation et déserialisation JSON simple """


import json


def serialize_and_save_to_file(data, filename):
    """ Sérialise des données Python au format JSON
        et les enregistre dans un fichier texte """
    with open(filename, 'w', encoding="utf-8") as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    """ Charge un fichier JSON et désérialise son contenu en objet Python """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
