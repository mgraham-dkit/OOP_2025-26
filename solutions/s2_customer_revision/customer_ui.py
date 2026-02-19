from customers import Customer


def create_customer(customers_dict: dict[str, Customer]) -> str | None:
    print("Creating new customer: ")
    new_username = handle_username_entry(customers_dict)
    password = handle_password_entry()
    email = handle_email_entry()

    new_customer = Customer(new_username.lower(), password, email.lower())
    if new_customer.username() in customers_dict:
        print("Username not available. Please try again.")
        return None
    else:
        customers_dict[new_customer.username()] = new_customer
        return new_customer.username()


def handle_email_entry() -> str:
    valid_email = False
    while not valid_email:
        email = input("Email: ")
        if not Customer.validate_email(email):
            print("Invalid email address. Try again.")
        else:
            valid_email = True
    return email


def display_password_requirements():
    print("Password must: ")
    print("\tBe at least 8 characters long")
    print("\tContain at least 1 uppercase")
    print("\tContain at least 1 lowercase")
    print("\tContain at least 1 digit")


def handle_password_entry() -> str:
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
    return password


def handle_username_entry(customers_dict: dict[str, Customer]) -> str:
    available = False
    while not available:
        new_username = input("Username: ")
        if new_username.lower() in customers_dict:
            print(f"Username \"{new_username}\" taken, please enter new username")
        else:
            available = True
    return new_username


def login_customer(customers_dict: dict[str, Customer]) -> str | None:
    username_attempt = input("Enter username: ").lower()
    password = input("Enter password: ")

    if username_attempt in customers_dict:
        user = customers_dict[username_attempt]
        if user.check_password(password):
            return username_attempt

    print("Login failed - no such username/password")
    return None


def populate_customer_dataset(customers_dict: dict[str, Customer]) -> None:
    # Create set of customers to work with
    cust1 = Customer("michelle", "password", "michelle@password")
    cust2 = Customer("hermione", "Wing4rdium", "hermione_email")
    cust3 = Customer("shorty", "SuperS3cur3", "short@accepted.com")
    cust4 = Customer("valid_username", "Valid passw0rd", "valid_email@emaildomain.com")
    cust5 = Customer("michelle", "Valid passw0rd", "valid_email@emaildomain.com")
    cust_list = [cust1, cust2, cust3, cust4, cust5]
    # Populate dictionary - do not add customers with duplicate usernames
    print()
    print("Now populating customer dataset")
    print("-" * 20)
    for cust in cust_list:
        if cust.username() not in customers_dict:
            customers_dict[cust.username()] = cust
        else:
            print(f"{cust.username()} cannot be added to the system as the username already exists")
            print(f"\tExisting user details: {customers_dict[cust.username()]}")
            print(f"\tThis user's details: {cust}")
    print("-" * 20)


# Create dictionary for overall storage
customers = {}
populate_customer_dataset(customers)

print()
print("Final Customer dataset:")
for i, username in enumerate(customers, start=1):
    print(f"{i}) {username}")


logged_in_user = None
exit_request = False
while not exit_request:
    if not logged_in_user:
        print("Please choose from the following options:")
        print("1) Register a new customer")
        print("2) Login")
        print("Exit to exit the system")

        choice = input("Enter choice: ")
        match(choice.lower()):
            case "1":
                logged_in_user = create_customer(customers)
            case "2":
                logged_in_user = login_customer(customers)
                pass
            case "exit":
                exit_request = True
                logged_in_user = None
                continue
            case _:
                print("Please choose one of the specified options")

    if logged_in_user:
        print("You are now logged in!")
