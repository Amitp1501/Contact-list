contacts = {}

def start():
    print("Welcome to Contact+ \n")
    name = input("Please enter your name: ")
    print("Hi {}, would you like to check your current contacts or make new ones?".format(name))
    print("To make new contacts, type 'New'")
    print("To check current contacts, type 'Contacts'")
    choice = input("Go to: ").lower()
    if choice == 'new':
        new_function()
    elif choice == 'contacts':
        contacts_function()
    elif choice == 'exit':
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")
        start()

def new_function():
    print("\nPlease input the name: ", end="")
    contact_name = input()
    
    while True:
        contact_number = input("Please input the number (10 digits): ")
        if contact_number.isdigit() and len(contact_number) == 10:
            break
        else:
            print("Invalid number. Please enter a 10-digit number.")

    contacts[contact_name] = contact_number
    print("Contact created\n")
    ask_for_action()

def contacts_function():
    if not contacts:
        print("You don't have any contacts yet.")
    else:
        print("\nYour contacts:")
        for name, number in contacts.items():
            print("Name:", name)
            print("Number:", number)
            print("-------------------")
    ask_for_action()

def ask_for_action():
    while True:
        choice = input("\nWould you like to make more contacts or check current contacts?\n"
                       "To make new contacts, type 'New'\n"
                       "To check current contacts, type 'Contacts'\n"
                       "To exit, type 'Exit'\n"
                       "Go to: ").lower()
        if choice == 'new':
            new_function()
        elif choice == 'contacts':
            contacts_function()
        elif choice == 'exit':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

start()
