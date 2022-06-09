def balance_parens(input_str):
    result = list(input_str)

    result = match_pairs(result[:], '(', ')')
    result.reverse()
    
    result = match_pairs(result[:], ')', '(')
    result.reverse()

    result = ''.join(result)

    print(result)
    return result

# match_pairs function
def match_pairs(input_list, open_char, close_char):
    result = []
    match_count = 0

    for char in input_list:
        if char == open_char:
            result.append(char)
            match_count += 1
        if char == close_char:
            if match_count > 0:
                result.append(char)
                match_count -= 1
        if (char != open_char) and (char != close_char):
            result.append(char)
    
    return result
