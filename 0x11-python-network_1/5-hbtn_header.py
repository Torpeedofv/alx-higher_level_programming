#!/usr/bin/python3
"""Takes in a url, sends a request to the url and displays a specified
variable"""


import sys
import requests
if __name__ == "__main__":
    r = requests.get(sys.argv[1])
    print(r.headers.get('X-Request-Id'))
