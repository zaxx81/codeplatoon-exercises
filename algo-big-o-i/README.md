# Big 0 Notation: 

## Release 0 : What is Big-O?


1. Read [Big-O notation explained by a self-taught programmer](https://justin.abrah.ms/computer-science/big-o-notation-explained.html)
2. Read [Big-O is easy to calculate, if you know how](https://justin.abrah.ms/computer-science/how-to-calculate-big-o.html)


## Release 1 : Determine the big O
Give the efficiency of each of the following code snippets. Try out the code snippets below and verify your answers. 

### Explanations
[Explanations](explanations.md)

### Problems for you

Snippet 1 - Big O:

```python
def largest(array, value):
  for item in array:
    if item > value:
      return False
  return True 
```

Snippet 2 - Big O:

```python
def info_dump(customers):
  
  print('Customer Names:')
  for customer in customers: 
    print(customer['name'])
  
  print('Customer Locations:')
  for customer in customers: 
    print(customer['country'])
  
```

Snippet 3 - Big O:
```python
def first_element_is_red(array):
  return array[0] == 'red' 
```

Snippet 4 - Big O:
```python
def duplicates(array):
  for index1, item1 in enumerate(array):
    for index2, item2 in enumerate(array):
      if index1 == index2:
        continue
      if item1 == item2:
        return True
  return False
```

Snippet 5 - Big O:
```python
words = ['chocolate', 'coconut', 'rainbow']
endings = ['cookie', 'pie', 'waffle']

for word in words:
  for ending in endings:
    print(word + ending)

```

Snippet 6 - Big O:
```python
numbers = [1,2,3,4,5,6,7,8,9,10]

def print_array(array):
  for item in array:
    print(item)

```

Snippet 7 - Big O:

```python
# this is insertion sort
def insertionSort(arr): 
  for i in range(1, len(arr)): 
    key = arr[i] 
    j = i-1
    while j >=0 and key < arr[j] : 
      arr[j+1] = arr[j] 
      j -= 1
    arr[j+1] = key 
```

Snippet 8 - Big O:
```python
for i in range(len(my_list)):
  min_idx = i
  for j in range(i+1, len(my_list)):
      if my_list[min_idx] > my_list[j]:
          min_idx = j

  my_list[i], my_list[min_idx] = my_list[min_idx], my_list[i]
```

