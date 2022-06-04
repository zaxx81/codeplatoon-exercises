import re

def palindrome(word):
    # Write code here
    str_arr = re.findall("[a-z0-9]", str(word).lower())
    
    mid = int(len(str_arr) / 2)

    if len(str_arr) % 2 == 1:
        str_arr.pop(mid)
    
    compare_arr1 = str_arr[:mid]
    compare_arr2 = str_arr[mid:]
    compare_arr2.reverse()

    return compare_arr1 == compare_arr2
