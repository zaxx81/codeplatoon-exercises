from algos.bottle_song import bottle_song
from algos.roman_numerals import to_roman
#   algo-roman-numerals, algo-factorial, algo-fibonacci, algo-linear-search, algo-armstrong-numbers, algo-sum-pairs, algo-anagrams-i, algo-anagrams-ii, algo-character-count, algo-palindromes, algo-calculate-mode, algo-pad-an-array, algo-balanced-parentheses

# Week 2 Challenges
#   oop-app-users-i, oop-guessing-game, csv-reader, oop-app-users-ii, oop-contact-list, algo-caesar-cipher, oop-app-users-iii, oop-school-interface-i, oop-boggle-i, oop-school-interface-ii, oop-budget, oop-bowling

# Reporting
import time
import random
import statistics

functions = bottle_song, to_roman(1981)

# this is just a one line way to make this: {'iterate_a_lot': [], 'iterate_a_little': []}
times = {f.__name__: [] for f in functions}

for func in functions:
  for i in range(500):  # adjust accordingly so whole thing takes a few sec
    t0 = time.time()
    func()
    t1 = time.time()
    times[func.__name__].append((t1 - t0) * 1000)



for name, numbers in times.items():
  print('FUNCTION:', name, 'Used', len(numbers), 'times')
  print('\tMEDIAN', statistics.median(numbers))
  print('\tMEAN  ', statistics.mean(numbers))
  print('\tSTDEV ', statistics.stdev(numbers))
