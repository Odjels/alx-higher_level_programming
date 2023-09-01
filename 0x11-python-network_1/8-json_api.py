#!/usr/bin/python3
""" accessing json object """

import requests
from sys import argv

if __name__ == '__main__':
    url = "http://0.0.0.0:5000/search_user"
    data = {"q": argv[1][0] if len(argv) > 1 else ""}
    res = requests.post(url, data=data)
    try:
        body = res.json()
        if not body:
            print("No result")
        else:
            print("[{}] {}".format(body.get("id"), body.get("name")))
    except ValueError:
        print("Not a valid JSON")
