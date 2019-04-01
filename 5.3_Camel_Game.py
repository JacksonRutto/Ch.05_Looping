'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

import random

miles = 0
thirst = 0
camel = 0
natives = -20
canteen = 3

done = False

while not done:
    print()
    print("A. Drink from your canteen")
    print("B. Ahead moderate speed")
    print("C. Ahead full speed")
    print("D. Stop for the night")
    print("E. Status check")
    print("Q. Quit")

    print()

    user_choice = input("What's your choice? ")

    if user_choice.upper() == "Q":
        done = True

    elif user_choice.upper() == "E":
        print()
        print("Miles traveled:", miles)
        print("Drinks in canteen", canteen)
        print("The natives are", natives, "miles behind you")

    elif user_choice.upper() == "D":
        print()
        camel = 0
        print("Camel is happy :)")
        natives += random.randrange(7,15)

    elif user_choice.upper() == "C":
        print()
        miles += random.randrange(10,21)
        thirst += 1
        camel += random.randrange(1,4)
        natives += random.randrange(7, 15)
        print(miles)
        print(natives)
        print(camel)
        print(thirst)