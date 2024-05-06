class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added to the To-Do list.")

    def view_tasks(self):
        if self.tasks:
            print("Tasks in the To-Do list:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")
        else:
            print("No tasks in the To-Do list.")

    def mark_completed(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            print(f"Task '{self.tasks[task_index - 1]}' marked as completed.")
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

    def delete_task(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            print(f"Task '{self.tasks[task_index - 1]}' deleted from the To-Do list.")
            del self.tasks[task_index - 1]
        else:
            print("Invalid task index.")

def main():
    todo_list = ToDoList()

    while True:
        print("\nTo-Do List Application")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Completed")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == '2':
            todo_list.view_tasks()
        elif choice == '3':
            index = int(input("Enter the index of the task to mark as completed: "))
            todo_list.mark_completed(index)
        elif choice == '4':
            index = int(input("Enter the index of the task to delete: "))
            todo_list.delete_task(index)
        elif choice == '5':
            print("Exiting the To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    main()
