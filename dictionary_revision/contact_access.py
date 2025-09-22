def view_contact(contact_dict):
    name = input(f"Please enter the contact's name: ")
    number = contact_dict.get(name)
    print(f"{name} : {number}")

def add_contact(contact_dict):
    finished = False
    while not finished:
        new_contact_name = input("Please enter the new name to be added: ")
        new_contact_num = int(input(f"Please enter {new_contact_name}'s number: "))

        if contact_dict.get(new_contact_name) is None:
            contact_dict[new_contact_name] = new_contact_num
            finished = True
        else:
            print(f"Contact already exists! {new_contact_name} : {contact_dict[new_contact_name]}")
            choice = input("Do you wish to try again??? (y to continue, any other key to end)")
            if choice != "y" and choice != "Y":
                finished = True

def delete_contact(contact_dict):
    name = input("Please enter the name of the contact to be deleted: ")
    if contact_dict.get(name) is not None:
        choice = input("Do you wish to \n1) Wipe contact phone number\n2) Delete contact from contacts\n")
        if choice == "1":
            contact_dict[name] = None
        elif choice == "2":
            # contact_dict.pop(name)
            del contact_dict[name]
        else:
            print("Invalid option selected. Delete cannot be performed.")
    else:
        print("Contact name not found.")

def authenticate(users_dict, username, password):
    if username.lower() in users_dict:
        if users_dict[username] == password:
            return True

    return False


def authenticate_user(users_dict):
    not_authenticated = True
    while not_authenticated:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        if authenticate(users_dict, username, password):
            not_authenticated = False
        else:
            print("Invalid username/password. Please try again.")


if __name__ == "__main__":

    users = {
        "admin" : "root",
        "michelle" : "secret",
        "hannah" : "password123!"

    }
    contacts = {
        "Ann" : 871234567,
        "Barry" : 867654321,
        "Celine" : 852468101
    }

    authenticate_user(users)

    finished = False
    while not finished:
        print("1) View a contact")
        print("2) Add a new contact")
        print("3) Delete a contact")
        print("0) Exit")
        choice = input("Enter your selection:")

        match choice:
            case "1":
                view_contact(contacts)
            case "2":
                add_contact(contacts)
            case "3":
                delete_contact(contacts)
            case "0":
                finished = True
            case _ :
                print("Please choose a valid option")