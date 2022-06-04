def factorial(num):
    if num <= 0:
        print('Invalid input')
    else:
        result = 1

    for x in range(1, num + 1):
        result *= x
    return result   