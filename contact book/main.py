import sys

contact = {
    "marvin": "0164193317",
    "divya": "0164642422",
    "dad": "0166446261"
}

while True:
    print("\nwhat do u want to do?\n1. search contact\n2. add contact\n3. delete contact\n4. update a contact\n5. view contact list\n6. exit program\n")
    action = input("enter an action: ")
    
    # search for a contact
    if action == "1":
        search_contact = input("\ntype in a name to search: ")
        if search_contact in contact:
            print("\nfound contact!")
            print(f"contact name: {search_contact}, contact number: {contact[search_contact]}")
        else: 
            print("contact unavailable!")
    # add a contact
    elif action == "2":
        add_contact_name = input("\ntype in new contact name: ")
        add_contact_number = input("type in new contact number: ")

        contact[add_contact_name] = add_contact_number
        print("\nnew contact has been added into contact list!")

    # delete a contact
    elif action == "3":
        remove_contact = input("\ntype in a contact name to remove: ")
        contact.pop(remove_contact)
    
    # update a contact
    elif action == "4":
        update_contact = input("\ntype in a contact name to update: ")
        new_num = input(f"type in new number for {update_contact}: ")
        contact[update_contact] = new_num
    
    # display all contacts
    elif action == "5":
        print("\n== CONTACT LIST ==\n")
        print("NAME\tNUMBER")
        for key, value in contact.items():
            print(f"{key}\t{value}")
    
    # exit program
    elif action == "6":
        sys.exit()
    
    # invalid choice
    else:
        print("only select from the choices listed.")