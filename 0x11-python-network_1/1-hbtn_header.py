#!/usr/bin/python3
"""
Response header value #0
"""

import urllib.request
import sys

if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        inf = response.inf()['X-Request-Id']
        print(inf)
