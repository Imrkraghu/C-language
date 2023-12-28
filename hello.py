# its my first python program
name = input("what is your full name? ")
#removing whitespace and capitalized name 
name = name.strip().capitalize()
# spliting the name into first and last name
first, last =  name.split(" ")
# we overrided separator here 
print("hello, Mr. ",last,sep="")
# taking age as input
age = int(input("enter your age: "))
# using f-string here
print(f"hello, Mr. {last} your age is {age}")