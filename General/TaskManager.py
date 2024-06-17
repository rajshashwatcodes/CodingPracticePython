import os
import json
from datetime import datetime

TASKS_FILE = 'tasks.json'

class Task:
    def __init__(self, description, due_date=None, completed=False):
        self.description = description
        self.due_date = due_date
        self.completed = completed
        self.created_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def mark_as_done(self):
        self.completed = True

    def to_dict(self):
        return {
            'description': self.description,
            'due_date': self.due_date,
            'completed': self.completed,
            'created_at': self.created_at
        }

class TaskManager:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r') as file:
                tasks_data = json.load(file)
                return [self.dict_to_task(task_data) for task_data in tasks_data]
        return []

    def save_tasks(self):
        with open(TASKS_FILE, 'w') as file:
            tasks_data = [task.to_dict() for task in self.tasks]
            json.dump(tasks_data, file, indent=4)

    def dict_to_task(self, task_data):
        task = Task(task_data['description'], task_data['due_date'], task_data['completed'])
        task.created_at = task_data['created_at']
        return task

    def add_task(self, description, due_date=None):
        task = Task(description, due_date)
        self.tasks.append(task)
        self.save_tasks()
        print("Task added successfully!")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks found.")
            return
        for index, task in enumerate(self.tasks, start=1):
            status = "Done" if task.completed else "Pending"
            due_date = f" (Due: {task.due_date})" if task.due_date else ""
            print(f"{index}. {task.description} - {status}{due_date} (Created: {task.created_at})")

    def mark_task_as_done(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()
            self.save_tasks()
            print("Task marked as done!")
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks.pop(task_index)
            self.save_tasks()
            print("Task deleted!")
        else:
            print("Invalid task index.")

def main():
    task_manager = TaskManager()
    while True:
        print("\nTo-Do List Application")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark a task as done")
        print("4. Delete a task")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter the task description: ")
            due_date = input("Enter the due date (optional, YYYY-MM-DD): ") or None
            task_manager.add_task(description, due_date)
        elif choice == '2':
            task_manager.view_tasks()
        elif choice == '3':
            task_index = int(input("Enter the task number to mark as done: ")) - 1
            task_manager.mark_task_as_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter the task number to delete: ")) - 1
            task_manager.delete_task(task_index)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
