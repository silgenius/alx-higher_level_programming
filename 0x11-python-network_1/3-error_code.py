#!/usr/bin/python3

"""
 a Python script that takes in a URL, sends a request to the URL and displays
 the body of the response (decoded in utf-8)
"""

from urllib import error
from urllib import request
import sys


def main():
    req = request.Request(sys.argv[1])
    try:
        with request.urlopen(req) as response:
            content = response.read().decode('utf-8')
    except error.HTTPError as e:
        print(f'Error code: {e.code}')
    else:
        print(content)


if __name__ == "__main__":
    main()
