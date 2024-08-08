#!/usr/bin/python3

"""
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Parameters:
    - text (str): The input text.

    Raises:
    TypeError: If text is not a string.
"""
def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?', and ':' character.

    Parameters:
    - text (str): The input text.

    Raises:
    TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    characters = ['.', '?', ':']

    formatted_text = ""
    sentence = ""
    for i, char in enumerate(text):
        formatted_text += char

        if char in characters and i < len(text) - 1:
            formatted_text += '\n\n'

    for line in formatted_text.split('\n'):
        print(line.strip())
