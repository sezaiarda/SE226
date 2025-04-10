from string_package import (
    reverse_string, capitalize_words, remove_punctuation, count_characters, count_words, average_word_length
)


def main() -> None:
    """Main function to demonstrate string manipulation and statistics."""

    text = input("Enter a string: ")
    print(f"Reversed and Capitalized string: {capitalize_words(reverse_string(text))}")
    text = remove_punctuation(text)
    print(f"Removed punctuation: {text}")
    print(f"Number of characters: {count_characters(text)}")
    print(f"Number of words: {count_words(text)}")

    print(f"Average word length: {average_word_length(text)}")


if __name__ == '__main__':
    main()