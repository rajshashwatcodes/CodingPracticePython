import time

def explore_dungeon():
    print("Welcome to the Text Adventure Game!")
    print("You find yourself in a dark and mysterious dungeon.")

    while True:
        print("\nYou see two doors in front of you. Do you go left (L) or right (R)?")
        choice = input().upper()

        if choice == 'L':
            # Left path
            print("\nYou enter a room filled with treasure chests. You find a key.")
            print("What do you do next?")
            print("A. Open one of the treasure chests.")
            print("B. Return to the previous room.")
            action = input().upper()

            if action == 'A':
                print("\nYou open a chest and find a pile of gold coins!")
            else:
                print("\nYou return to the previous room.")

        else:
            # Right path
            print("\nYou enter a room with a locked door.")
            print("What do you do next?")
            print("A. Try to pick the lock.")
            print("B. Search for a key.")
            action = input().upper()

            if action == 'A':
                print("\nYou attempt to pick the lock, but it's too difficult.")
                print("You hear footsteps approaching. You hide!")
                print("A guard walks in, but doesn't notice you.")
            else:
                print("\nYou search the room and find a key hidden behind a painting.")
                print("You use the key to unlock the door and proceed.")

        # Continue exploring or end the game
        print("\nDo you want to continue exploring? (Y/N)")
        continue_exploring = input().upper()
        if continue_exploring != 'Y':
            print("\nYou decide to leave the dungeon and end your adventure.")
            break

# Start the game
explore_dungeon()
