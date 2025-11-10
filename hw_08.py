import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact {name} has been added.")

    def show_contacts(self):
        if not self.contacts:
            print("The address book is empty.")
        else:
            print("Address Book:")
            for name, phone in self.contacts.items():
                print(f"{name}: {phone}")


def save_data(book, filename="addressbook.pkl"):
    """Save the address book to a file."""
    with open(filename, "wb") as f:
        pickle.dump(book, f)
    print("Data has been saved successfully.")


def load_data(filename="addressbook.pkl"):
    """Load the address book from a file."""
    try:
        with open(filename, "rb") as f:
            print("Data loaded from file.")
            return pickle.load(f)
    except FileNotFoundError:
        print("No saved file found. Creating a new address book...")
        return AddressBook()


def main():
    book = load_data()  # Load saved data if available

    while True:
        print("\nCommands: add - add contact, show - show contacts, exit - quit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            name = input("Name: ").strip()
            phone = input("Phone: ").strip()
            book.add_contact(name, phone)

        elif command == "show":
            book.show_contacts()

        elif command == "exit":
            save_data(book)  # Save before exiting
            print("Program closed. Goodbye!")
            break

        else:
            print("Unknown command. Please try again.")


if __name__ == "__main__":
    main()
