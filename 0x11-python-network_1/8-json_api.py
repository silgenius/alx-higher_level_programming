#!/usr/bin/python3

"""
 a Python script that takes in a letter and sends a POST request to
 http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

import sys
import requests


def main():
    if len(sys.argv) < 2:
        value = {'q': ""}
    else:
        value = {'q': sys.argv[1]}
    req = requests.post('http://0.0.0.0:5000/search_user', value)
    try:
        data = req.json()
        if data:
            print(f"[{data['id']}] {data['name']}")
        else:
            print("No result")
    except ValueError:
            print("Not a valid JSON")


if __name__ == "__main__":
    main()
