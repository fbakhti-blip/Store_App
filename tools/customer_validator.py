import re


def first_name_validator(first_name):
    if not (isinstance(first_name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", first_name)):
        raise ValueError("Invalid first_name !!!")
    else:
        return first_name


def last_name_validator(last_name):
    if not (isinstance(last_name, str) and re.match(r"^[a-zA-Z\s]{3,30}$", last_name)):
        raise ValueError("Invalid last_name !!!")
    else:
        return last_name


def phone_number_validator(phone_number):
    if not (isinstance(phone_number, str) and re.match(r"^(09|\+989)\d{9}$", phone_number)):
        raise ValueError("Invalid phone_number !!!")
    else:
        return phone_number


def address_validator(address):
    if not (isinstance(address, str) and re.match(r"^[\w,\-]{3,100}$", address)):
        raise ValueError("Invalid address !!!")
    else:
        return address
