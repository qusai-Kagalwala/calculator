# Angela Yu - 100 Days of Code - Day 10: Calculator Program
# This program creates a functional calculator that performs basic arithmetic operations
# and allows users to continue calculations with previous results or start fresh

import art


# Basic arithmetic operation functions
def add(n1, n2):
    """Add two numbers and return the result."""
    return n1 + n2


def subtract(n1, n2):
    """Subtract second number from first number and return the result."""
    return n1 - n2


def multiply(n1, n2):
    """Multiply two numbers and return the result."""
    return n1 * n2


def divide(n1, n2):
    """Divide first number by second number and return the result."""
    return n1 / n2


# Dictionary mapping operation symbols to their corresponding functions
operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

# Example of how to use the operations dictionary
# print(operations["*"](4, 8))


def calculator():
    """
    Main calculator function that handles user input and performs calculations.
    Allows for continuous calculations using previous results.
    """
    # Display the calculator logo from art module
    print(art.logo)
    
    # Flag to control whether to continue with accumulated results
    should_accumulate = True
    
    # Get the first number from user
    num1 = float(input("What is the first number?: "))

    # Main calculation loop
    while should_accumulate:
        # Display available operations to user
        for symbol in operations:
            print(symbol)
        
        # Get operation choice from user
        operation_symbol = input("Pick an operation: ")
        
        # Get the second number from user
        num2 = float(input("What is the next number?: "))
        
        # Perform the calculation using the operations dictionary
        answer = operations[operation_symbol](num1, num2)
        
        # Display the calculation result
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        # Ask user if they want to continue with the result or start fresh
        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            # Continue with the current result as the new first number
            num1 = answer
        else:
            # Exit the accumulation loop and start a new calculation
            should_accumulate = False
            print("\n" * 20)  # Clear screen with newlines
            calculator()  # Recursive call to start fresh


# Start the calculator program
calculator()