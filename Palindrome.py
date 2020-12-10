# Find whether a number is palindrome or not

def palindrom(x):

    list_digits= [int(i) for i in str(x)]

    if list_digits==list_digits[::-1]):
        print(str(x)+ " is a palindrome")
    else:
        print(str(x)+ " is not a palindrome")

palindrom(1)

palindrom(22)

palindrom(234)

palindrom(565)

palindrom(1234321)
