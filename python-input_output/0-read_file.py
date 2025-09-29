#!/usr/bin/python3
"""Module that reads a text file and displays it on standard output"""


def read_file(filename=""):
    """Reads a text file and displays it on standard output"""
    with open(filename, 'r') as outfile:
        print(outfile.read())
