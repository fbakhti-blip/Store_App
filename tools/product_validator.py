import re
from datetime import datetime


def name_validator(name):
    if not (isinstance(name, str) and re.match(r"^[a-zA-Z0-9\s]{3,30}$", name)):
        raise ValueError("Invalid name !!!")
    else:
        return name


def brand_validator(brand):
    if not (isinstance(brand, str) and re.match(r"^[a-zA-Z0-9\s]{1,30}$", brand)):
        raise ValueError("Invalid brand !!!")
    else:
        return brand


def model_validator(model):
    if not (isinstance(model, str) and re.match(r"^[a-zA-Z0-9\s]{3,30}$", model)):
        raise ValueError("Invalid model !!!")
    else:
        return model


def serial_validator(serial):
    if not (isinstance(serial, str) and re.match(r"^[a-zA-Z0-9\s]{3,30}$", serial)):
        raise ValueError("Invalid serial !!!")
    else:
        return serial


def category_validator(category):
    if not (isinstance(category, str) and re.match(r"^[\w\s]{3,30}$", category)):
        raise ValueError("Invalid category !!!")
    else:
        return category


def unit_validator(unit):
    if not (isinstance(unit, str) and re.match(r"^[\w\s]{1,10}$", unit)):
        raise ValueError("Invalid unit !!!")
    else:
        return unit


def expiration_date_validator(expiration_date):
    # if not (isinstance(expiration_date, str) and re.match(r"^\d{4}-\d{2}-\d{2}$", expiration_date)):
    if not datetime.strptime(expiration_date, "%Y/%m/%d"):
        raise ValueError("Invalid date time format !!!")
    else:
        return expiration_date
