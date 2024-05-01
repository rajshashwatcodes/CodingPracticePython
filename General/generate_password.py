import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special=True):
    characters = ''
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_special:
        characters += string.punctuation

    if len(characters) == 0:
        raise ValueError("At least one character type should be enabled")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password: "))

    use_uppercase = input("Include uppercase letters? (Y/N): ").upper() == 'Y'
    use_lowercase = input("Include lowercase letters? (Y/N): ").upper() == 'Y'
    use_digits = input("Include digits? (Y/N): ").upper() == 'Y'
    use_special = input("Include special characters? (Y/N): ").upper() == 'Y'

    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special)
        print("Your random password is:", password)
    except ValueError as e:
        print("Error:", e)

if __name__ == "__main__":
    main()
