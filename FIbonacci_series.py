# Whether a number is a Fibonacci number or # not

def fib_series(n):
    if n>1:
        fib = fib_series(n-1) + fib_series(n-2)
        return fib
    elif n==1:
        return 1
    elif n==0:
        return 0

print(fib_series(4))

print(fib_series(3))

print(fib_series(10))
