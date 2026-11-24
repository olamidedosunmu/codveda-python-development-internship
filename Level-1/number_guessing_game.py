"""Codveda Level 1 - Number Guessing Game.

The player has up to five attempts to guess a randomly selected number
between 1 and 100.
"""

# Import random so the program can generate a secret number.
import random

# Choose a random integer from 1 through 100 (both endpoints are included).
secret_number = random.randint(1, 100)

# Set the maximum number of guesses allowed and initialise the counter.
max_attempts = 5
attempts = 0

# Explain the rules to the player before the game starts.
print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 5 attempts to guess it.")

# Repeat the guessing round while the player still has attempts remaining.
while attempts < max_attempts:

    # Collect the player's guess and convert the input text to an integer.
    guess = int(input("Enter your guess: "))

    # Count this guess as one attempt.
    attempts = attempts + 1

    # Tell the player when the guess is greater than the secret number.
    if guess > secret_number:
        print("Too high!")

    # Tell the player when the guess is less than the secret number.
    elif guess < secret_number:
        print("Too low!")

    # If neither condition is true, the player has guessed correctly.
    else:
        print("Congratulations! You guessed correctly!")
        print("Number of attempts:", attempts)

        # Stop the loop because the game has been won.
        break

# After the loop, check whether the player failed to guess the number.
if guess != secret_number:
    print("Game over! You have used all your attempts.")
    print("The secret number was:", secret_number)
