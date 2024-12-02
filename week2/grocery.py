#this is a grocery list program which takes input from user and return number of  grocery items
grocery =[]
def userinput():
    print("enter the grocery item or exit to exit")
    try:
        while True:
            try:
                item = str(input("enter the grocery item: "))
                if item != "exit":
                    item = item.upper()
                    grocery.append(item)
                else:
                    return grocerylist()
                    break
            except ValueError:
                 pass
    except EOFError:
     return grocerylist()
def grocerylist():
    for i in range(len(grocery)):
        print(i+1, grocery[i])
userinput()