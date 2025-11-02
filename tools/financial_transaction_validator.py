import re
from datetime import datetime


def customer_id_validator(customer_id):
    if not (type(customer_id) == int and customer_id > 0):
        raise ValueError("Invalid Customer Id !!!")
    else:
        return customer_id


def employee_id_validator(employee_id):
    if not (type(employee_id) == int and employee_id > 0):
        raise ValueError(f"Invalid Employee Id !!!")
    else:
        return employee_id


def amount_validator(amount):
    if not (type(amount) == int and amount > 0):
        raise ValueError("Invalid Amount !!!")
    else:
        return amount


def date_time_validator(date_time):
    # if not (type(date_time) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", date_time)):
    if not datetime.strptime(date_time, "%Y/%m/%d"):
        raise ValueError("Invalid date time format !!!")
    else:
        return date_time


def payment_id_validator(payment_id):
    if not (type(payment_id) == int and payment_id > 0):
        raise ValueError("Invalid Payment Id !!!")
    else:
        return payment_id


def description_validator(description):
    if not (type(description) == str and re.match(r"^[\w\s.,;:-]*$", description)):
        raise ValueError("Invalid Description !!!")
    else:
        return description
