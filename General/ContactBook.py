class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Email: {self.email}"


class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone_number, email):
        new_contact = Contact(name, phone_number, email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added successfully!")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted successfully!")
                return
        print(f"Contact {name} not found!")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print(f"Contact {name} not found!")

    def view_all_contacts(self):
        if not self.contacts:
            print("Contact book is empty.")
        else:
            print("All Contacts:")
            for contact in self.contacts:
                print(contact)


def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. View All Contacts")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_book.add_contact(name, phone_number, email)

        elif choice == "2":
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)

        elif choice == "3":
            name = input("Enter the name of the contact to search: ")
            contact_book.search_contact(name)

        elif choice == "4":
            contact_book.view_all_contacts()

        elif choice == "5":
            print("Exiting Contact Book. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
