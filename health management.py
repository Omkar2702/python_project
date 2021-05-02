# Health Management System
# You are free to create your own files but don't forget to change the file names in the program!
import datetime


def gettime():
    return datetime.datetime.now()


def write(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Enter your details here: ")
            with open("ex1.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Nice job!")
        elif c == 2:
            value = input("Enter your details here: ")
            with open("food1.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Nice job!")
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Enter your details here: ")
            with open("ex2.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Nice job!")
        elif c == 2:
            value = input("Enter your details here: ")
            with open("food2.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Nice job!")
    elif k == 3:
        c = int(input("enter 1 for exercise and 2 for food"))
        if c == 1:
            value = input("Enter your details here: ")
            with open("ex3.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Nice job!")
        elif c == 2:
            value = input("Enter your details here: ")
            with open("food3.txt", "a") as op:
                op.write(str([str(gettime())]) + ": " + value + "\n")
            print("Nice job!")
    else:
        print("Please enter a valid input[1,2,3]")


def retrieve(k):
    if k == 1:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("ex1.txt") as op:
                print(op.read())
        elif c == 2:
            with open("food1.txt") as op:
                print(op.read())
    elif k == 2:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("ex2.txt") as op:
                print(op.read())
        elif c == 2:
            with open("food2.txt") as op:
                print(op.read())
    elif k == 3:
        c = int(input("Enter 1 for exercise and 2 for food"))
        if c == 1:
            with open("ex3.txt") as op:
                print(op.read())
        elif c == 2:
            with open("food3.txt") as op:
                print(op.read())
    else:
        print("Please enter a valid input [1,2,3]")


print("Welcome to My Health Management System!")
a = int(input("Enter 1 for writing the data or 2 for retrieving the data "))

if a == 1:
    b = int(input("Enter 1 for Omkar, 2 for Gurleen & 3 for Simrat: "))
    write(b)
else:
    b = int(input("Enter 1 for Omkar, 2 for Gurleen & 3 for Simrat: "))
    retrieve(b)
