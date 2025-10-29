from repository import BankRepository


class BankService:
    bank_repository = BankRepository()

    @classmethod
    def save(cls, bank):
        return cls.bank_repository.save(bank)

    @classmethod
    def update(cls, bank):
        bank_result = cls.bank_repository.find_by_id(bank.bank_id)
        if bank_result:
            return cls.bank_repository.update(bank)
        else:
            raise Exception("Bank Not Found !!!")

    @classmethod
    def delete(cls, bank_id):
        bank = cls.bank_repository.find_by_id(bank_id)
        if bank:
            cls.bank_repository.delete(bank_id)
            return bank
        else:
            raise Exception("Bank Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.bank_repository.find_all()

    @classmethod
    def find_by_id(cls, bank_id):
        bank = cls.bank_repository.find_by_id(bank_id)
        if bank:
            return bank
        else:
            raise Exception("Bank Not Found !!!")

    @classmethod
    def find_by_name(cls, name):
        return cls.bank_repository.find_by_name(name)

    @classmethod
    def find_by_account(cls, account):
        return cls.bank_repository.find_by_account(account)
