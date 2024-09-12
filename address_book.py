'''

@Author: Venkatesh 
@Date: 2024-09-09 18:00:30 
@Last Modified by: Venkatesh 
@Last Modified time: 2024-09-06
18:00:30 
@Title : Programs on Addressbook 

''' 


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

    def add_contact(self, contact):
        '''
        Description: 
            Adds a new contact to the address book.
        Parameters: 
            contact: Contact object to add.
        Return: 
            None
        '''
        self.contacts_list.append(contact)
        print(f"Contact for {contact.first_name} {contact.last_name} added successfully.\n")


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


def main():

    print("Welcome to the Address Book Program")
    address_book = AddressBook()

    while True:
        print("\n1. Add New Contact")
        print("2. Display All Contacts")
        print("3. Exit")

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

        elif choice == '3':
            print("Exiting Address Book.")
            break

        else:
            print("Invalid choice, please try again.")


if __name__=="__main__":
    main()