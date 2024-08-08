#!/usr/bin/python3

"""
 a Python script that takes in a URL and an email address, sends a POST request
 to the passed URL with the email as a parameter, and finally displays the body
 of the response.
"""

import requests
import sys


def main():
    data = {'email': sys.argv[2]}
    req = requests.post(sys.argv[1], data)
    print(req.text)


if __name__ == "__main__":
    main()
