#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_values = set(my_list)
    _sum = 0
    for i in unique_values:
        _sum = _sum + i
    return _sum
