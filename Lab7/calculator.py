import math_utils

operator_dict = {
    "add": math_utils.add,
    "subtract": math_utils.subtract,
    "multiply": math_utils.multiply,
    "divide": math_utils.divide,
    "power": math_utils.power,
    "mod": math_utils.mod
}


def get_operator() -> str | None:
    """Get the operator from the user."""
    while True:
        print("Available operations: add, subtract, multiply, divide, power, mod")
        operator = input("Enter the operation you want to perform: ").strip().lower()
        if operator not in operator_dict:
            print(f"Invalid operation: {operator}")
            continue
        return operator


def get_numbers() -> tuple[float, float]:
    """Get two numbers from the user."""
    while True:
        try:
            x = float(input("Enter the first number: "))
            y = float(input("Enter the second number: "))
            return x, y
        except ValueError:
            print("Invalid input. Please enter numeric values.")


def main() -> None:
    """Get two numbers and an operator from user and print the result."""
    print("Welcome to the calculator program!")
    x, y = get_numbers()
    operator = get_operator()

    result = operator_dict[operator](x, y)
    print(f"The result of {operator}ing {x} and {y} is: {result}")


if __name__ == '__main__':
    main()
