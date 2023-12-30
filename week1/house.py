#this is a program for match 
name = input("what's your name? ")
name = name.capitalize()
match name:
    case "Harry"|"Hermione"|"Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case _:
        print("who?")