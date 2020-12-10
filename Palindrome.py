# Find whether a number is palindrome or not

def palindrom(x):

    list_digits= [int(i) for i in str(x)]

    k=0
    for i,j in zip(list_digits,list_digits[::-1]):
        if i!=j:
            k+=1
            print(str(x)+" is not a palindrome")
            break

    if k==0:
        print(str(x)+" is a palindrome")


palindrom(1)

palindrom(22)

palindrom(234)

palindrom(565)

palindrom(1234321)
