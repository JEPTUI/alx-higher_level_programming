#!/usr/bin/python3
def weight_average(my_list=[]):
    if not isinstance(my_list, list) or len(my_list) == 0:
        return (0)
    total = 0
    frequency = 0
    for tup in my_list:
        total += (tup[0] * tup[1])
        frequency += tup[1]
        return (total / frequency)
