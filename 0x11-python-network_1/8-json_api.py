#!/usr/bin/python3
"""takes in a letter and sends a Post request to a URL with the letter as a parameter
"""


import requests
import sys
if __name__ == "__main__":
    if len(sys.argv) == 1:
        payload = {'q': ""} 
    else:
        payload = {'q': sys.argv[1]}
    new_param = payload
    r = requests.post('http://0.0.0.0:5000/search_user', data=new_param)
    response = r.json()
    if type(response) == dict:
        if len(response) == 0:
            print("No result")
        else:
            print(f"[{response.get('id')}] {response.get('name')}")
    else:
        print("Not a valid JSON")
