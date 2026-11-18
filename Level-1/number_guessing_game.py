import random

# Generate a random secret number
secret_number = random.randint(1, 100)

# Set the maximum number of attempts
max_attempts = 5
attempts = 0

print("Welcome to the Number Guessing Game!")
print("I have selected a number between 1 and 100.")
print("You have 5 attempts to guess it.")

# Start the game
while attempts < max_attempts:

    guess = int(input("Enter your guess: "))

    attempts = attempts + 1

    if guess > secret_number:
        print("Too high!")

    elif guess < secret_number:
        print("Too low!")

    else:
        print("Congratulations! You guessed correctly!")
        print("Number of attempts:", attempts)
        break

# Check whether the player has used all attempts
if guess != secret_number:
    print("Game over! You have used all your attempts.")
    print("The secret number was:", secret_number)
