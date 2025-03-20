import random
import sys


lowercase_letters = 'abcdefghijklmnopqrstuvwxyz'

def get_valid_letter(existing_letters):
    while True:
        letter = input("Enter a lowercase character: ").strip()
        if len(letter) != 1:
            print("Error: Please enter exactly one character.")
            continue
        if letter not in lowercase_letters:
            print("Error: Please enter a lowercase letter (a-z).")
            continue
        if letter in existing_letters:
            print(f"Error: The letter '{letter}' has already been chosen. Please select another.")
            continue
        return letter


def get_valid_replacement(letter, used_replacements, current_replacements):
    while True:
        replacement = input(f"Enter replacement #{len(current_replacements) + 1} for '{letter}': ").strip()
        if len(replacement) != 1:
            print("Error: Please enter exactly one character.")
            continue
        if replacement in used_replacements:
            print("Error: This character is already used as a replacement. Please choose another.")
            continue
        return replacement


def collect_letter_replacements(num_letters=5, num_replacements=3):
    letter_replacements = {}
    used_replacements = set()

    print(f"\nSelect {num_letters} letters and assign {num_replacements} replacement characters to each:")

    for i in range(num_letters):
        print(f"\nLetter {i + 1} of {num_letters}")
        letter = get_valid_letter(letter_replacements.keys())

        replacements = set()
        for j in range(num_replacements):
            replacement = get_valid_replacement(letter, used_replacements, replacements)
            replacements.add(replacement)
            used_replacements.add(replacement)

        letter_replacements[letter] = replacements

    return letter_replacements


def generate_random_passwords(length=15, count=5):
    return [''.join(random.choices(lowercase_letters, k=length)) for _ in range(count)]


def apply_replacements(passwords, letter_replacements):
    categorized_passwords = {"STRONG PASSWORDS": [], "WEAK PASSWORDS": []}

    for password in passwords:
        new_password = ""
        replaced_count = 0

        for char in password:
            if char in letter_replacements:
                replacement = random.choice(list(letter_replacements[char]))
                new_password += replacement
                replaced_count += 1
            else:
                new_password += char

        category = "STRONG PASSWORDS" if replaced_count > 4 else "WEAK PASSWORDS"
        categorized_passwords[category].append(new_password)

    return categorized_passwords


def display_results(categorized_passwords, original_passwords=None):
    print("GENERATED PASSWORDS")

    if original_passwords:
        print("\nOriginal passwords:")
        for pwd in original_passwords:
            print(f"  {pwd}")
        print()

    for category, pwd_list in categorized_passwords.items():
        print(f"\n{category} ({len(pwd_list)}):")
        print("-" * 50)
        for pwd in pwd_list:
            print(f"  {pwd}")


def display_letter_replacements(letter_replacements):
    print("LETTER REPLACEMENT RULES")

    for letter, replacements in letter_replacements.items():
        replacements_str = ", ".join(replacements)
        print(f"  Letter '{letter}' → {replacements_str}")


def main():
    try:
        letter_replacements = collect_letter_replacements()
        passwords = generate_random_passwords()
        categorized_passwords = apply_replacements(passwords, letter_replacements)
        display_letter_replacements(letter_replacements)
        display_results(categorized_passwords, passwords)

        print("\nProgram completed successfully.")

    except KeyboardInterrupt:
        print("\n\nProgram terminated by user.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()