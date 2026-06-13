import random
import string

def generate_password(length):
    if length < 4:
        print("Password length should be at least 4.")
        return

    # Ensure password contains all character types
    lowercase = random.choice(string.ascii_lowercase)
    uppercase = random.choice(string.ascii_uppercase)
    digit = random.choice(string.digits)
    special = random.choice("!@#$%^&*()_+-=[]{}|;:,.<>?")

    remaining = length - 4

    all_characters = (
        string.ascii_letters +
        string.digits +
        "!@#$%^&*()_+-=[]{}|;:,.<>?"
    )

    password = [lowercase, uppercase, digit, special]

    for _ in range(remaining):
        password.append(random.choice(all_characters))

    random.shuffle(password)

    return "".join(password)

# Main Program
try:
    length = int(input("Enter password length: "))
    password = generate_password(length)

    if password:
        print("\nGenerated Password:")
        print(password)

except ValueError:
    print("Please enter a valid number.")