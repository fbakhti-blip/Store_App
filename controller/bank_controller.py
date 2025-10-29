from model import Bank
from service import BankService
from tools import Logger


class BankController:
    @staticmethod
    def save(name, account, balance, description):
        try:
            bank = Bank(None, name, account, balance, description)
            bank.validate()
            bank = BankService.save(bank)
            Logger.info(f"Bank {bank} saved")
            return True, f"Bank Saved Successfully"
        except Exception as e:
            Logger.error(f"Bank Saved Error: {e}")
            return False, e

    @staticmethod
    def update(bank_id, name, account, balance, description):
        try:
            bank = Bank(bank_id, name, account, balance, description)
            bank.validate()
            bank = BankService.update(bank)
            Logger.info(f"Bank {bank} updated")
            return True, "Bank Updated Successfully"
        except Exception as e:
            Logger.error(f"Bank Updated Error: {e}")
            return False, e

    @staticmethod
    def delete(bank_id):
        try:
            bank = BankService.delete(bank_id)
            Logger.info(f"Bank {bank} deleted")
            return True, f"Bank Deleted Successfully"
        except Exception as e:
            Logger.error(f"Bank Delete Error: {e}")
            return False, e

    @staticmethod
    def find_all(cls):
        try:
            bank_list = BankService.find_all()
            Logger.info("Bank FindAll")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Bank FindAll Error: {e}")
            return False, e

    @staticmethod
    def find_by_id(bank_id):
        try:
            bank = BankService.find_by_id(bank_id)
            Logger.info(f"Bank FindById {bank_id}")
            return True, bank
        except Exception as e:
            Logger.error(f"{e} With Id {bank_id}")
            return False, e

    @staticmethod
    def find_by_name(name):
        try:
            bank_list = BankService.find_by_name(name)
            Logger.info(f"Bank FindByName {name}")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Bank FindByName Error: {e}")
            return False, e

    @staticmethod
    def find_by_account(account):
        try:
            bank_list = BankService.find_by_account(account)
            Logger.info(f"Bank FindByAccount {account}")
            return True, bank_list
        except Exception as e:
            Logger.error(f"Bank FindByAccount Error: {e}")
            return False, e
