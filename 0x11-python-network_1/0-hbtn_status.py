#!/usr/bin/python3

"""
 a Python script that fetches https://alx-intranet.hbtn.io/status
"""


def main():
    from urllib import request

    with request.urlopen('https://alx-intranet.hbtn.io/status') as response:
        content = response.read()

    print("Body response:")
    print(f'\t- type: {type(content)}')
    print(f'\t- content: {content}')
    print(f'\t- utf8 content: {content.decode("utf-8")}')


if __name__ == "__main__":
    main()
