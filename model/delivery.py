from tools.delivery_validator import *


class Delivery:
    def __init__(self, delivery_id, first_name, last_name, address, description):
        self.delivery_id = delivery_id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.description = description

    def validate(self):
        first_name_validator(self.first_name)
        last_name_validator(self.last_name)
        address_validator(self.address)
        description_validator(self.description)

    def __repr__(self):
        return f'{self.__dict__}'

    def to_tuple(self):
        return tuple((self.delivery_id, self.first_name, self.last_name, self.address, self.description))
