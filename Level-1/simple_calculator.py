"""Codveda Level 1 - Simple Calculator.

This program performs addition, subtraction, multiplication, and division
using separate functions.
"""


# Each function receives two numbers and returns the result of an operation.
def add(a, b):
    # Add the two numbers and send the answer back to the caller.
    return a + b


def subtract(a, b):
    # Subtract the second number from the first number.
    return a - b


def multiply(a, b):
    # Multiply the two numbers.
    return a * b


def divide(a, b):
    # Check the denominator first to prevent division by zero.
    if b == 0:
        return "Cannot divide by zero"
    else:
        # Divide the first number by the second number.
        return a / b


# input() collects the values as text, while float() converts them to numbers.
first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

# Display the four operations the user can choose from.
print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Store the user's selected operation.
choice = input("Enter your choice (1-4): ")

# Check the selected option and call the matching function.
if choice == "1":
    print("Result:", add(first_number, second_number))
elif choice == "2":
    print("Result:", subtract(first_number, second_number))
elif choice == "3":
    print("Result:", multiply(first_number, second_number))
elif choice == "4":
    print("Result:", divide(first_number, second_number))
else:
    # Inform the user when the selected menu option is not valid.
    print("Invalid choice")
