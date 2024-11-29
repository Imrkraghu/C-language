menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    item = get_dish("Item: ")
    total = 0
    try:
        while True:
            try:
                total += menu[item.title()]
                print("$" + str(round(total, 3)))
                item = get_dish("Item: ")
            except KeyError:
                item = get_dish("Item: ")
                pass
    except EOFError:
        pass

def get_dish(prompt):
    dish = input(prompt)
    while dish.lower() in menu == False:
        dish = input(prompt)
    else:
        return dish

main()