def fibonacci(n):
    if n < 0:
        print("Incorrect input")

    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        fib_num = {
        "fn": 1,
        "fn-1": 1,
        "fn-2": 0,
        }
        
        for x in range(3, n + 1):
            fib_num["fn-2"] = fib_num["fn-1"]
            fib_num["fn-1"] = fib_num["fn"]
            fib_num["fn"] = fib_num["fn-1"] + fib_num["fn-2"]

    return fib_num["fn"]