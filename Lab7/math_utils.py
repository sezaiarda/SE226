

def add(x: float, y: float) -> float:
    """Add two numbers."""
    return x + y


def subtract(x: float, y: float) -> float:
    """Subtract two numbers."""
    return x - y


def multiply(x: float, y: float) -> float:
    """Multiply two numbers."""
    return x * y


def divide(x: float, y: float) -> float:
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x / y


def power(x: float, y: float) -> float:
    """Raise x to the power of y."""
    return x ** y


def mod(x: float, y: float) -> float:
    """Return the modulus of x and y."""
    if y == 0:
        raise ValueError("Cannot divide by zero")
    return x % y


if __name__ == '__main__':
    # Test the functions
    print("Testing math_utils.py")
    print(f"add(2, 3) = {add(2, 3)}")
    print(f"subtract(5, 2) = {subtract(5, 2)}")
    print(f"multiply(3, 4) = {multiply(3, 4)}")
    print(f"divide(10, 2) = {divide(10, 2)}")
    print(f"power(2, 3) = {power(2, 3)}")
    print(f"mod(10, 3) = {mod(10, 3)}")
