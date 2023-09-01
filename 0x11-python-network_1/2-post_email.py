#!/usr/bin/python3
"""
Python script that takes in a URL and an email, sends a POST
request to the passed URL with the email as a parameter, and
displays the body of the response (decoded in utf-8)
"""

import urllib.request
import urllib.parse
import sys

if __name__ == '__main__':
    mail_data = urllib.parse.urlencode({'email': sys.argv[2]}).encode('ascii')
    mail_req = urllib.request.Request(sys.argv[1], data)
    with urllib.request.urlopen(mail_req) as r:
        body = r.read()
        print('{}'.format(body.decode('utf-8')))
