#!/usr/bin/python3
"""
takes repository name as first arg and owner name as second to print commits
"""


import sys
import requests

if __name__ == "__main__":
    url = "https://api.github.com/repos/{}/{}/commits".format(
        sys.argv[2], sys.argv[1])
    re = requests.get(url)
    commits = re.json()

    for commit in commits[0:10]:
        print(commit.get('sha'), end=': ')
        print(commit.get('commit').get('author').get('name'))
