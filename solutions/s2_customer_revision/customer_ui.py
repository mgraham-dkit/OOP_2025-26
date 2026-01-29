from customers import Customer


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