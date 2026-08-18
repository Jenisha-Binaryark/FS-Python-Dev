import random

number = random.randint(1,10)
guess = 0

print("I'm thinking of a number between 1 and 10.")

while guess != number:
    guess = int(input("Take a guess: "))

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")

print(f"Congratulations! You guessed the secret number {number}!")