#!/usr/bin/python3
"""Take a URL, sends requests ans analyzes HTTP status code"""


import requests
from sys import argv

if __name__ == "__main__":
    try:
        resp = requests.get(argv[1])
        error = resp.raise_for_status()
        if not error:
            print(resp.text)
    except requests.exceptions.HTTPError as err:
        if resp.status_code >= 400:
            print(f'Error code: {resp.status_code}')
