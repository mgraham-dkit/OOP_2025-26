from types import NotImplementedType


class Customer:
    def __init__(self, username: str, password: str, email:str):
        if not Customer.validate_username(username):
            print("Supplied username is invalid")
        self._username = username

        if not Customer.validate_password(password):
            print("Password does not meet requirements")
        self.__password = password

        if not Customer.validate_email(email):
            print("Supplied email is invalid")
        self._email = email

    # Getter methods so we can see the encapsulated information outside this class
    # No getter for password as it's sensitive information!
    def username(self) -> str:
        return self._username

    def email(self) -> str:
        return self._email

    # Validator methods
    @staticmethod
    def validate_username(username: str) -> bool:
        if username is None:
            return False

        if len(username.strip()) < 8:
            return False

        return True

    @staticmethod
    def validate_password(password: str) -> bool:
        if password is None:
            return False

        if len(password) < 8:
            return False

        # Check each character in password for uppercase status - true if there is any appearance of uppercase
        upper_check = any((c.isupper() for c in password))
        if not upper_check:
            print("No uppercase letter included")
            return False

        # Check each character in password for lowercase status - true if there is any appearance of lowercase
        lower_check = any((c.islower() for c in password))
        if not lower_check:
            print("No lowercase letter included")
            return False

        # Check each character in password for digit status - true if there is any digit appears
        digit_check = any((c.isdigit() for c in password))
        if not digit_check:
            print("No digit included")
            return False

        return True

    @staticmethod
    def validate_email(email: str) -> bool:
        if email is None:
            return False

        if "@" not in email:
            return False

        return True

    # Text representation
    def __str__(self) -> str:
        return f"Username: {self._username} - {self._email}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}[_username={self._username}, __password=\"********\", _email={self._email}]"

    # Equality comparison
    def __eq__(self, other: object) -> bool | NotImplementedType:
        # Confirm other is the right type, return NotImplemented if not
        # If we don't know how to compare to other's type, let other try
        if not isinstance(other, Customer):
            return NotImplemented

        # username is identifying attribute
        return self._username == other._username

    def __ne__(self, other: object) -> bool | NotImplementedType:
        if not isinstance(other, Customer):
            return NotImplemented

        # Use eq logic to check for equality; flip result to get not equal
        return not self == other

if __name__ == "__main__":
    print("Creating cust 1 (bad password)")
    cust1 = Customer("michelle", "password", "michelle@password")
    print(f"cust1: {cust1}")
    print(f"repr for cust1: {repr(cust1)}")
    print("")

    print("Creating cust2 (bad email)")
    cust2 = Customer("hermione", "Wing4rdium", "hermione_email")
    print(f"cust2: {cust2}")
    print(f"repr for cust2: {repr(cust2)}")
    print("")

    print("Creating cust3 (bad username)")
    cust3 = Customer("shorty", "SuperS3cur3", "short@accepted.com")
    print(f"cust3: {cust3}")
    print(f"repr for cust3: {repr(cust3)}")
    print("")

    print("Creating cust4 (All good!)")
    cust4 = Customer("valid_username", "Valid passw0rd", "valid_email@emaildomain.com")
    print(f"cust4: {cust4}")
    print(f"repr for cust4: {repr(cust4)}")
    print("")

    print("Creating cust5 (Values are valid, same username as cust1)")
    cust5 = Customer("michelle", "Valid passw0rd", "valid_email@emaildomain.com")
    print(f"cust5: {cust5}")
    print(f"repr for cust5: {repr(cust5)}")
    print("")


    if cust1 != cust2:
        print(f"cust1 and cust2 have different usernames (cust1: {cust1.username()}, cust2: {cust2.username()}), "
              f"therefore can't be the same user")
    else:
        print("cust1 and cust2 have the same username - this shouldn't have happened!")

    if cust1 == cust5:
        print(f"cust1 and cust5 have the same username (cust1: {cust1.username()}, cust5: {cust5.username()}), "
              f"therefore are considered the same entity")
    else:
        print("cust1 and cust5 have different usernames - this shouldn't have happened!")