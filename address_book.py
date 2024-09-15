'''

@Author: Venkatesh 
@Date: 2024-09-09 18:00:30 
@Last Modified by: Venkatesh 
@Last Modified time: 2024-09-06
18:00:30 
@Title : Programs on Addressbook 

''' 


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
        '''
           Description: 
                   this function is displaying the details 
           Parameters: 
                   None
           Return: 
                   None
        '''
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
    
    def validate_phone_number(self,phone_number):
        '''
           Description: 
                   this function validate the phone number having 10 number or not 
           Parameters: 
                   phone_number: phone number digits
           Return: 
                   Returns the true or false
        '''
        if re.match(r'\d{10}',phone_number):
            return True
        else:
            return False
        
    def validate_zip_code(self,zip_code):
        '''
           Description: 
                   this function validate the zip code having 6 number or not 
           Parameters: 
                   zip_code: code 
           Return: 
                   Return the True or False
        '''
        if re.match(r'\d{6}',zip_code):
            return True
        else:
            return False
        
    def validate_email(self,email):

        '''
           Description: 
                   this function validate the email having proper formate or not
           Parameters: 
                   eamil: email
           Return: 
                   Return the True or False
        '''
        if re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$',email):
            return True
        else:
            return False

    def add_contact(self, contact):
        '''
            Description: 
                   this function Adds a new contact to the address book.
            Parameters: 
                   contact: Contact object to add.
            Return: 
                   None
        '''
        for existing_contact in self.contacts_list:
            if existing_contact.first_name == contact.first_name and existing_contact.last_name == contact.last_name:
                print(f"Contact {contact.first_name} {contact.last_name} already exists.\n")
                logger_init("UC-7").info("This name already exists in contacts.")
                return
            
        if not self.validate_phone_number(contact.phone_number):
            print("Invalid phone number! It must contain exactly 10 digits.\n")
            logger_init("UC-2").info("Invalid phone number.")
            return

        # Validate zip code
        if not self.validate_zip_code(contact.zip_code):
            print("Invalid zip code! It must contain exactly 6 digits.\n")
            logger_init("UC-2").info("Invalid zip code.")
            return

        # Validate email
        if not self.validate_email(contact.email):
            print("Invalid email format! It should follow the format abc@example.com.\n")
            logger_init("UC-2").info("Invalid email format.")
            return


        self.contacts_list.append(contact)
        print(f"Contact for {contact.first_name} {contact.last_name} added successfully.\n")
        logger_init("UC-2").info("Added contact successfully.")

    def display_all_contacts(self):
        '''
        Description: 
            Displays all contacts in the address book.
        Parameters: 
            None
        Return: 
            None
        '''
        if not self.contacts_list:
            print("Address Book is empty.\n")
        else:
            for contact in self.contacts_list:
                contact.display()

    def edit_existing_contact(self):
        '''
        Description: 
               this function editing alreaady existing contacts using name
        Parameters: 
               None
        Return: 
               None
        '''
        name=input("Enter first name of the contacts to edit: ")
        contacts_to_edit = [contact for contact in self.contacts_list if contact.first_name == name]

        if not contacts_to_edit:
            print("no name in contact to edit")
            logger_init("UC-3").info("ther is no name in contact to edit")
            return
        
        print(f"Found {len(contacts_to_edit)} contact(s):")
        for i, contact in enumerate(contacts_to_edit, start=1):
            print(f"{i}. {contact.first_name} {contact.last_name}")
            contact.display()

        
        if len(contacts_to_edit) > 1:
            selection = int(input("Select the contact number you want to edit: "))
            selected_contact = contacts_to_edit[selection]
        else:
            selected_contact = contacts_to_edit[0]

        
        print("\nWhat would you like to edit?\n",
              "1. First Name\n",
              "2. Last Name\n",
              "3. Address\n",
              "4. City\n",
              "5. State\n"
              "6. Zip Code\n"
              "7. Phone Number\n",
              "8. Email")

        option = input("Enter the number corresponding to the field you want to edit: ")

        if option == '1':
            selected_contact.first_name = input("Enter new first name: ")
        elif option == '2':
            selected_contact.last_name = input("Enter new last name: ")
        elif option == '3':
            selected_contact.address = input("Enter new address: ")
        elif option == '4':
            selected_contact.city = input("Enter new city: ")
        elif option == '5':
            selected_contact.state = input("Enter new state: ")
        elif option == '6':
            selected_contact.zip_code = input("Enter new zip code: ")
        elif option == '7':
            selected_contact.phone_number = input("Enter new phone number: ")
        elif option == '8':
            selected_contact.email = input("Enter new email: ")
        else:
            print("Invalid choice. No changes were made.")
        
        print("Contact updated successfully.\n")
        logger_init("UC-3").info("Contact update succussfully")

    
    def delete_person_from_contacts(self):
        '''
        Description: 
                  this function deleting alreaady existing contacts using name
        Parameters: 
                 None
        Return: 
                 None
        '''
        name=input("Enter first name of the contacts to edit: ")
        contacts_to_delete = [contact for contact in self.contacts_list if contact.first_name == name]

        if not contacts_to_delete:
            print("no name in contact to delete from contacts")
            logger_init("UC-4").info("There is no name in contact to delete from contacts ")
            return
        
        print(f"Found {len(contacts_to_delete)} contact(s):")
        for i, contact in enumerate(contacts_to_delete, start=1):
            print(f"{i}. {contact.first_name} {contact.last_name}")
            contact.display()

        
        if len(contacts_to_delete) > 1:
            selection = int(input("Select the contact number you want to delete: ")) - 1
            selected_contact = contacts_to_delete[selection]
        else:
            selected_contact = contacts_to_delete[0]

        
        self.contacts_list.remove(selected_contact)
        print(f"Contact {selected_contact.first_name} {selected_contact.last_name} deleted successfully.\n")
        logger_init("UC-4").info(" selected contact deleted successfully.")


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
    
    def count_by_city_or_state(self, city=None, state=None):
        '''
        Description:
            This function returns the count of contacts by city or state in an address book.
        Parameters:
            city: City name to count (optional)
            state: State name to count (optional)
        Return:
            Count of contacts by city or state.
        '''
        count = 0
        for contact in self.contacts_list:
            if (city and contact.city.lower() == city.lower()) or (state and contact.state.lower() == state.lower()):
                count += 1
        return count
    
    def sort_entries_by_name(self):
        '''
        Description:
            this function Sorts the contact list alphabetically by first name and last name.
        Parameters:
            None
        Return:
            None
        '''
        self.contacts_list = sorted(self.contacts_list, key=lambda contact: (contact.first_name.lower(), contact.last_name.lower()))
        print("Contacts sorted alphabetically by name")
        logger_init("UC-11").info("sorted alphabetically by name")
        self.display_all_contacts()


class System:
    def __init__(self):
        self.address_books = {}

    def add_address_book(self, name):
        '''
            Description: 
                   this function Adds a new address book with a unique name
            Parameters: 
                   name: name of the new address book
            Return: 
                   None
        '''
        if name in self.address_books:
            print(f"Address Book '{name}' already exists.\n")
            logger_init("UC-6").info("This address book name already exists.")
        else:
            self.address_books[name] = AddressBook()
            print(f"Address Book '{name}' created successfully.\n")
            logger_init("UC-6").info("Address book created successfully.")


    def select_address_book(self):
        '''
            Description: 
                   this function is selecting an address book by name
            Parameters: 
                   None
            Return: 
                   Returns the addres book or if it is not in return None
        '''
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
        city_count=0
        state_count=0
        for book_name, address_book in self.address_books.items():
            results = address_book.search_contact_by_city_or_state(city, state)
            if results:
                all_results.extend([(book_name, contact) for contact in results])
                if city:
                    city_count += address_book.count_by_city_or_state(city=city)
                if state:
                    state_count += address_book.count_by_city_or_state(state=state)

        if not all_results:
            print(f"No contacts found in city '{city}' or state '{state}'.\n")
            logger_init("UC-8").info("No contacts found in city or state name")

        else:
            print(f"Found {len(all_results)} contact(s) in city '{city}' or state '{state}':")
            if city:
                print(f"Total contacts by city '{city}': {city_count}")
                logger_init("UC-10").info(f"Total contacts by city '{city}': {city_count}")
            if state:
                print(f"Total contacts by state '{state}': {state_count}")
                logger_init("UC-10").info(f"Total contacts by state '{state}': {state_count}")
            
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
                          "3. Edit Existing Contact\n",
                          "4. Delete Contact\n",
                          "5. Sort by names all entries\n",
                          "6. Back to Main Menu")

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
                        selected_address_book.edit_existing_contact()

                    elif sub_choice == '4':
                        selected_address_book.delete_person_from_contacts()

                    elif sub_choice == '5':
                        selected_address_book.sort_entries_by_name()

                    elif sub_choice == '6':
                        break

                    else:
                        print("Invalid choice, please try again.")

        elif choice == '3':
            city = input("Enter city to search : ")
            state = input("Enter state to search : ")

            system.search_across_address_books(city=city or None, state=state or None)

        elif choice == '4':
            print("Exiting the Address Book System.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
