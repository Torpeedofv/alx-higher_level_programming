#!/usr/bin/python3
"""
takes a github username and password and uses the github API to display the id
"""


import requests
import sys
if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {'Authorization': f'Basic {username}:{password}'}
    r = requests.get('https://api.github.com/user', data=headers)
    response = r.json()
    print(response.get('id'))
