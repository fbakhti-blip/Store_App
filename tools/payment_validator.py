import re


def transaction_type_validator(transaction_type):
    if not (type(transaction_type) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", transaction_type)):
        raise ValueError("Invalid transaction_type !!!")
    else:
        return transaction_type


def payment_type_validator(payment_type):
    if not (type(payment_type) == str and re.match(r"^[a-zA-Z0-9\s]{3,30}$", payment_type)):
        raise ValueError("Invalid payment_type !!!")
    else:
        return payment_type


def date_time_validator(date_time):
    if not (type(date_time) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", date_time)):
        raise ValueError("Invalid date_time !!!")
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
    if not (type(description) == str and re.match(r"^[a-zA-Z0-9\s.,_-]+$", description)):
        raise ValueError("Invalid description !!!")
    else:
        return description
