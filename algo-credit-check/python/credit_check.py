import functools
from re import M
import itertools
import re

def credit_check(str):
    int_list = re.findall('[0-9]', int(str))
    
    # str_list = list(str)
    # map_object = reversed(list(map(int, str_list)))
    # int_list = list(map_object)
    
    for i, item in enumerate(int_list):
        if (i % 2 == 1):
            int_list[i] *= 2
            if int_list[i] > 9:
                int_list[i] -= 9

    int_list.reverse()
    results = functools.reduce(lambda agg, item : agg + item, int_list)
    if results % 10 == 0:
        return "The number is valid!"
    else:
        return "The number is invalid!"
