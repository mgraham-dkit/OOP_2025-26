contacts = {
    "Ann" : 871234567,
    "Barry" : 867654321,
    "Celine" : 852468101
}

name = input(f"Please enter the contact's name: ")
number = contacts.get(name)
print(f"{name} : {number}")

new_contact_name = input("Please enter the new name to be added: ")
new_contact_num = int(input(f"Please enter {new_contact_name}'s number: "))

if contacts.get(new_contact_name) is None:
    contacts[new_contact_name] = new_contact_num
else:
    print("Contact already exists!")

print(contacts)