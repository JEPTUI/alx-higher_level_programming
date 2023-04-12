#!/usr/bin/python3
""" Module - 4-from_json_string
Defines a function that returns an object represented by a JSON string
"""


def from_json_string(my_str):
    """
    Returns an object represented by a JSON string
    """
    import json

    return json.loads(my_str)
