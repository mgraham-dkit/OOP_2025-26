class User:
    def __init__(self, username, password):
        if not username:
            print("Username cannot be blank!")

        self._username = username

        self.validate_password(password)
        self._password = password

    @staticmethod
    def validate_password(password):
        if len(password) < 8:
            print("Password must contain at least 8 characters")
            return False

        if not any(char.isdigit() for char in password):
            print("Password must contain at least one digit!")
            return False

        if not any(char.isupper() for char in password):
            print("Password must contain at least one uppercase!")
            return False

        if not any(char.islower() for char in password):
            print("Password must contain at least one lower!")
            return False

        return True


    def change_password(self, old_pass, new_pass):
        if old_pass != self._password:
            return False

        if not User.validate_password(new_pass):
            return False

        self._password = new_pass
        return True

    def check_credentials(self, password):
        if self._password == password:
            return True

        return False

    def __str__(self):
        return f"Username: {self._username}"

    def __repr__(self):
        return f"{self.__class__.__name__}[_username={self._username}, _password=********]"

    def get_username(self):
        return self._username

    def __eq__(self, other):
        if not other:
            return False

        return self._username.tolower() == other.get_username().tolower()


    def __ne__(self, other):
        if self == other:
            return False
        else:
            return True
