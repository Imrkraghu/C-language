# this is a python program to implement fuel gauges feature 
# takes input of x and y return there division with round of percentage
def main():
    perc = get_int()
    if perc<=1:
        print("E")
    elif perc>=99:
        print("F")
    else:
        print(f"the fuel is {perc} %")
def get_int():
    while True:
        try:
            x = int(input("what's x? "))
            y = int(input("what's y? "))
            if y==0:
                print("the value of y can't be zero")
                continue
            elif(x>y):
                print("the value of x can't be more than y")
                continue
        except ValueError:
            pass
        else:
            perc = (x/y)*100
            perc = round(perc)
            return perc
main()