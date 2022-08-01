# Iterative

def fibonacci(n):
    fib = [1,1]
    prev = 2
    for i in range(2,n+1):
        fib.append(fib[i-2] + fib[i-1])
    return fib


for i in range(16):
    print(fibonacci(i))

# Recursive

def fib(n):
    if n == 0 or n ==1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

def fibonacci(n):
    return [fib(n) for n in range(n+1)]

for i in range(16):
    print(fibonacci(i))