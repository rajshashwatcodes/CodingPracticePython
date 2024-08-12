import datetime

class Diary:
    def __init__(self):
        self.entries = []

    def add_entry(self, title, content):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = {
            'title': title,
            'content': content,
            'timestamp': timestamp
        }
        self.entries.append(entry)
        print("Entry added successfully!")

    def view_entries(self):
        if not self.entries:
            print("No entries yet.")
        else:
            for i, entry in enumerate(self.entries, 1):
                print(f"\nEntry {i}:")
                print(f"Title: {entry['title']}")
                print(f"Date: {entry['timestamp']}")
                print(f"Content: {entry['content']}")
                print("-" * 40)

def main():
    my_diary = Diary()

    while True:
        print("\nPersonal Diary Application")
        print("1. Add Entry")
        print("2. View Entries")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            title = input("Enter the title: ")
            content = input("Write your entry: ")
            my_diary.add_entry(title, content)
        elif choice == '2':
            my_diary.view_entries()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1, 2, or 3.")

if __name__ == "__main__":
    main()
