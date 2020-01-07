#!/bin/bash
# Write a Bash script that takes in a URL as an argument, sends a GET request.

curl -H "X-HolbertonSchool-User-Id: 98" -sX GET $1
