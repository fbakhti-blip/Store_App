import re


def name_validator(name):
    if not (isinstance(name, str) and re.match(r"^[a-zA-Z\s]{2,20}$", name)):
        raise ValueError("Invalid Name !!!")
    else:
        return name


def balance_validator(balance):
    if not (isinstance(balance, (int, float)) and balance > 0):
        raise ValueError(f"Invalid Balance !!!")
    else:
        return balance


def description_validator(description):
    if not (isinstance(description, str) and re.match(r"^[\w\s.,;:-]*$", description)):
        raise ValueError("Invalid Description !!!")
    else:
        return description
