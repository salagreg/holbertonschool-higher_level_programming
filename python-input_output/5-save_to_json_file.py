#!/usr/bin/python3
""" Module that writes an object to a text file, in JSON representation """
import json


def save_to_json_file(my_obj, filename):
    """ Write an object to a text file """
    with open(filename, 'w') as filename:
        json.dump(my_obj, filename)
