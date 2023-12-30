#this will give 100 dollars if the greetings didn't start with hello or 20 if it start with h
string = input("Greetings: ")
if string.startswith("hello"):
    print("$0")
elif string.startswith("h"):
    print("$20")
else:
    print("$100")