import functools

def find_armstrong_numbers(numbers):
  results = []

  for x in numbers:
    strArr = list(str(x))
    intArr = list(map(int, strArr))
    power = len(intArr)
    
    intPowArr = map(lambda item : pow(item, power), intArr)
    sums = functools.reduce(lambda agg, item : agg + item, intPowArr)

    if sums == x:
      results.append(x)
  
  return results