import re
from my_logging import logger_init

class Contacts:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def display(self):
        print("****************************\n",
              f" first-name: {self.first_name}\n",
              f" last-name: {self.last_name}\n",
              f" address: {self.address}\n", 
              f" city: {self.city}\n",
              f" state: {self.state}\n",
              f" zip-code: {self.zip_code}\n",
              f" phone-number: {self.phone_number}\n",
              f" email: {self.email}\n",
              "************************")


class AddressBook:
    def __init__(self):
        self.contacts_list = []

    def add_contact(self, contact):
        for existing_contact in self.contacts_list:
            if existing_contact.first_name == contact.first_name and existing_contact.last_name == contact.last_name:
                print(f"Contact {contact.first_name} {contact.last_name} already exists.\n")

                logger_init("UC-7").info(" This name already exists in contacts.")

                logger_init("UC-7").info("This name already exists in contacts.")
                return

        self.contacts_list.append(contact)
        print(f"Contact for {contact.first_name} {contact.last_name} added successfully.\n")
        logger_init("UC-2").info("Added contact successfully.")

    def display_all_contacts(self):
        if not self.contacts_list:
            print("Address Book is empty.\n")
        else:
            for contact in self.contacts_list:
                contact.display()

    def search_contact_by_city_or_state(self, city=None, state=None):
        '''
        Description:
            This function searches for contacts by city or state in an address book.
        Parameters:
            city: City name to search (optional)
            state: State name to search (optional)
        Return:
            List of matching contacts.
        '''
        results = []
        for contact in self.contacts_list:
            if (city and contact.city.lower() == city.lower()) or (state and contact.state.lower() == state.lower()):
                results.append(contact)
        return results


class System:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        if name in self.address_books:
            print(f"Address Book '{name}' already exists.\n")
            logger_init("UC-6").info("This address book name already exists.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address Book '{name}' created successfully.\n")
            logger_init("UC-6").info("Address book created successfully.")

    def select_address_book(self):
        if not self.address_books:
            print("No address books available.\n")
            logger_init("UC-6").info("There is no address book available.")
            return None

        print("Available Address Books:")
        for book_name in self.address_books:
            print(f"- {book_name}")

        selected_name = input("Enter the name of the address book to select: ")

        if selected_name in self.address_books:
            return self.address_books[selected_name]
        else:
            print("Address Book not found.\n")
            return None

    def search_across_address_books(self, city=None, state=None):
        '''
        Description:
            This function searches across all address books for contacts by city or state.
        Parameters:
            city: City name to search (optional)
            state: State name to search (optional)
        Return:
            None
        '''
        all_results = []
        for book_name, address_book in self.address_books.items():
            results = address_book.search_contact_by_city_or_state(city, state)
            if results:
                all_results.extend([(book_name, contact) for contact in results])

        if not all_results:
            print(f"No contacts found in city '{city}' or state '{state}'.\n")
            logger_init("UC-8").info("No contacts found in city or state name")

        else:
            print(f"Found {len(all_results)} contact(s) in city '{city}' or state '{state}':")
            
            for book_name, contact in all_results:
                print(f"From Address Book: {book_name}")
                contact.display()


def main():
    print("Welcome to the Address Book Program")

    system = System()

    while True:
        print("\n1. Create New Address Book\n",
              "2. Select an Address Book\n",
              "3. Search Person by City/State Across Address Books\n",
              "4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            book_name = input("Enter a unique name for the new Address Book: ")
            system.add_address_book(book_name)

        elif choice == '2':
            selected_address_book = system.select_address_book()

            if selected_address_book:
                while True:
                    print("\n1. Add New Contact\n",
                          "2. Display All Contacts\n",
                          "3. Back to Main Menu")

                    sub_choice = input("Enter your choice: ")

                    if sub_choice == '1':
                        first_name = input("Enter first name: ")
                        last_name = input("Enter last name: ")
                        address = input("Enter address: ")
                        city = input("Enter city: ")
                        state = input("Enter state: ")
                        zip_code = input("Enter zip code: ")
                        phone_number = input("Enter phone number: ")
                        email = input("Enter email: ")

                        new_contact = Contacts(first_name, last_name, address, city, state, zip_code, phone_number, email)
                        selected_address_book.add_contact(new_contact)

                    elif sub_choice == '2':
                        selected_address_book.display_all_contacts()

                    elif sub_choice == '3':
                        break

                    else:
                        print("Invalid choice, please try again.")

        elif choice == '3':
            city = input("Enter city to search (leave blank if searching by state): ")
            state = input("Enter state to search (leave blank if searching by city): ")

            system.search_across_address_books(city=city or None, state=state or None)

        elif choice == '4':
            print("Exiting the Address Book System.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
