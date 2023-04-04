# practicing Fibonacci recursively

import time

def fib(n):
    if n == 1:
        return 1
    if n == 2:
        return 1
        
    return fib(n-1) + fib(n-2)
    
start = time.time()
print(fib(40))
end = time.time()
print("Time it took to recursively calculate: %f" % (end-start))

def improvedFib(n):
    arr = []
    arr[0] = 1
    arr[1] = 1
    for i in range(3, n):
        fib[i] = fib[i-1] + fib[i-2]
    return fib[n]
    
start = time.time()    
print(improvedFib(40))
end = time.time()
print("Time it took to iteratively calculate: %f" % (end-start))
