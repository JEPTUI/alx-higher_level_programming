#!/usr/bin/python3
""" Module - 5-text_indentation
Defines function that prints a text
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    Args: text(string)
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    for char in ".?:":
        text = text.replace(char, char + "\n\n")
    printed_lines = [lines.strip(' ') for lines in text.split('\n')]
    output = "\n".join(printed_lines)
    print(output, end="")
