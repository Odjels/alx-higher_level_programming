#!/usr/bin/python3
""" script to fetch id from a requested url """


if __name__ == '__main__':
    from urllib import request
    from sys import argv

    url = argv[1]
    with request.urlopen(url) as response:
       url_request = response.getheader('X-Request-Id')
        print(url_request)
