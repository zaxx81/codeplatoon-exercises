import re

def char_count(input_str):
  results = []
  charsList = re.findall('[a-z]', str(input_str).lower())
  charsSet = set(charsList)

  for char in charsSet:
    count = charsList.count(char)
    results.append([char, count])
  
  return sorted(results, key=lambda x:(-x[1], x[0]))
