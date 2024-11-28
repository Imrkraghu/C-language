#this is cs50 exception handling program
while True:
    try:
        x = int(input("what's x? "))
    except ValueError:
        print("x is not an integer")
    else:
        print(f"x is {x}")