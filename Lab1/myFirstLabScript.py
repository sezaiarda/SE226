

def q1() -> None:
    name = input("What is your name?\n")
    print(f"Hello {name}.")
    student_id = input("What is your Student ID?\n")
    print(f"Your ID is {student_id}")


def q2() -> None:
    var1 = float(input("Enter var1\n"))
    var2 = float(input("Enter var2\n"))

    var_sum = var1 + var2
    var_diff = var1 - var2
    var_prod = var1 * var2

    print(
        f"var1: {var1}\n"
        f"var2: {var2}\n"
        f"sum: {var_sum}\n"
        f"diff: {var_diff}\n"
        f"prod: {var_prod}"
    )


def q3() -> None:
    name = input("What is your name?\n")
    lab = float(input("What is your lab grade?\n"))
    midterm = float(input("What is your midterm grade?\n"))
    final = float(input("What is your final grade?\n"))
    print(
        f"Name: {name}\n"
        f"Lab: {lab}\n"
        f"Midterm: {midterm}\n"
        f"Final: {final}\n"
        f"Last Score: {lab * 0.25 + midterm * 0.35 + final * 0.4}"
    )


def q4() -> None:
    print("*\n**\n***\n**\n*\n")


def main() -> None:
    q1()
    q2()
    q3()
    q4()


if __name__ == '__main__':
    main()
