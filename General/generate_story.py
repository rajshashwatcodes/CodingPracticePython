import random

# Lists of different story elements
characters = ["a brave knight", "a clever wizard", "a cunning thief", "a fearless adventurer"]
places = ["in a haunted castle", "in a mystical forest", "in an ancient temple", "in a bustling marketplace"]
actions = ["battled", "discovered", "stole", "protected"]
objects = ["a magical artifact", "a hidden treasure", "a powerful spellbook", "an ancient relic"]

def generate_story():
    character = random.choice(characters)
    place = random.choice(places)
    action = random.choice(actions)
    obj = random.choice(objects)
    
    story = f"One day, {character} {place}, {character} {action} {obj}."
    return story

def main():
    print("Welcome to the Random Story Generator!")
    while True:
        print("\nHere's your story:")
        print(generate_story())
        another = input("\nWould you like to generate another story? (yes/no): ").strip().lower()
        if another != "yes":
            break
    print("Thank you for using the Random Story Generator!")

if __name__ == "__main__":
    main()
