#!/usr/bin/python3
""" Module that adds a string to the end of the file
    and returns the number of characters added """


def append_write(filename="", text=""):
    """Add a string at the end"""
    with open(filename, 'a', encoding="UTF-8") as f:
        return f.write(text)
