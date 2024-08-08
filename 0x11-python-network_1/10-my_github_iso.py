#!/usr/bin/python3

"""
 a Python script that takes your GitHub credentials (username and password)
 and uses the GitHub API to display your id
"""

import sys
import requests


def main():
    auth_key = sys.argv[1] + sys.argv[2]
    headers = {'Accept': 'application/vnd.github+json',
            'Authorization': f'token {auth_key}',
            'X-GitHub-Api-Version': '2022-11-28'}
    req = requests.get('https://api.github.com/user', headers=headers)
    print(req.headers.get('name'))


if __name__ == "__main__":
    main()
