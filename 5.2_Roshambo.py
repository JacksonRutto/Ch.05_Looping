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

choice = 0
win = 0
loss = 0
done = False

while not done:

    player = int(input("What do you want to throw: \n Type 1 for rock \n Type 2 for paper \n Type 3 for scissors \n Type 4 to quit \n"))
    print()
    while player > 4 or player < 1:
        player = int(input("Invalid option: \n Type 1 for rock \n Type 2 for paper \n Type 3 for scissors \n Type 4 to quit \n"))
    if player == 1:
        choice = "rock"

    elif player == 2:
        choice = "paper"

    elif player == 3:
        choice = "scissors"

    elif player == 4:
        print("Game over")
        print("Final score is", win,"-", loss)
        done = True

    print("You're choice was", choice)

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

    if player == opp_choice:
        print("Tie, go again")

    elif player == 1:
        if opp_choice == 2:
            print("Computer wins")
            loss += 1
        else:
            print("You win!!!")
            win += 1

    elif player == 2:
        if opp_choice == 3:
            print("Computer wins")
            loss += 1
        else:
            print("You win!!!")
            win += 1

    elif player == 3:
        if opp_choice == 1:
            print("Computer wins")
            loss += 1
        else:
            print("You win!!!")
            win += 1
    else:
        print()
    print()
    print(win, "-", loss)
    print()

    if done == True:
        print("Game Over")
        print("Final score is", win, "-", loss)

