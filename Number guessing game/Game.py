
import random

number = random.randint(1, 10)

print("Welcome to Number Guessing Game")
print("Guess a number between 1 and 10")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Congratulations! You guessed it right")

elif guess < number:
    print("Your guess is too low")
    print("The correct number was:", number)

else:
    print("Your guess is too high")
    print("The correct number was:", number)
