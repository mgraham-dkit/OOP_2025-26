from customers import Customer


def create_customer(customers: dict[str, Customer]) -> Customer:
    print("Creating new customer: ")
    available = False
    while not available:
        new_username = input("Username: ")
        if new_username.lower() in customers:
            print(f"Username \"{new_username}\" taken, please enter new username")
        else:
            available = True

    matching = False
    while not matching:
        valid = False
        while not valid:
            display_password_requirements()
            password = input("Password: ")
            if not Customer.validate_password(password):
                print("Invalid password entered, please try again.")
            else:
                valid = True

        duplicate = input("Enter password again:")
        if not password == duplicate:
            print("Passwords do not match. Please try again.")
        else:
            matching = True


    valid_email = False
    while not valid_email:
        email = input("Email: ")
        if not Customer.validate_email(email):
            print("Invalid email address. Try again.")
        else:
            valid_email = True

    new_customer = Customer(new_username.lower(), password, email.lower())
    return new_customer


def display_password_requirements():
    print("Password must: ")
    print("\tBe at least 8 characters long")
    print("\tContain at least 1 uppercase")
    print("\tContain at least 1 lowercase")
    print("\tContain at least 1 digit")


# Create set of customers to work with
cust1 = Customer("michelle", "password", "michelle@password")
cust2 = Customer("hermione", "Wing4rdium", "hermione_email")
cust3 = Customer("shorty", "SuperS3cur3", "short@accepted.com")
cust4 = Customer("valid_username", "Valid passw0rd", "valid_email@emaildomain.com")
cust5 = Customer("michelle", "Valid passw0rd", "valid_email@emaildomain.com")
cust_list = [cust1, cust2, cust3, cust4, cust5]

# Create dictionary for overall storage
customers = {}

# Populate dictionary - do not add customers with duplicate usernames
print()
print("Now populating customer dataset")
print("-" * 20)
for cust in cust_list:
    if cust.username() not in customers:
        customers[cust.username()] = cust
    else:
        print(f"{cust.username()} cannot be added to the system as the username already exists")
        print(f"\tExisting user details: {customers[cust.username()]}")
        print(f"\tThis user's details: {cust}")
print("-" * 20)

print()
print("Final Customer dataset:")
for i, username in enumerate(customers, start=1):
    print(f"{i}) {username}")

new_cust = create_customer(customers)
print(new_cust)