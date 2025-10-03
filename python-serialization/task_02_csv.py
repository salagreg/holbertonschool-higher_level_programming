#!/usr/bin/python3
"""Module qui lit un fichier CSV et le convertit en fichier JSON"""


import csv
import json


def convert_csv_to_json(csv_filename):
    """Lit un fichier CSV et le convertit en fichier JSON"""
    try:
        with open(csv_filename, mode='r', encoding='utf-8') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            data = list(csv_reader)

        with open("data.json", mode='w', encoding='utf-8') as json_file:
            json.dump(data, json_file, indent=4)
        return True

    except FileNotFoundError:
        return False
