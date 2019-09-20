#!/usr/python3
def roman_to_int(roman_string):
    if roman_string is None:
        return 0
     roman_string = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
     result = 0
     for i,c in enumerate(num):
        if (i+1) == len(num) or roman_string[c] > roman_string[num[i+1]]:
            result += roman_string[c]
        else:
            result -= roman_string[c]
    return result
