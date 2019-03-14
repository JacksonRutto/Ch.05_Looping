'''
ROSHAMBO PROGRAM
----------------

Create a program that randomly prints 1, 2, or 3.
Expand the program so it randomly prints rock, paper, or scissors using if statements. Don't select from a list.
Add to the program so it first asks the user their choice as well as if they want to quit.
(It will be easier if you have them enter 1 for rock, 2 for paper, and 3 for scissors.)
Add conditional statements to figure out who wins and keep the records
When the user quits print a win/loss record

'''
import random


while True:

    player = int(input("What do you want to throw: \n Type 1 for rock \n Type 2 for paper \n Type 3 for scissors \n"))
print()
    while player > 3 or player < 1:
        player = int(input("Invalid option: \n Type 1 for rock \n Type 2 for paper \n Type 3 for scissors \n"))
    if player == 1:
        choice = "rock"

    elif player == 2:
        choice = "paper"

    else:
        choice = "scissors"

    print("You're choice was", choice)
print()
    opp_choice = random.randrange(1, 4)

    if opp_choice == 1:
        opp = "rock"

    elif opp_choice == 2:
        opp = "paper"

    else:
        opp = "scissors"

    print("Computer choice was", opp)
    print()
    print(choice, "vs", opp)









