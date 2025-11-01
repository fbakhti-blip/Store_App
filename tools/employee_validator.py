import re


def first_name_validator(first_name):
    if not (isinstance(first_name, str) and re.match(r"^[a-zA-Z\s]{2,20}$", first_name)):
        raise ValueError("Invalid first_name !!!")
    else:
        return first_name


def last_name_validator(last_name):
    if not (isinstance(last_name, str) and re.match(r"^[a-zA-Z\s]{2,20}$", last_name)):
        raise ValueError("Invalid last_name !!!")
    else:
        return last_name


def salary_validator(salary):
    if not (isinstance(salary, int) and salary > 0):
        raise ValueError("Invalid salary !!!")
    else:
        return salary


def phone_number_validator(phone_number):
    if not (isinstance(phone_number, str) and re.match(r"^[0-9]{7,14}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number


def role_validator(role):
    if not (isinstance(role, str) and re.match(r"^(manager|cashier|storekeeper|sale)$", role)):
        raise ValueError("Invalid role !!!")
    else:
        return role


def occupation_validator(occupation):
    if not (isinstance(occupation, str) and re.match(r"^(manager|cashier|storekeeper|sale)$", occupation)):
        raise ValueError("Invalid occupation !!!")
    else:
        return occupation


def username_validator(username):
    if not (isinstance(username, str) and re.match(r"^[a-zA-Z0-9]{3,30}$", username)):
        raise ValueError("Invalid username !!!")
    else:
        return username


def password_validator(password):
    if not (isinstance(password, str) and re.match(r"^[a-zA-Z0-9@#$%^&+=]{8,20}$", password)):
        raise ValueError("Invalid password !!!")
    else:
        return password
