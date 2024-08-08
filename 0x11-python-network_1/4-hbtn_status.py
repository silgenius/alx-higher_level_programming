#!/usr/bin/python3

"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""

import requests


def main():
    req = requests.get('https://alx-intranet.hbtn.io/status')
    print('Body response:')
    print(f'\t- type: {type(req.text)}')
    print(f'\t- content: {req.text}')


if __name__ == "__main__":
    main()
