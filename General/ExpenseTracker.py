import json
import os
from datetime import datetime

EXPENSES_FILE = 'expenses.json'

class Expense:
    def __init__(self, amount, category, description=''):
        self.amount = amount
        self.category = category
        self.description = description
        self.date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def to_dict(self):
        return {
            'amount': self.amount,
            'category': self.category,
            'description': self.description,
            'date': self.date
        }

class ExpenseTracker:
    def __init__(self):
        self.expenses = self.load_expenses()

    def load_expenses(self):
        if os.path.exists(EXPENSES_FILE):
            with open(EXPENSES_FILE, 'r') as file:
                expenses_data = json.load(file)
                return [self.dict_to_expense(expense_data) for expense_data in expenses_data]
        return []

    def save_expenses(self):
        with open(EXPENSES_FILE, 'w') as file:
            expenses_data = [expense.to_dict() for expense in self.expenses]
            json.dump(expenses_data, file, indent=4)

    def dict_to_expense(self, expense_data):
        expense = Expense(expense_data['amount'], expense_data['category'], expense_data['description'])
        expense.date = expense_data['date']
        return expense

    def add_expense(self, amount, category, description=''):
        expense = Expense(amount, category, description)
        self.expenses.append(expense)
        self.save_expenses()
        print("Expense added successfully!")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses found.")
            return
        for index, expense in enumerate(self.expenses, start=1):
            print(f"{index}. ${expense.amount} - {expense.category} - {expense.description} (Date: {expense.date})")

    def delete_expense(self, expense_index):
        if 0 <= expense_index < len(self.expenses):
            self.expenses.pop(expense_index)
            self.save_expenses()
            print("Expense deleted!")
        else:
            print("Invalid expense index.")

def main():
    expense_tracker = ExpenseTracker()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            amount = float(input("Enter the amount: $"))
            category = input("Enter the category: ")
            description = input("Enter a description (optional): ")
            expense_tracker.add_expense(amount, category, description)
        elif choice == '2':
            expense_tracker.view_expenses()
        elif choice == '3':
            expense_index = int(input("Enter the expense number to delete: ")) - 1
            expense_tracker.delete_expense(expense_index)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
