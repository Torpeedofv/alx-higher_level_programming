#!/usr/bin/python3
"""fetches a url and displaying the body of the
response in a specific format"""


import urllib.request
if __name__ == "__main__":
    with urllib.request.urlopen('https://alx-intranet.hbtn.io/status') as body:
        f_body = body.read()
        print('Body response:')
        print(f"\t- type: {type(f_body)}")
        print(f"\t- content: {f_body}")
        print(f"\t- utf8 content: {f_body.decode('utf-8')}")
