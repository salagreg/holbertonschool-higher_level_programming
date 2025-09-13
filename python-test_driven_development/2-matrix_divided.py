#!/usr/bin/python3
"""
Ce module fournit une fonction permettant de diviser tous les éléments
d'une matrice par un nombre donné.

La fonction vérifie que la matrice est correctement formée et que le
diviseur est un nombre valide, puis retourne une nouvelle matrice
avec les valeurs divisées et arrondies à 2 décimales.
"""


def matrix_divided(matrix, div):
    """
    Divise tous les éléments d'une matrice par un diviseur donné.

    Paramètres :
        matrix (list de list):
        Une matrice (liste de listes) d'entiers ou de flottants.
        Toutes les lignes doivent avoir la même taille.

        div (int ou float):
        Le nombre par lequel chaque élément de la matrice sera divisé.

    Exceptions :
        TypeError :
            - Si matrix n'est pas une liste de listes de nombres (int ou float)
            - Si toutes les lignes de matrix ne sont pas de la même taille
            - Si div n'est pas un nombre (int ou float)
        ZeroDivisionError :
            - Si div est égal à 0

    Retour :
        list de list : Une nouvelle matrice avec les valeurs divisées par div
        et arrondies à 2 chiffres après la virgule.
    """
    if not isinstance(matrix, list) or not all(
        isinstance(row, list) for row in matrix
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    if not all(
        isinstance(num, (int, float)) for row in matrix for num in row
    ):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
        )

    row_length = len(matrix[0])
    if not all(len(row) == row_length for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    return [
        [round(num / div, 2) for num in row]
        for row in matrix
    ]
