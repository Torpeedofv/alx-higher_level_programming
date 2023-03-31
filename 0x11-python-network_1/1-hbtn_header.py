#!/usr/bin/python3
"""takes in a url sends a request to the url and displays
the value of the X-Request_Id variable found in the header
of the response"""


import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as body:
    print(body.info()['X-Request-Id'])
