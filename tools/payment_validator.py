import re
from datetime import datetime


def date_time_validator(date_time):
    # if not (type(date_time) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", date_time)):
    if not datetime.strptime(date_time, "%Y/%m/%d"):
        raise ValueError("Invalid date time format !!!")
    else:
        return date_time


def customer_id_validator(customer_id):
    if not (type(customer_id) == int and customer_id > 0):
        raise ValueError("Invalid customer_id !!!")
    else:
        return customer_id


def total_amount_validator(total_amount):
    if not (type(total_amount) == int and total_amount > 0):
        raise ValueError("Invalid total_amount !!!")
    else:
        return total_amount


def employee_id_validator(employee_id):
    if not (type(employee_id) == int and employee_id > 0):
        raise ValueError("Invalid employee_id !!!")
    else:
        return employee_id


def description_validator(description):
    if not (isinstance(description, str) and re.match(r"^[\w\s\"\'!?.,;:-]*$", description)):
        raise ValueError("Invalid description !!!")
    else:
        return description
