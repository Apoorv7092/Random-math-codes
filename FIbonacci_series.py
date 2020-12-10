# Whether a number is a Fibonacci number or # not

def fib_series(n):
    if n>1:
        globals()["f_%i"%(n-1)] = fib_series(n-1)
        globals()["f_%i"%(n-2)] = fib_series(n-2)
        globals()["f_%i" %n] = globals()["f_%i"%(n-1)] +globals()["f_%i"%(n-2)]
        return globals()["f_%i" %n]
    elif n==1:
        return 1
    elif n==0:
        return 0

print(fib_series(4))

print(fib_series(3))

print(fib_series(10))
