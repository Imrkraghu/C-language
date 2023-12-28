# its my first python program
name = input("what is your name? ")
#removing whitespace and capitalized name 
name = name.strip().capitalize()
# we overrided separator here 
print("hello, ",name,sep="")
# taking age as input
age = int(input("enter your age: "))
# using f-string here
print(f"hello, {name} your age is {age}")