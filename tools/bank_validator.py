import re


def name_validator(name):
    if not (type(name) == str and re.match(r"^[a-zA-Z\s]{2,20}$", name)):
        raise ValueError("Invalid Name !!!")
    else:
        return name

def account_validator(account):
    if not (type(account) == str and re.match(r"^[a-zA-Z\s]{2,20}$", account)):
        raise ValueError("Invalid Account !!!")
    else:
        return account

def balance_validator(balance):
    if not (type(balance) == int and balance > 0):
        raise ValueError(f"Invalid Balance !!!")
    else:
        return balance


def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z\s]*$", description)):
        raise ValueError("Invalid Description !!!")
    else:
        return description