import random

def generate_random_art(width, height):
    characters = ['@', '#', '$', '%', '&', '*', '+', '-', '.', ' ']
    art = ""

    for _ in range(height):
        line = "".join(random.choice(characters) for _ in range(width))
        art += line + "\n"

    return art

def main():
    width = 40
    height = 20
    print("Random ASCII Art:\n")
    print(generate_random_art(width, height))

if __name__ == "__main__":
    main()
