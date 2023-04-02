#!/usr/bin/python3
"""takes to argument: repository name, owner name to list 10 commits
of a repo using github api
"""


import requests
import sys
if __name__ == "__main__":
    url = f"https://api.github.com/repos/{sys.argv[2]}/{sys.argv[1]}/commits"
    r = requests.get(url)
    commits = r.json()
    i = 0
    while i < 10:
        print(f"{commits[i].get('sha')}: {commits[i].get('commit')\
                .get('author').get('name')}")
        i += 1
