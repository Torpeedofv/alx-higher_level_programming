#!/usr/bin/python3
"""
takes a github username and password and uses the github API to display the id
"""


import requests
import sys
param = {'username': sys.argv[1], 'password': sys.argv[2]}

