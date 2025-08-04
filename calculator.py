# calculator.py

def add(x, y):
    """Adds two numbers and returns the result."""
    return x + y

def subtract(x, y):
    """Subtracts the second number from the first and returns the result."""
    return x - y

def multiply(x, y):
    """Multiplies two numbers and returns the result."""
    return x * y

def divide(x, y):
    """Divides the first number by the second and returns the result."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

def power(x, y):
    """Raises the first number to the power of the second."""
    return x ** y

def main_menu():
    """Displays the main menu and handles user input."""
    print("Welcome to the Python Calculator!")
    print("Select an operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    print("6. Exit")

    while True:
        try:
            choice = input("Enter your choice (1-6): ")
            if choice == '6':
                print("Exiting calculator. Goodbye!")
                break

            if choice in ('1', '2', '3', '4', '5'):
                num1 = float(input("Enter the first number: "))
                num2 = float(input("Enter the second number: "))

                if choice == '1':
                    print(f"{num1} + {num2} = {add(num1, num2)}")
                elif choice == '2':
                    print(f"{num1} - {num2} = {subtract(num1, num2)}")
                elif choice == '3':
                    print(f"{num1} * {num2} = {multiply(num1, num2)}")
                elif choice == '4':
                    try:
                        print(f"{num1} / {num2} = {divide(num1, num2)}")
                    except ValueError as e:
                        print(f"Error: {e}")
                elif choice == '5':
                    print(f"{num1} ** {num2} = {power(num1, num2)}")
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main_menu()