

class HarmonicNumber:

    def __init__(self):
        self._harmonic_sum = 0

    def harmonic_number(self, n: float) -> None:
        """
        Calculate the nth harmonic number recursively using a global variable.

        The harmonic number Hn is defined as:
        Hn = 1 + 1/2 + 1/3 + ... + 1/n

        The function uses recursion to calculate the sum and updates the global
        variable 'harmonic_sum' instead of returning a value.

        :param n: A positive float representing which harmonic number to calculate
        :return: None, The function updates the global variable 'harmonic_sum'
        """

        if n <= 0:
            return

        if n == 1:
            self._harmonic_sum = 1
            return

        self.harmonic_number(n - 1)

        self._harmonic_sum += 1 / n

    def get_harmonic_sum(self) -> float:
        return self._harmonic_sum


if __name__ == "__main__":
    n = int(input("Enter a positive integer n: "))

    harmonic_number = HarmonicNumber()
    harmonic_number.harmonic_number(n)

    print(f"H({n}) = {harmonic_number.get_harmonic_sum()}")
