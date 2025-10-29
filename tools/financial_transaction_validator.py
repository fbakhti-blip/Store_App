import re


def transaction_type_validator(transaction_type):
    if not (type(transaction_type) == str and re.match(r"^[a-zA-Z\s]{2,20}$", transaction_type)):
        raise ValueError("Invalid Transaction Type !!!")
    else:
        return transaction_type


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
    if not (type(date_time) == str and re.match(r"^\d{2}[/-]\d{2}[/-]\d{4}\s\d{2}:\d{2}(:\d{2})$", date_time)):
        raise ValueError("Invalid Date Time !!!")
    else:
        return date_time


def payment_id_validator(payment_id):
    if not (type(payment_id) == int and payment_id > 0):
        raise ValueError("Invalid Payment Id !!!")
    else:
        return payment_id


def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z\s]*$", description)):
        raise ValueError("Invalid Description !!!")
    else:
        return description
