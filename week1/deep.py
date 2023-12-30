def main():
    print("what is the Answer to the Great Question of Life, the Universe and Everything?")
    Answer = input("")
    Answer = Answer.title()
    match Answer:
        case "42"|"Fourty Two"|"Fourty-Two":
            print("yes")
        case _:
            print("No")
main()