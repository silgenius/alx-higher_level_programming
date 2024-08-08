#!/usr/bin/python3

"""
a Python script that takes your GitHub credentials
(username and password) and uses the GitHub API to
display your id
"""

import sys
import requests
from requests.auth import HTTPBasicAuth


def get_github_user_id(username, token):
    url = "https://api.github.com/user"
    response = requests.get(url, auth=HTTPBasicAuth(username, token))

    user_data = response.json()

    print(user_data.get('id'))


if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    get_github_user_id(username, token)
