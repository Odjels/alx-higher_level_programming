#!/usr/bin/python3
"""
Takes your Github credentials and uses the GitHub API
to dispaly your ID.
"""

if __name__ == '__main__':
    import sys
    import requests

    url = "https://api.github.com/user"
    resp = requests.get(
        url, auth=requests.auth.HTTPBasicAuth(sys.argv[1], sys.argv[2]))
    response_dict = resp.json()
    print(response_dict.get('id'))
