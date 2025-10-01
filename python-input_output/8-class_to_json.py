#!/usr/bin/python3
""" Module that return the dictionary description with simple data structure """


def class_to_json(obj):
    """ Get the attributes of an object in dictionary form """
    return obj.__dict__
