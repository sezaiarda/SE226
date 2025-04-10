

def count_characters(string: str) -> int:
    """Counts the number of characters in a string."""
    return len(string)


def count_words(string: str) -> int:
    """Counts the number of words in a string."""
    return len(string.split())


def average_word_length(string: str) -> float:
    """Calculates the average word length in a string."""
    words = string.split()
    if not words:
        return 0
    return sum(len(word) for word in words) / len(words)


if __name__ == '__main__':
    # Test the functions
    print("Testing string_utils.py")
    test_string = "Hello, World!"
    print(f"Original string: {test_string}")
    print(f"Number of characters: {count_characters(test_string)}")
    print(f"Number of words: {count_words(test_string)}")
    print(f"Average word length: {average_word_length(test_string)}")
