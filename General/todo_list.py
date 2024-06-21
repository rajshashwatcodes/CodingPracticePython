import os

TODO_FILE = "todo.txt"

def load_todos():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as file:
        todos = file.readlines()
    return [todo.strip() for todo in todos]

def save_todos(todos):
    with open(TODO_FILE, "w") as file:
        for todo in todos:
            file.write(todo + "\n")

def add_todo():
    todo = input("Enter a new to-do: ")
    todos.append(todo)
    save_todos(todos)
    print(f'To-do "{todo}" added.')

def view_todos():
    if not todos:
        print("No to-dos available.")
        return
    print("Your to-dos:")
    for i, todo in enumerate(todos, 1):
        print(f"{i}. {todo}")

def remove_todo():
    view_todos()
    if not todos:
        return
    try:
        index = int(input("Enter the number of the to-do to remove: ")) - 1
        if 0 <= index < len(todos):
            removed = todos.pop(index)
            save_todos(todos)
            print(f'To-do "{removed}" removed.')
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\nTo-Do List")
        print("1. View to-dos")
        print("2. Add a new to-do")
        print("3. Remove a to-do")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            view_todos()
        elif choice == "2":
            add_todo()
        elif choice == "3":
            remove_todo()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    todos = load_todos()
    main()
