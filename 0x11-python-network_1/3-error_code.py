#!/usr/bin/python3
"""Takes in a url, sends a request to the url and displays the body
of the response"""


import urllib.request
import urllib.parse
import sys
if __name__ == "__main__":
    try:
        with urllib.request.urlopen(sys.argv[1]) as body:
            print(body.read().decode('utf-8'))
    except urllib.error.HTTPError as e:
        print(f"Error code: {e.code}")
