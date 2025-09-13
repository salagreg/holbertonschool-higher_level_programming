#!/usr/bin/python3
"""
Ce module fournit une fonction qui permet d'ajouter deux entiers.

Si les valeurs fournies sont des flottants, elles seront d'abord converties
en entiers avant l'addition.
Si l'une des valeurs n'est pas un entier ou un flottant,
une exception sera levée.
"""


def add_integer(a, b=98):
    """
    Additionne deux entiers ou flottants après les avoir convertis en entiers.

    Paramètres :
        a (int ou float) :
              Le premier nombre à additionner.
        b (int ou float, optionnel) :
              Le second nombre à additionner (par défaut : 98).

    Exceptions :
        TypeError : Si a ou b n'est ni un entier ni un flottant.

    Retour :
        int : La somme des deux nombres, après conversion en entiers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
