#!/usr/bin/python3
""" Github commits code challenge"""

if __name__ == '__main__':
    import sys
    import requests

    url = 'https://api.github.com/repos/{}/{}/commits'.format(
        sys.argv[2], sys.argv[1])
    try:
        res = requests.get(url)
        resp_dict = res.json()
        for a in range(0, 10):
            print("{}: {}".format(resp_dict[i].get('sha'), resp_dict[i].get(
                'commit').get('author').get('name')))
    except Exception:
        pass
