# UPDATED CODE

def add_contact(name_list, phone_num_list, mini_address_book):
    # validating number of contacts to add
    while True:
        try:
            num = int(input("Enter the number of contacts you want to enter: "))
            if num <= 0:
                print("Please enter a positive number.")
                continue
            break
        except ValueError:
            print("Please enter the number correctly (digits only).")

    for _ in range(num):
        name = input("Enter a contact name: ")
        if name.lower() in [n.lower() for n in mini_address_book]:
            print(f"{name} already exists in your address book!")
            continue
        phone_num = input("Enter a contact number: ")
        name_list.append(name)
        phone_num_list.append(phone_num)
        mini_address_book[name] = phone_num
        print(f"{name}'s contact added successfully!")


def search_contact(mini_address_book):
    print("\n***** Searching Contact *****\n")
    search_contact = input('Enter a name to search: ')
    for key in mini_address_book:
        if key.lower() == search_contact.lower():
            print(f"\nContact number of {key}: {mini_address_book[key]}")
            return
    print(f"\nNo contact exists with the name {search_contact}")


def delete_contact(mini_address_book, name_list, phone_num_list):
    print("\n***** Delete Contact *****\n")
    delete_name = input('Enter a name to delete: ')
    for key in list(mini_address_book.keys()):
        if key.lower() == delete_name.lower():
            mini_address_book.pop(key)
            if key in name_list:
                idx = name_list.index(key)
                name_list.pop(idx)
                phone_num_list.pop(idx)
            print(f"\n{key}'s contact has been deleted.")
            return
    print(f"\nNo contact exists with the name {delete_name}")


def list_all_contacts(mini_address_book):
    print("\n***** Listing All Contacts *****\n")
    if not mini_address_book:
        print("No contacts to display.")
    else:
        for key, value in mini_address_book.items():
            print(f"Name: {key} | Contact Number: {value}")


def main():
    mini_address_book = {}
    name_list = []
    phone_num_list = []

    while True:
        print("*" * 70)
        print("\nMINI ADDRESS BOOK | CHOOSE AN OPTION")
        print('1- Add a new contact')
        print('2- Search for a contact')
        print('3- Delete a contact')
        print('4- List all contacts')
        print('5- Exit\n')
        print("*" * 70)

        choice = input("Enter your choice: ")
        match choice:
            case '1':
                add_contact(name_list, phone_num_list, mini_address_book)
            case '2':
                search_contact(mini_address_book)
            case '3':
                delete_contact(mini_address_book, name_list, phone_num_list)
            case '4':
                list_all_contacts(mini_address_book)
            case '5':
                print("Exiting... Goodbye!")
                break
            case _:
                print("Invalid Choice! Please try again.")


if __name__ == '__main__':
    main()





#previous code
# def add_contact(name_list, phone_num_list, mini_address_book):
#     #validating number
#     while True:
#         try:
#             num = int(input("Enter the number of contacts you want to enter: "))
#             if num <= 0:
#                 print("Please enter a positive number.")
#                 continue
#             break
#         except ValueError:
#             print("Please enter the number correctly (digits only).")


#     for i in range(num):
#         name = input("Enter a contact name: ")
#         phone_num = input("Enter a contact number: ")
#         name_list.append(name)
#         phone_num_list.append(phone_num)
#         mini_address_book[name] = phone_num

# #function for searching contact
# def search_contact(mini_address_book):
#     print("\n*****Searching Contact****\n")
#     search_contact = input('Enter a name to search the contact number: ')
#     if mini_address_book.get(search_contact):
#         result = mini_address_book.get(search_contact)
#         print(f"\nContact number of {search_contact}: {result}")
#     else:
#         print(f"\nNo contact exist of name {search_contact}")


# #function for deleting contact
# def delete_contact(mini_address_book, name_list, phone_num_list):
#     print("\n*****Delete Contact****\n")
#     delete_name = input('Enter a name to delete the contact number: ')
#     if mini_address_book.get(delete_name):
#         mini_address_book.pop(delete_name)
#         if delete_name in name_list:
#             idx = name_list.index(delete_name)
#             name_list.pop(idx)
#             phone_num_list.pop(idx)
#         print(f"\nDeleting the {delete_name}'s contact from the Address Book")
#     else:
#         print(f"\nNo contact exist of name {delete_contact}")

# #function for listing contact
# def list_all_contacts(name_list, phone_num_list, mini_address_book):
#     print("\n***** Listing All Contacts *****\n")
#     if not mini_address_book:
#         print("No contacts to display.")
#     else:
#         for key, value in mini_address_book.items():
#             print(f"Name: {key} | Contact Number: {value}")


# #main function
# def main():
#     mini_address_book = {}
#     name_list = []
#     phone_num_list = []
#     while True:

#         print("*" * 70)
#         print("\nMINI ADDRESS BOOK | CHOOSE AN OPTION")
#         print('1- Add a new contact')
#         print('2- Search for a contact')
#         print('3- Delete a contact')
#         print('4- List all contacts')
#         print('5- Exit\n')
#         print("*" * 70)
#         choice = input("Enter your choice: ")
#         match choice:
#             case '1':
#                 add_contact(name_list, phone_num_list, mini_address_book)
#             case '2':
#                 search_contact(mini_address_book)
#             case '3':
#                 delete_contact(mini_address_book, name_list, phone_num_list)
#             case '4':
#                 list_all_contacts(name_list, phone_num_list, mini_address_book)
#             case '5':
#                 break
#             case _:
#                 print("Invalid Choice")


# if __name__ == '__main__':
#     main()
