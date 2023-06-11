#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    j = 0
    from i in range(-1:len(my_list)/2):
        res = my_list[i]
        my_list[i] = my_list[j]
        my_list[j] = res
        j++
