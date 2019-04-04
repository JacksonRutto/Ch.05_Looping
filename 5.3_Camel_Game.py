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

# user choices

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
        print("Game Over")
        done = True

    elif user_choice.upper() == "E":
        print()
        print("Miles traveled:", miles)
        print("Drinks in canteen", canteen)
        print("The natives are", miles - natives, "miles behind you")
        print(camel)
        print(thirst)

    elif user_choice.upper() == "D":
        print()
        camel = 0
        print("Camel is happy :)")
        natives += random.randrange(7, 15)

    elif user_choice.upper() == "C":
        print()
        miles += random.randrange(10, 21)
        print(miles)
        thirst += 1
        camel += random.randrange(1, 4)
        natives += random.randrange(7, 15)

    elif user_choice.upper() == "B":
        print()
        miles += random.randrange(5, 13)
        print(miles)
        thirst += 1
        camel += 1
        natives += random.randrange(7, 15)

    elif user_choice.upper() == "A":
        print()
        if canteen > 0:
            canteen -= 1
            thirst = 0
        elif canteen == 0:
            print("No drinks left in canteen, must refill")
        else:
            print("No drinks left in canteen, must refill")

    if thirst > 4:
        print("You are thirsty")
        if thirst == 6:
            break

    if thirst >= 6:
        print("Game Over")
        print("You died of thirst")
        done = True

    if not done and camel > 5:
        print("Your camel is getting tired")
        if camel == 8:
            print("Your camel is dead")
            break

    if natives >= miles:
        print("Game Over")
        print("The natives have caught you")
        done = True

    elif natives >= miles - 15:
        print("natives are getting close")

    if miles >= 200:
        print("You won!!!")
        done = True

    oasis = random.randrange(1, 21)

    if oasis == 1:
        print()
        print("You found an oasis")
        canteen = 3
        thirst = 0
        camel = 0
