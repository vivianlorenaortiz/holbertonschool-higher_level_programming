#!/usr/bin/python3
"""
GITH
"""

import requests
from sys import argv

if __name__ == '__main__':
    user = argv[1]
    passw = argv[2]

    r = requests.get('https://api.github.com/user', auth=(user, passw))
    if r.status_code != 200:
        print("None")
    else:
        json_dict = r.json()
        print(json_dict['id'])
