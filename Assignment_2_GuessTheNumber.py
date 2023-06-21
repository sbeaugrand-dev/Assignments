## Guess The Number Assignment
import random
x = random.randint(1,10)
y = int(input('Please enter a number between 1 and 10 '))

while y != x:
    if y > x:
        y = int(input('The number is smaller than the one you provided. Please try again '))
    elif y < x:
        y = int(input('The number is larger than the one you provided. Please try again '))
print('Great job! You guessed the correct number!')