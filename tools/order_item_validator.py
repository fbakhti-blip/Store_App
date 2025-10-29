import re

def quantity_validator(quantity):
    if not (type(quantity) == int and quantity > 0):
        raise ValueError("Invalid quantity !!!")
    else:
        return quantity

def customer_validator(customer):
    if not (type(customer) == str and re.match(r"^[a-zA-Z]{5,20}$", customer)):
        raise ValueError(f"{customer} is not a valid name for customer")
    else:
        return customer

def price_validator(price):
    if not (type(price) == int or type(price) == float) or price <= 0:
        raise ValueError("Invalid price !!!")
    else:
        return price

def discount_validator(discount):
    if  not 0 <= discount <= 100:
        raise ValueError("Invalid discount !!!")
    else:
        return discount

def description_validator(description):
    if not (type(description) == str and re.match(r"^[a-zA-Z\s\d\"\'!?.,:;]{0,30}$", description)):
        raise ValueError("Invalid description !!!")
    else:
        return description
