#!/usr/bin/python3
""" Module - 100-append_after
Defines a function that inserts a line of text to a file,
after each line containing a specific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    inserts a line of text to a file,
    after each line containing a specific string
    Args:
        filename(str) - name of the file
        search_string - string to search within the file
        new_string - string to insert
    """
    with open(filename, 'r+', encoding="utf-8") as f:
        text = ""
        for line in f:
            text += line
            if search_string in line:
                text += new_string
        f.seek(0)
        f.write(text)
