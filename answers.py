# Basic Calculator Program
# Description: This program takes two numbers and a math operation from the user, then  performs the calculation, and prints the result.
# Greet the user
print("Welcome to the Python Basic Calculator!")
print("You can perform: addition (+), subtraction (-), multiplication (*), or division (/)\n")
# Get input from the user
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")
    # Perform calculation based on the operation entered
    if operation == '+':
        result = num1 + num2
        print(f"\nResult: {num1} + {num2} = {result}")

    elif operation == '-':
        result = num1 - num2
        print(f"\nResult: {num1} - {num2} = {result}")

    elif operation == '*':
        result = num1 * num2
        print(f"\nResult: {num1} * {num2} = {result}")

    elif operation == '/':
        # Handle division by zero
        if num2 == 0:
            print("\nError: Division by zero is not allowed.")
        else:
            result = num1 / num2
            print(f"\nResult: {num1} / {num2} = {result}")

    else:
        # If user enters an invalid operator
        print("\nInvalid operation. Please enter one of +, -, *, or /.")

except ValueError:
    # Handles cases where user input is not a valid number
    print("\nError: Please enter valid numeric values.")

# End message
print("\nThank you for using the calculator!")


