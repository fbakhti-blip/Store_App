import re
from datetime import datetime


def product_id_validator(product_id):
    if not (type(product_id) == int and product_id > 0):
        raise ValueError("Invalid product ID !!")
    else:
        return product_id


def quantity_validator(quantity):
    if not (type(quantity) == int and quantity > 0):
        raise ValueError("Invalid quantity !!")
    else:
        return quantity


def datetime_validator(date_time):
    if datetime.strptime(date_time, "%Y/%m/%d"):
        return date_time
    else:
        raise ValueError("date or time is invalid !!")


def customer_id_validator(customer_id):
    if not (type(customer_id) == int and customer_id > 0):
        raise ValueError("Invalid customer_id !!")
    else:
        return customer_id


def employee_id_validator(employee_id):
    if not (type(employee_id) == int and employee_id > 0):
        raise ValueError("Invalid employee_id !!!")
    else:
        return employee_id
