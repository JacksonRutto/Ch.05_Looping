'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: ______________________


 1. Make the following program work.
   '''

print("This program takes three numbers and returns the sum.")
total = 0

for i in range(3):
    x = input("Enter a number: ")
    total = total + i
print("The total is:", x)
  


'''
  2. Write a Python program that will use a FOR loop to print the even
     numbers from 2 to 100, inclusive.
'''

for i in range(0,101):
    if (i % 2 == 0):
        print(i)



'''
  3. Write a program that will use a WHILE loop to count from
     10 down to, and including, 0. Then print the words Blast off! Remember, use
     a WHILE loop, don't use a FOR loop.
'''

i = 11
while i >= 1:
     i -= 1
     print(i)
     if i == 0:
        print("Blast off!")





'''
  4. Write a program that prints a random integer from 1 to 10 (inclusive).
'''

import random

number = random.randrange(1,11)
print(number)



'''
  5. Write a Python program that will:
     
     * Ask the user for seven numbers
     * Print the total sum of the numbers
     * Print the count of the positive entries, the count of entries equal to zero,
     and the count of negative entries. Use an if, elif, else chain, not just three
     if statements.
      
'''
zero = 0
pos = 0
neg = 0

print("Enter 7 numbers")
print()
total = 0
for i in range (7):
    number = int(input("Enter a number: "))
    total += number
    if number > 0:
        pos += 1
    elif number < 0:
        neg += 1
    else:
        zero += 1
print("Total is:", total)
print("Amount of positive entries:", pos)
print("Amount of negative entries:", neg)
print("Amount of entries as zero:", zero)