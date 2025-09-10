#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # Supprimer une clé dans un dictionnaire
    if key in a_dictionary:
        del a_dictionary[key]
    return a_dictionary
