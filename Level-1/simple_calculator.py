def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    else:
        return a / b

first_number = float(input("Enter first number: "))
second_number = float(input("Enter second number: "))

print("\nChoose an operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result:", add(first_number, second_number))
elif choice == "2":
    print("Result:", subtract(first_number, second_number))
elif choice == "3":
    print("Result:", multiply(first_number, second_number))
elif choice == "4":
    print("Result:", divide(first_number, second_number))
else:
    print("Invalid choice")
