import json
import os
from datetime import datetime

DIARY_FILE = 'diary_entries.json'

def load_entries():
    if os.path.exists(DIARY_FILE):
        with open(DIARY_FILE, 'r') as file:
            return json.load(file)
    return []

def save_entries(entries):
    with open(DIARY_FILE, 'w') as file:
        json.dump(entries, file, indent=4)

def add_entry(title, content):
    entries = load_entries()
    entry = {
        'title': title,
        'content': content,
        'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    entries.append(entry)
    save_entries(entries)
    print("Entry added successfully!")

def view_entries():
    entries = load_entries()
    if not entries:
        print("No entries found.")
        return
    for entry in entries:
        print(f"Date: {entry['date']}")
        print(f"Title: {entry['title']}")
        print(f"Content: {entry['content']}\n")

def search_entries(keyword):
    entries = load_entries()
    found_entries = [entry for entry in entries if keyword.lower() in entry['title'].lower() or keyword.lower() in entry['content'].lower()]
    if not found_entries:
        print("No matching entries found.")
        return
    for entry in found_entries:
        print(f"Date: {entry['date']}")
        print(f"Title: {entry['title']}")
        print(f"Content: {entry['content']}\n")

def main():
    while True:
        print("\nPersonal Diary App")
        print("1. Add a new entry")
        print("2. View all entries")
        print("3. Search entries")
        print("4. Exit")
        choice = input("Choose an option: ")
        
        if choice == '1':
            title = input("Title: ")
            content = input("Content: ")
            add_entry(title, content)
        elif choice == '2':
            view_entries()
        elif choice == '3':
            keyword = input("Enter keyword to search: ")
            search_entries(keyword)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
