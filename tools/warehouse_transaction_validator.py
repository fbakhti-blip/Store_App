import re
from datetime import datetime

def product_id_validator(product_id):
    if not (type(product_id) == int and re.match(r'^[0-9]{8}$', product_id)):
        raise ValueError('Invalid product ID')
    else:
        return product_id

def quantity_validator(quantity):
    if not (type(quantity) == int and re.match(r'^[0-9]+$', quantity)):
        raise ValueError('Invalid quantity')
    else:
        return quantity

def datetime_validator(date_time):
    if datetime.strptime(date_time, "%Y-%m-%d %H:%M"):
        return date_time
    else:
        raise ValueError('date or time is invalid!!')

def customer_id_validator(customer_id):
    if not (type(customer_id) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", customer_id)):
        raise ValueError("Invalid customer_id !!!")
    else:
        return customer_id

def employee_id_validator(employee_id):
    if not (type(employee_id) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", employee_id)):
        raise ValueError("Invalid employee_id !!!")
    else:
        return employee_id


def transaction_type_validator(transaction_type):
    if transaction_type=="get"or transaction_type=="receive":
        return transaction_type
    else:
        raise ValueError('Invalid transaction type !!!')