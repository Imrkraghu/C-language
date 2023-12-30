#this is a math interpretor
question = input("expression: ")
first, operator, second = question.split()
match operator:
    case "+":
        print(float(first) + float(second))
    case "-":
        print(float(first) - float(second))
    case "/":
        print(float(first) / float(second))
    case "*":
        print(float(first) * float(second))
    case _:
        print("Invalid Values")