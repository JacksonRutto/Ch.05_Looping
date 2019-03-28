'''
CAMEL GAME
----------
The pseudo-code for how to code this game is in Chapter 5 of the Python Jedi book

'''

miles = 0
thirst = 0
camel =

done = False

while not done:
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
