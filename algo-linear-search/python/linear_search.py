array_to_search_through = []
for number in range(1, 1001):
    array_to_search_through.append(number)

def linear_search(value_to_find, array_to_search_through):
    for idx, elem in enumerate(array_to_search_through):
        if value_to_find == elem:
            return idx

def global_linear_search(value_to_find, array_to_search_through):
    result = []

    for idx, elem in enumerate(array_to_search_through):
        if value_to_find == elem:
            result.append(idx)
    
    return result