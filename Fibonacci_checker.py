# Whether a number is Fibonacci or not

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

def fib_or_not(x):
    if (x==2) | (x==3):
        print(str(x)+" is a fibonacci number")
    else:
        list_fib_series = []
        for i in range(x+1):
            list_fib_series.append(fib_series(i))

        k=0
        for j in list_fib_series:
            if j==x:
                k+=1
                print(str(x)+" is a fibonacci number")
                break
        if k==0:
            print(str(x)+" is not a fibonacci number")


fib_or_not(7)

fib_or_not(8)

fib_or_not(3)

fib_or_not(2)

fib_or_not(9)

fib_or_not(0)
