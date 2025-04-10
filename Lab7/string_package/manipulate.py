

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""


def reverse_string(string: str) -> str:
    """Reverses the given string."""
    return string[::-1]


def capitalize_words(string: str) -> str:
    """Capitalizes the first letter of the string."""
    return string.capitalize()


def remove_punctuation(string: str) -> str:
    """Removes punctuation from the string."""
    return string.translate(str.maketrans('', '', punctuation))


if __name__ == '__main__':
    # Test the functions
    print("Testing string_utils.py")
    test_string = "Hello, World!"
    print(f"Original string: {test_string}")
    print(f"Reversed string: {reverse_string(test_string)}")
    print(f"Capitalized string: {capitalize_words(test_string)}")
    print(f"String without punctuation: {remove_punctuation(test_string)}")
