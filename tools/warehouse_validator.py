import re

def product_id_validator(product_id):
    if not (type(product_id) == int and re.match(r'^[0-9]{8}$', product_id)):
        raise ValueError('Invalid product ID')
    else:
        return product_id

def quantity_validator(quantity):
    if not (type(quantity) == int and re.match(r'^\d+$', quantity)):
        raise ValueError('Invalid quantity')
    else:
        return quantity