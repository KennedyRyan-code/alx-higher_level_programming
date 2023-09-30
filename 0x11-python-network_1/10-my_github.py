#!/usr/bin/python3
"""uses the GitHub API to display your id"""
import sys
import requests
from requests.auth import HTTPBasicAuth

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]

    response = requests.get('https://api.github.com/user',
                            auth=HTTPBasicAuth(username, token))

    if response.status_code == 200:
        print(response.json().get('id'))
    else:
        print("Error: {}".format(response.status_code))
