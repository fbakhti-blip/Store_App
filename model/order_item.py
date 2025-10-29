from tools.order_item_validator import *


class OrderItem:

    def __init__(self, order_item_id, order_id, product_id, quantity, price, discount=None, description=None):
        self.order_item_id = order_item_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity
        self.price = price
        self.discount = discount
        self.description = description

    def validate(self):
        quantity_validator(self.quantity)
        price_validator(self.price)
        discount_validator(self.discount)
        description_validator(self.description)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        from service import ProductService

        product = ProductService.find_by_id(self.product_id)

        return tuple((
            self.order_item_id,
            self.order_id,
            product.name+" "+product.brand,
            self.quantity,
            self.price,
            self.discount,
            self.description))

