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

    def __init__(self,first_name,last_name,address,city,state,zip_code,phone_number,email):
        self.first_name=first_name
        self.last_name=last_name
        self.address=address
        self.city=city
        self.state=state
        self.zip_code=zip_code
        self.phone_number=phone_number
        self.email=email

    def display(self):
        '''
          Description: 
                this function is dispaying contact all the details
          Parameters: 
                None
          Return : 
                None
        '''
        print("****************************\n",
              f" first-name: {self.first_name}\n",
              f" last-name: {self.last_name}\n",
              f" address: {self.address}\n", 
              f" city: {self.city}\n ",
              f" state: {self.state}\n",
              f" zip-code: {self.zip_code}\n ",
              f" phone-number: {self.phone_number}\n ",
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
                logger_init("UC-2").info(f"Contact {contact.first_name} {contact.last_name} already exists.")
                return
            
        if not self.validate_phone_number(contact.phone_number):
            print("Invalid phone number! It must contain exactly 10 digits.\n")
            logger_init("UC-2").error("Invalid phone number.")
            return

        # Validate zip code
        if not self.validate_zip_code(contact.zip_code):
            print("Invalid zip code! It must contain exactly 6 digits.\n")
            logger_init("UC-2").error("Invalid zip code.")
            return

        # Validate email
        if not self.validate_email(contact.email):
            print("Invalid email format! It should follow the format abc@example.com.\n")
            logger_init("UC-2").error("Invalid email format.")
            return

            

        self.contacts_list.append(contact)
        print(f"Contact for {contact.first_name} {contact.last_name} added successfully.\n")
        logger_init("UC-2").info("added contact successfully")


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
        logger_init("UC-4").info(f"Contact {selected_contact.first_name} {selected_contact.last_name} deleted successfully.\n")


def main():

    print("Welcome to the Address Book Program")
    address_book = AddressBook()

    while True:
        print("1. Add New Contact\n",
              "2. Display All Contacts\n",
              "3. Edit existing contact\n",
              "4. Delete person from contacts\n",
              "5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input("Enter address: ")
            city = input("Enter city: ")
            state = input("Enter state: ")
            zip_code = input("Enter zip code: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")

            new_contact = Contacts(first_name, last_name, address, city, state, zip_code, phone_number, email)
            address_book.add_contact(new_contact)

        elif choice == '2':
            address_book.display_all_contacts()

        elif choice=='3':
            address_book.edit_existing_contact()

        elif choice=='4':
            address_book.delete_person_from_contacts()

        elif choice == '5':
            print("Exiting Address Book.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__=="__main__":
    main()