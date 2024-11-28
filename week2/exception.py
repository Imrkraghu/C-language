#this is cs50 exception handling program
def main():
    x = get_int()
    print(f"x is {x}")
def get_int():
    while True:
        try:
            x = int(input("what's x? "))
        except ValueError:
            pass
        else:
            return x
main()