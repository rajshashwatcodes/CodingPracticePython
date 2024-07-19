import time

def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a wicked fairie is somewhere around here, and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) dagger.\n")

def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock when the door opens and out steps a fairie.")
    print_pause("Eep! This is the wicked fairie!")
    print_pause("The fairie attacks you!\n")

    choice = input("Would you like to (1) fight or (2) run away?\n")
    if choice == "1":
        fight()
    elif choice == "2":
        field()
    else:
        print_pause("Please enter 1 or 2.")
        house()

def cave():
    print_pause("You peer cautiously into the cave.")
    print_pause("It turns out to be only a very small cave.")
    print_pause("Your eye catches a glint of metal behind a rock.")
    print_pause("You have found the magical Sword of Ogoroth!")
    print_pause("You discard your silly old dagger and take the sword with you.")
    print_pause("You walk back out to the field.\n")

    global weapon
    weapon = "Sword of Ogoroth"
    field()

def fight():
    if weapon == "Sword of Ogoroth":
        print_pause("As the fairie moves to attack, you unsheath your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand as you brace yourself for the attack.")
        print_pause("But the fairie takes one look at your shiny new toy and runs away!")
        print_pause("You have rid the town of the fairie. You are victorious!\n")
    else:
        print_pause("You feel a bit under-prepared for this, with only having a tiny dagger.")
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the fairie.")
        print_pause("You have been defeated!\n")

    play_again()

def field():
    print_pause("You are back in the field. Where would you like to go?")
    choice = input("Enter 1 to knock on the door of the house.\nEnter 2 to peer into the cave.\n")
    if choice == "1":
        house()
    elif choice == "2":
        cave()
    else:
        print_pause("Please enter 1 or 2.")
        field()

def play_again():
    choice = input("Would you like to play again? (y/n)\n")
    if choice == "y":
        print_pause("Excellent! Restarting the game...\n")
        play_game()
    elif choice == "n":
        print_pause("Thanks for playing! See you next time.")
    else:
        print_pause("Please enter y or n.")
        play_again()

def play_game():
    global weapon
    weapon = "dagger"
    intro()
    field()

play_game()
