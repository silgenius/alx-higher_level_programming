#!/usr/bin/python3

"""
 a Python script that takes in a URL, sends a request to the
 URL and displays the body of the response.
"""

import sys
import requests


def main():
    try:
        req = requests.get(sys.argv[1])
        req.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f'Error code: {e.response.status_code}')
    else:
        print(req.text)


if __name__ == "__main__":
    main()
