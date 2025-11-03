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

        if not password.isDigit():
            print("Password must contain at least one digit!")
            return False

        if not password.isUpper():
            print("Password must contain at least one uppercase!")
            return False

        if not password.isLower():
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

