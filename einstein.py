#this is a program to print no. of joules by using e= mc^2
def energy(weight):
    joules = weight*300000000*300000000
    return joules
def main():
    mass =int(input("enter the mass: "))
    print(energy(mass))
main()