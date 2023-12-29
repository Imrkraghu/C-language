#this is a program which will return emoji if matches description
def convert(check):
    check = check.replace(":)","🙂").replace(":(","🙁")
    return check
def main():
    match = input("enter text: ")
    print(convert(match))
main()