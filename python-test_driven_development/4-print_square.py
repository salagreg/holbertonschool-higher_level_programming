#!/usr/bin/python3
"""
Ce module contient une fonction qui imprime un carré
de taille donnée avec le caractère #.
"""


def print_square(size):
    """
    Affiche un carré de taille size avec le caractère #

    Paramètre :
        size (int) : la taille du carré à afficher (entier ≥ 0)

    Exceptions :
        TypeError : si size n'est pas un entier
        ValueError : si size est négatif
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
