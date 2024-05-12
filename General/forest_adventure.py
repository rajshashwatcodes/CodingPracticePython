import time

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious forest...")
    time.sleep(1)
    print("Your objective is to find the hidden treasure.")
    time.sleep(1)

def choose_path():
    print("\nWhich path will you take?")
    time.sleep(0.5)
    print("1. Follow the path to the left.")
    time.sleep(0.5)
    print("2. Venture deeper into the forest.")
    time.sleep(0.5)
    return input("Enter your choice (1 or 2): ")

def explore_path(choice):
    if choice == "1":
        print("\nYou follow the path to the left...")
        time.sleep(1)
        print("You encounter a river blocking your path.")
        time.sleep(1)
        print("What will you do?")
        time.sleep(0.5)
        print("1. Try to swim across.")
        time.sleep(0.5)
        print("2. Look for a bridge.")
        time.sleep(0.5)
        return input("Enter your choice (1 or 2): ")
    elif choice == "2":
        print("\nYou venture deeper into the forest...")
        time.sleep(1)
        print("You come across a dark cave.")
        time.sleep(1)
        print("Do you dare to enter?")
        time.sleep(0.5)
        print("1. Enter the cave.")
        time.sleep(0.5)
        print("2. Continue exploring the forest.")
        time.sleep(0.5)
        return input("Enter your choice (1 or 2): ")

def main():
    intro()
    choice1 = choose_path()
    if choice1 == "1":
        choice2 = explore_path(choice1)
        if choice2 == "1":
            print("\nYou attempt to swim across the river...")
            time.sleep(1)
            print("You are swept away by the strong current and lose consciousness.")
            time.sleep(1)
            print("Game Over. You have failed to find the treasure.")
        elif choice2 == "2":
            print("\nYou search for a bridge and find one nearby.")
            time.sleep(1)
            print("You cross the bridge safely and continue your journey.")
            time.sleep(1)
            print("You reach the treasure and claim your reward!")
    elif choice1 == "2":
        choice2 = explore_path(choice1)
        if choice2 == "1":
            print("\nYou gather your courage and enter the dark cave...")
            time.sleep(1)
            print("You discover the treasure hidden inside the cave!")
            time.sleep(1)
            print("Congratulations! You have found the treasure!")
        elif choice2 == "2":
            print("\nYou decide not to enter the cave and continue exploring the forest.")
            time.sleep(1)
            print("Unfortunately, you are unable to find the treasure.")
            time.sleep(1)
            print("Game Over. You have failed to find the treasure.")

if __name__ == "__main__":
    main()
