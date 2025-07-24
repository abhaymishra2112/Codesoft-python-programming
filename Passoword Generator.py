import random
import string
def generate_password(length):
    if length < 4:
        return "Password length should be at least 4."
    # Character sets: letters, digits, symbols
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
def main():
    print("Password Generator")
    try:
        length = int(input("Enter desired password length: "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Invalid input! Please enter a valid number.")
if __name__ == "__main__":
    main()
