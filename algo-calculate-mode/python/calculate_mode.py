def calculate_mode(input_list):
    results = []
    keysCount = []
    keys = list(set(input_list))

    for key in keys:
        count = input_list.count(key)
        keysCount.append([key, count])

    keysCount.sort(key=lambda x:(-x[1]))
    higest_count = keysCount[0][1]

    for item in keysCount:
        if item[1] == higest_count:
            results.append(item[0])
    
    return results
