import math


def factorial(x: int) -> int:
    # Using the recursive factorial function from question 1
    if x == 0 or x == 1:
        return 1
    else:
        return x * factorial(x - 1)


def sine_x(x: float, n: int) -> float:
    x_rad = x * math.pi / 180

    # Lambda function, though it should be def
    term = lambda i: ((-1) ** i) * (x_rad ** (2 * i + 1)) / factorial(2 * i + 1)

    result = 0
    for j in range(n + 1):
        result += term(j)

    return result


if __name__ == "__main__":
    _x = float(input("Enter angle in degrees: "))
    _n = int(input("Enter number of terms (n): "))

    _result = sine_x(_x, _n)
    print(f"sin({_x}°) = {_result}")
    print(f"Built-in math.sin({_x}°) = {math.sin(_x * math.pi / 180)}")
