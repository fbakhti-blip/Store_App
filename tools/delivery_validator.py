import re

def first_name_validator(first_name):
    if not (type(first_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", first_name)):
        raise ValueError("Invalid first_name !!!")
    else:
        return first_name

def last_name_validator(last_name):
    if not (type(last_name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", last_name)):
        raise ValueError("Invalid last_name !!!")
    else:
        return last_name

def address_validator(address):
    if not (type(address) == str and re.match(r"^[\w,\-]{3,100}$", address)):
        raise ValueError("Invalid address !!!")
    else:
        return address

def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z\s]*$", description)):
        raise ValueError("Invalid description !!!")
    else:
        return description
