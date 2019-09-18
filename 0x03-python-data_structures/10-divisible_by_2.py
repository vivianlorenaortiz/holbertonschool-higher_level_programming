#!/usr/bin/Python3
def divisible_by_2(my_list=[]):

    list_div2 = [i % 2 == 0 for i in my_list]

    return list_div2
