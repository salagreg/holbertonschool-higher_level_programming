#!/usr/bin/python3
""" Module CustomObject """


import pickle


class CustomObject():
    """
    Classe représentant un objet avec un nom, un âge et un statut étudiant.
    Fournit des méthodes pour affichage, sérialisation et désérialisation.
    """
    def __init__(self, name, age, is_student):
        """Initialise un objet CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Affiche les informations de l'objet dans un format lisible."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {'True' if self.is_student else 'False'}")

    def serialize(self, filename):
        """Sérialise l'objet courant dans un fichier binaire avec pickle"""
        with open(filename, "wb") as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """Désérialise un objet depuis un fichier binaire
          et retourne une instance de CustomObject."""
        with open(filename, "rb") as f:
            my_obj = pickle.load(f)
            return my_obj
