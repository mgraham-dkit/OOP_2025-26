import re

'''
    [a-z]     : at least one lowercase
    [A-Z]     : at least one uppercase
    \\d        : at least one digit
    [^\\w\\s]   : at least one special character
'''

# Module-level constants to indicate status codes
SUCCESS = 0
NONE_FAIL = 1
LENGTH_FAIL = 2
LOWERCASE_FAIL = 3
UPPERCASE_FAIL = 4
DIGIT_FAIL = 5
SPECIAL_FAIL = 6

# Module-level constant dictionary mapping status codes to descriptions
REQUIREMENTS = {
    SUCCESS: "Valid password",
    NONE_FAIL: "No password supplied",
    LENGTH_FAIL: "Password too short",
    LOWERCASE_FAIL: "No lowercase letter included",
    UPPERCASE_FAIL: "No uppercase letter included",
    DIGIT_FAIL: "No digit included",
    SPECIAL_FAIL: "No special character included"
}

def validate_password(password: str) -> int:
    if not password:
        return NONE_FAIL

    if len(password) < 8:
        return LENGTH_FAIL

    if not re.search(r"[a-z]", password):
        return LOWERCASE_FAIL

    if not re.search(r"[A-Z]", password):
        return UPPERCASE_FAIL

    if not re.search(r"\d", password):
        return DIGIT_FAIL

    if not re.search(r"[^\w\s]", password):
        return SPECIAL_FAIL

    return SUCCESS


# Define a custom exception for use to mark password issues
class PasswordError(ValueError):
    pass


if __name__ == "__main__":
    validated = False
    while not validated:
        user_password = input("Please enter password: ")
        password_status = validate_password(user_password)
        if password_status != SUCCESS:
            print(f"Invalid password: {REQUIREMENTS[password_status]}")
            print("-"*20)
        else:
            validated = True
            print("Password accepted.")