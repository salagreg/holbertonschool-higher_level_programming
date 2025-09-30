#!/usr/bin/python3
"""Module that reads a text file and displays it on standard output"""


def read_file(filename=""):
    """Reads a text file and displays it on standard output"""
    with open(filename, 'r', encoding="UTF-8") as f:
        new_contener = f.read()
        print("{}".format(new_contener), end="")
