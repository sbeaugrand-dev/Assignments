# Dice Roling Simulator Assignment
import random
def roll_die():
    print(random.randint(1,6))
x = "yes"
while x == "yes":
    roll_die()
    x = (input('Do you want to roll again?'))
