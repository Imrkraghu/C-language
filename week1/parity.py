# this is a program to check if a number is odd or even
x = int(input("what's x? "))
if x!=0:
    if x%2 == 0:
        print("the number is even")
        exit()
    else:
        print("the number is odd")
        exit()
print("the number is zero")