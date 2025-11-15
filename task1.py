def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

print("Welcome to the Command-Line Calculator!")

while True:
    print("\nSelect operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == '5':
        print("Exiting calculator. Goodbye!")
        break

    if choice not in ('1', '2', '3', '4'):
        print("Invalid choice. Please select a valid operation.")
        continue

    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == '1':
            result = add(num1, num2)
            operation = '+'
        elif choice == '2':
            result = subtract(num1, num2)
            operation = '-'
        elif choice == '3':
            result = multiply(num1, num2)
            operation = '*'
        elif choice == '4':
            if num2 == 0:
                raise ZeroDivisionError("Division by zero is not allowed.")
            result = divide(num1, num2)
            operation = '/'

        print(f"\nResult: {num1} {operation} {num2} = {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")
    except ZeroDivisionError as e:
        print(e)