# Big O Answers

## Snippet 1 - 
### Big O: O(N): Linear Time
### Explanation:
```python
def largest(array, value):
  for item in array: # ...factor of N
    if item > value:
      return False
  return True 
```


## Snippet 2 -
### Big O: O(N): Linear Time
### Explanation:

```python
def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: # ...factor of N
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: # ...factor of N 
    print(customer['country'])
  
```

## Snippet 3 -
### Big O: O(1): Constant Time
### Explanation:

```python
def first_element_is_red(array):
  return array[0] == 'red' # ...factor of 1
```

## Snippet 4 -
### Big O: O(N^2): Quadratic Time
### Explanation:

```python
def duplicates(array):
  for index1, item1 in enumerate(array): # ...factor of N
    for index2, item2 in enumerate(array): # ...factor of N
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
``` 

## Snippet 5 -
### Big O: O(N * M): Quadratic Time
### Explanation:

```python
words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words: # ...factor of N
  for ending in endings: # ...factor of M
    print(word + ending)

```

## Snippet 6 -
### Big O: O(N): Linear Time
### Explanation:

```python
numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array: # ...factor of N
    print(item)

```

## Snippet 7 -
### Big O: O(N^2): Quadratic Time
### Explanation:

```python
# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): # ...factor of N
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : # ...factor of N
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 
```

## Snippet 8 -
### Big O: O(N^2): Quadratic Time
### Explanation:

```python
for i in range(len(my_list)): # ...factor of N
  min_idx = i
  for j in range(i+1, len(my_list)): # ...factor of N
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
```
