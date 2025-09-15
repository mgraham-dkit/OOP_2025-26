contacts = {
    "Ann" : 871234567,
    "Barry" : 867654321,
    "Celine" : 852468101
}

name = input(f"Please enter the contact's name: ")
number = contacts.get(name)
print(f"{name} : {number}")

finished = False
while not finished:
    new_contact_name = input("Please enter the new name to be added: ")
    new_contact_num = int(input(f"Please enter {new_contact_name}'s number: "))

    if contacts.get(new_contact_name) is None:
        contacts[new_contact_name] = new_contact_num
        finished = True
    else:
        print(f"Contact already exists! {new_contact_name} : {contacts[new_contact_name]}")
        choice = input("Do you wish to try again??? (y to continue, any other key to end)")
        if choice != "y" and choice != "Y":
            finished = True

print(contacts)