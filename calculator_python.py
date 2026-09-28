def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def calculator():
    print("=" * 30)
    print("       PYTHON CALCULATOR")
    print("=" * 30)

    while True:
        print("\nSelect an operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")
        print("5. Exit")

        choice = input("\nEnter your choice (1-5): ")

        if choice == "5":
            print("\nThank you for using the calculator!")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice. Please select 1-5.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == "1":
                result = add(num1, num2)
                operator = "+"

            elif choice == "2":
                result = subtract(num1, num2)
                operator = "-"

            elif choice == "3":
                result = multiply(num1, num2)
                operator = "*"

            elif choice == "4":
                result = divide(num1, num2)
                operator = "/"

            print(f"\n{num1} {operator} {num2} = {result}")

        except ValueError as error:
            print(f"\nError: {error}")

        except Exception:
            print("\nSomething went wrong. Please try again.")


if __name__ == "__main__":
    calculator()
