import json
import os

TASKS_FILE = 'tasks.json'

def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as file:
        json.dump(tasks, file, indent=4)

def add_task(task_description):
    tasks = load_tasks()
    task = {
        'description': task_description,
        'completed': False
    }
    tasks.append(task)
    save_tasks(tasks)
    print("Task added successfully!")

def view_tasks():
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return
    for index, task in enumerate(tasks, start=1):
        status = "Done" if task['completed'] else "Not Done"
        print(f"{index}. {task['description']} - {status}")

def complete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        save_tasks(tasks)
        print("Task marked as completed!")
    else:
        print("Invalid task index.")

def delete_task(task_index):
    tasks = load_tasks()
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
        save_tasks(tasks)
        print("Task deleted!")
    else:
        print("Invalid task index.")

def main():
    while True:
        print("\nTo-Do List App")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Complete a task")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            task_description = input("Enter the task description: ")
            add_task(task_description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as completed: ")) - 1
            complete_task(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            delete_task(task_index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
