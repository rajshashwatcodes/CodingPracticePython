import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.items = []
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def add_item(self, item):
        self.items.append(item)

    def remove_item(self, item):
        self.items.remove(item)

class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []

    def move(self, direction):
        if direction in self.current_room.exits:
            self.current_room = self.current_room.exits[direction]
            print(f"You move to the {self.current_room.name}.")
            print(self.current_room.description)
        else:
            print("You can't go that way!")

    def pick_up(self, item_name):
        for item in self.current_room.items:
            if item.name == item_name:
                self.inventory.append(item)
                self.current_room.remove_item(item)
                print(f"You picked up the {item_name}.")
                return
        print(f"There is no {item_name} here.")

    def drop(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                self.inventory.remove(item)
                self.current_room.add_item(item)
                print(f"You dropped the {item_name}.")
                return
        print(f"You don't have a {item_name}.")

def create_world():
    # Create rooms
    living_room = Room("Living Room", "You are in a cozy living room with a fireplace.")
    kitchen = Room("Kitchen", "You are in a kitchen with a strange smell.")
    garden = Room("Garden", "You are in a beautiful garden with blooming flowers.")
    attic = Room("Attic", "You are in a dusty attic filled with old furniture.")

    # Add exits
    living_room.add_exit("north", kitchen)
    living_room.add_exit("west", garden)
    kitchen.add_exit("south", living_room)
    garden.add_exit("east", living_room)
    living_room.add_exit("up", attic)
    attic.add_exit("down", living_room)

    # Add items
    key = Item("Key", "A small rusty key.")
    map = Item("Map", "A map showing the layout of the house.")
    book = Item("Book", "An old book with strange symbols.")

    living_room.add_item(key)
    kitchen.add_item(map)
    attic.add_item(book)

    return living_room

def main():
    print("Welcome to the Adventure Game!")
    starting_room = create_world()
    player = Player(starting_room)
    print(player.current_room.description)

    while True:
        command = input("> ").strip().lower()
        if command in ["quit", "exit"]:
            print("Thanks for playing!")
            break
        elif command in ["north", "south", "east", "west", "up", "down"]:
            player.move(command)
        elif command.startswith("pick up "):
            item_name = command[8:]
            player.pick_up(item_name)
        elif command.startswith("drop "):
            item_name = command[5:]
            player.drop(item_name)
        elif command == "inventory":
            if player.inventory:
                print("You have:")
                for item in player.inventory:
                    print(f"- {item.name}: {item.description}")
            else:
                print("You are carrying nothing.")
        else:
            print("I don't understand that command.")

if __name__ == "__main__":
    main()
