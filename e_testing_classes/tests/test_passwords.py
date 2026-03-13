import pytest

from e_testing_classes import passwords

def test_validate_password_valid_password():
    password = "Hi there1!"
    result = passwords.validate_password(password)

    assert result is passwords.SUCCESS

def test_validate_password_none():
    password = None
    result = passwords.validate_password(password)

    assert result is passwords.NONE_FAIL


def test_validate_password_too_short():
    password = "hi"
    result = passwords.validate_password(password)

    assert result is passwords.LENGTH_FAIL

def test_validate_password_lowercase():
    password = "HI THERE1!"
    result = passwords.validate_password(password)

    assert result is passwords.LOWERCASE_FAIL

def test_validate_password_uppercase():
    password = "hi there1!"
    result = passwords.validate_password(password)

    assert result is passwords.UPPERCASE_FAIL

def test_validate_password_digit():
    password = "Hi there!"
    result = passwords.validate_password(password)

    assert result is passwords.DIGIT_FAIL

def test_validate_password_special():
    password = "Hi there1"
    result = passwords.validate_password(password)

    assert result is passwords.SPECIAL_FAIL

# Parameterised version:
@pytest.mark.parametrize("password, expected_status", [
    ("Hi there1!", passwords.SUCCESS),
    (None, passwords.NONE_FAIL),
    ("hi", passwords.LENGTH_FAIL),
    ("HI THERE1!", passwords.LOWERCASE_FAIL),
    ("hi there1!", passwords.UPPERCASE_FAIL),
    ("Hi there!", passwords.DIGIT_FAIL),
    ("Hi there1", passwords.SPECIAL_FAIL)
])
def test_validate_password_all_cases(password, expected_status):
    result = passwords.validate_password(password)

    assert result is expected_status