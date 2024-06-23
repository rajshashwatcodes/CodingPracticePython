# To-Do List Application

import datetime

# To-Do List storage
tasks = []

def add_task(task_description):
    task = {
        'description': task_description,
        'completed': False,
        'timestamp': datetime.datetime.now()
    }
    tasks.append(task)
    print(f"Task '{task_description}' added successfully.")

def view_tasks():
    if tasks:
        print("\nYour To-Do List:")
        for i, task in enumerate(tasks):
            status = "Completed" if task['completed'] else "Not Completed"
            timestamp = task['timestamp'].strftime("%Y-%m-%d %H:%M:%S")
            print(f"{i + 1}. {task['description']} - {status} (Added on {timestamp})")
    else:
        print("\nYour To-Do List is empty.")

def mark_task_as_complete(task_number):
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]['completed'] = True
        print(f"Task '{tasks[task_number - 1]['description']}' marked as complete.")
    else:
        print("Invalid task number.")

def delete_task(task_number):
    if 0 < task_number <= len(tasks):
        task = tasks.pop(task_number - 1)
        print(f"Task '{task['description']}' deleted successfully.")
    else:
        print("Invalid task number.")

def main():
    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Complete")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task_description = input("Enter task description: ")
            add_task(task_description)
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            view_tasks()
            task_number = int(input("Enter task number to mark as complete: "))
            mark_task_as_complete(task_number)
        elif choice == '4':
            view_tasks()
            task_number = int(input("Enter task number to delete: "))
            delete_task(task_number)
        elif choice == '5':
            print("Exiting To-Do List Application.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
