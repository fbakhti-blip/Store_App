from tools.bank_validator import *


class Bank:
    def __init__(self, bank_id, name, account, balance, description):
        self.bank_id = bank_id
        self.name = name
        self.account = account
        self.balance = balance
        self.description = description

    def validate(self):
        name_validator(self.name)
        account_validator(self.account)
        balance_validator(self.balance)
        description_validator(self.description)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        return tuple((self.bank_id, self.name, self.account, self.balance, self.description))
