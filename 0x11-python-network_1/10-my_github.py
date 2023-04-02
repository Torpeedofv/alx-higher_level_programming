#!/usr/bin/python3
"""
takes a github username and password and uses the github API to display the id
"""


import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    r = requests.get('https://api.github.com/user', auth=(username, password))
    response = r.json()
    print(response.get('id'))
