#!/usr/bin/python3
def uniq_add(my_list=[]):
    sum = 0
    my_unique = set(my_list)
    for num in my_unique:
        sum += num
    return sum
