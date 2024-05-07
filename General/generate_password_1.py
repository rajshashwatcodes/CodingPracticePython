import random
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Welcome to the Random Password Generator!")
    length = int(input("Enter the length of the password (default is 12): ") or 12)
    password = generate_password(length)
    print("Your random password is:", password)

if __name__ == "__main__":
    main()
