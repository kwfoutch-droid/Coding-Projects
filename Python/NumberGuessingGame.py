import random

numberCPU = random.randint(1, 100)
guess = None

while guess != numberCPU:
    guess = int(input("Guess a number between 1 and 100: "))
    if guess < numberCPU:
        print("Too low! Try again.")
    elif guess > numberCPU:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the correct number.")
        