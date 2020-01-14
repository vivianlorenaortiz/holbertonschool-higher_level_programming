#!/usr/bin/python3
"""
script that takes in a URL and an email address, sends a POST request.
"""
import requests
import sys
if __name__ == "__main__":
    try:
        payload = {'q': sys.argv[1]}
        r = requests.post('http://0.0.0.0:5000/search_user', payload)
    except:
        r = requests.post('http://0.0.0.0:5000/search_user')
    try:
        print("[{}] {}".format(r.json()["id"], r.json()["name"]))
    except:
        if not r.json():
            print("No result")
