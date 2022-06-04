def to_roman(num):
    # write your code here!
    result = ""
    rom_arb_map = {
        "M": 1000,
        "CM": 900,
        "D": 500,
        "CD": 400,
        "C": 100,
        "XC": 90,
        "L": 50,
        "XL": 40,
        "X": 10,
        "IX": 9,
        "V": 5,
        "IV": 4,
        "I": 1
    }
    
    for key in rom_arb_map:
        div_num_times = num / rom_arb_map[key]
        if div_num_times >= 1:
           result += key * int(div_num_times)
           num -= rom_arb_map[key] * int(div_num_times)
    return result