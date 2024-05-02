import random

def roll_dice():
    return random.randint(1, 6)

def main():
    print("Welcome to the Rolling Dice Game!")

    while True:
        input("Press Enter to roll the dice...")

        dice1 = roll_dice()
        dice2 = roll_dice()
        total = dice1 + dice2

        print("You rolled:", dice1, "and", dice2)
        print("Sum of the numbers:", total)

        play_again = input("Do you want to roll again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing the Rolling Dice Game!")
            break

if __name__ == "__main__":
    main()
