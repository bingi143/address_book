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


def main():
    print("Welcome to address book program")
    first_name=input("Enter first name:")
    last_name=input("Enter last name:")
    address=input("Enter address:")
    city=input("Enter city:")
    state=input("Enter state:")
    zip_code=int(input("Enter zip-code:"))
    phone_number=int(input("Enter phone number:"))
    email=input("Enter email:")
    person_1=Contacts(first_name,last_name,address,city,state,zip_code,phone_number,email)
    person_1.display()


if __name__=="__main__":
    main()