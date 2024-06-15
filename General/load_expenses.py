import json
import os
from datetime import datetime

EXPENSES_FILE = 'expenses.json'

def load_expenses():
    if os.path.exists(EXPENSES_FILE):
        with open(EXPENSES_FILE, 'r') as file:
            return json.load(file)
    return []

def save_expenses(expenses):
    with open(EXPENSES_FILE, 'w') as file:
        json.dump(expenses, file, indent=4)

def add_expense(amount, category, description):
    expenses = load_expenses()
    expense = {
        'amount': amount,
        'category': category,
        'description': description,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    expenses.append(expense)
    save_expenses(expenses)
    print("Expense added successfully!")

def view_expenses():
    expenses = load_expenses()
    if not expenses:
        print("No expenses found.")
        return
    for index, expense in enumerate(expenses, start=1):
        print(f"{index}. {expense['date']} - {expense['category']}: ${expense['amount']} ({expense['description']})")

def delete_expense(expense_index):
    expenses = load_expenses()
    if 0 <= expense_index < len(expenses):
        expenses.pop(expense_index)
        save_expenses(expenses)
        print("Expense deleted!")
    else:
        print("Invalid expense index.")

def generate_summary():
    expenses = load_expenses()
    if not expenses:
        print("No expenses to summarize.")
        return
    total_amount = sum(expense['amount'] for expense in expenses)
    category_summary = {}
    for expense in expenses:
        category = expense['category']
        category_summary[category] = category_summary.get(category, 0) + expense['amount']
    
    print(f"Total Expenses: ${total_amount}")
    print("Expenses by Category:")
    for category, amount in category_summary.items():
        print(f"{category}: ${amount}")

def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add a new expense")
        print("2. View all expenses")
        print("3. Delete an expense")
        print("4. Generate summary report")
        print("5. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            view_expenses()
        elif choice == '3':
            expense_index = int(input("Enter the expense number to delete: ")) - 1
            delete_expense(expense_index)
        elif choice == '4':
            generate_summary()
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
