#!/usr/bin/python3

"""
a Python script that takes in a URL, sends a request to the URL and displays
the value of the variable X-Request-Id in the response header
"""

import requests
import sys


def main():
    req = requests.get(sys.argv[1])
    header = req.headers.get('X-Request-Id')
    print(header)


if __name__ == "__main__":
    main()
