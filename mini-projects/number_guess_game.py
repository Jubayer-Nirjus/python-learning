
import random

number = random.randint(1,10)

guess = int(input("Guess number between 1-10: "))

if guess == number:
    print("Correct!")
else:
    print("Wrong. Number was", number)