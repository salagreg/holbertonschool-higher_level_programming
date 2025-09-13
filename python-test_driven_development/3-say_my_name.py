#!/usr/bin/python3
"""
Ce module fournit une fonction permettant d'afficher un nom complet
au format : "My name is <first name> <last name>".
"""


def say_my_name(first_name, last_name=""):
    """
    Affiche le nom complet sous la forme :
            "My name is <first name> <last name>".

    Paramètres :
        first_name (str) : Le prénom de la personne.
                              Doit être une chaîne de caractères.
        last_name (str, optionnel) : Le nom de famille de la personne.
                              Par défaut : chaîne vide.

    Exceptions :
        TypeError :
              Si first_name ou last_name ne sont pas des chaînes de caractères.

    Affiche :
        Le nom complet formaté.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
