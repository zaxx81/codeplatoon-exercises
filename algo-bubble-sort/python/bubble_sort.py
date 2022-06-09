bubble_sort_results = []
new_bubble_sort_results = []

def bubble_sort(arr):
  result = arr[:]
  swaps = 0
  last_index = len(result)
  prev = 0
  cur = 1

  while (cur < last_index):
    if result[cur] < result[prev]:
      temp = result[cur]
      result[cur] = result[prev]
      result[prev] = temp
      swaps += 1
      prev = 0
      cur = 1
    else:
      prev += 1
      cur += 1

  print(f"Final result: {result}")
  print(f"Swaps: {swaps}")
  bubble_sort_results.append(swaps)

  return result

def new_bubble_sort(arr):
  result = arr[:]
  swaps = 0
  last_index = len(result) - 1
  pass_swap = False
  
  for index in range(last_index):
    for elem in range(0, last_index - index):
      if result[elem] > result[elem + 1]:
        pass_swap = True
        swaps += 1
        result[elem], result[elem + 1] = result[elem + 1], result[elem]
    if not pass_swap:
      return
  
  print(f"Final result: {result}")
  print(f"Swaps: {swaps}")
  new_bubble_sort_results.append(swaps)

  return result
    

# Test Cases
print('=== bubble_sort() ===')
print(bubble_sort([4, 3, 5, 0, 1]) == [0, 1, 3, 4, 5])
print(bubble_sort([1, 3, 5, 9, 4, 6, 2, 0, 8, 7]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(bubble_sort([227, 605, 201, 653, 592, 545, 663, 316, 732, 849, 206, 580, 961, 253, 810, 536, 481, 325, 626, 384]) == [201, 206, 227, 253, 316, 325, 384, 481, 536, 545, 580, 592, 605, 626, 653, 663, 732, 810, 849, 961])

print('=== new_bubble_sort() ===')
print(new_bubble_sort([4, 3, 5, 0, 1]) == [0, 1, 3, 4, 5])
print(new_bubble_sort([1, 3, 5, 9, 4, 6, 2, 0, 8, 7]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(new_bubble_sort([227, 605, 201, 653, 592, 545, 663, 316, 732, 849, 206, 580, 961, 253, 810, 536, 481, 325, 626, 384]) == [201, 206, 227, 253, 316, 325, 384, 481, 536, 545, 580, 592, 605, 626, 653, 663, 732, 810, 849, 961])

print(f'bubble_sort() # of swaps {bubble_sort_results}')
print(f'new_bubble_sort() # of swaps {new_bubble_sort_results}')