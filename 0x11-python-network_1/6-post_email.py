#!/usr/bin/python3
"""Takes in a url and email address, sends a Post request to the url
with the email as a parameter and displays the body of the response
"""


import requests
import sys
if __name__ == "__main__":
    url = sys.argv[1]
    payload = {'email': sys.argv[2]}
    r = requests.post(url, params=payload)
    print(r.text)
