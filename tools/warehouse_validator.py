def product_id_validator(product_id):
    if not (isinstance(product_id, int) and product_id > 0):
        raise ValueError('Invalid product ID')
    else:
        return product_id


def quantity_validator(quantity):
    if not (isinstance(quantity, int) and quantity >= 0):
        raise ValueError('Invalid quantity')
    else:
        return quantity
