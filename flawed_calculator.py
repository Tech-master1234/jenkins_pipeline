# flawed_calculator.py

def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts the second number from the first and returns the result."""
    # This function has a bug! It adds instead of subtracting.
    return x + y

def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

def divide(x, y):
    """Divides the first number by the second and returns the result."""
    # This function has a bug and doesn't handle zero division correctly.
    return x / y

def power(x, y):
    """Raises the first number to the power of the second."""
    return x ** y

# The main_menu is omitted here for brevity, as the focus is on the functions.