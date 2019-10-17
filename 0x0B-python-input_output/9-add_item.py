#!/usr/bin/python3
import json
import sys
save_to_json_file = __import__('7-save_to_json_file').save_to_json_file
load_from_json_file = __import__('8-load_from_json_file').load_from_json_file
args = sys.argv
try:
    list = list(load_from_json_file("add_item.json"))
except:
    list = list()
for arg in args[1:]:
    list.append(arg)

save_to_json_file(list, "add_item.json")
