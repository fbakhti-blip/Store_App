import re


def name_validator(name):
    if not (isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,20}$", name)):
        raise ValueError("Invalid Name !!!")
    else:
        return name


def description_validator(description):
    if not (isinstance(description, str) and re.match(r"^[a-zA-Z\s]*$", description)):
        raise ValueError("Invalid Description !!!")
    else:
        return description
