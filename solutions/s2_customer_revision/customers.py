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

        upper_check = any((c.isupper() for c in password))
        if not upper_check:
            print("No uppercase letter included")
            return False

        lower_check = any((c.islower() for c in password))
        if not lower_check:
            print("No lowercase letter included")
            return False

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


if __name__ == "__main__":
    cust1 = Customer("michelle", "password", "michelle@password")