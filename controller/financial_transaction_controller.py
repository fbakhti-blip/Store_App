from model import FinancialTransaction
from service import FinancialTransactionService
from tools.logging import Logger


class FinancialTransactionController:

    @classmethod
    def save(cls, transaction_type, customer_id, employee_id, amount, date_time, payment_id, description):
        try:
            financial_transaction = FinancialTransaction(None, transaction_type, customer_id, employee_id, amount,
                                                         date_time, payment_id, description)
            financial_transaction.validate()
            financial_transaction = FinancialTransactionService.save(financial_transaction)
            Logger.info(f"FinancialTransaction {financial_transaction} saved")
            return True, f"FinancialTransaction Saved Successfully"
        except Exception as e:
            Logger.error(f"FinancialTransaction Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, financial_transaction_id, transaction_type, customer_id, employee_id, amount, date_time, payment_id,
               description):
        try:
            financial_transaction = FinancialTransaction(financial_transaction_id, transaction_type, customer_id,
                                                         employee_id, amount,
                                                         date_time, payment_id, description)
            financial_transaction.validate()
            financial_transaction = FinancialTransactionService.update(financial_transaction)
            Logger.info(f"FinancialTransaction {financial_transaction} updated")
            return True, "FinancialTransaction Updated Successfully"
        except Exception as e:
            Logger.error(f"FinancialTransaction Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, financial_transaction_id):
        try:
            financial_transaction = FinancialTransactionService.delete(financial_transaction_id)
            Logger.info(f"FinancialTransaction {financial_transaction} deleted")
            return True, f"FinancialTransaction Deleted Successfully"
        except Exception as e:
            Logger.error(f"FinancialTransaction Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            financial_transaction_list = FinancialTransactionService.find_all()
            Logger.info("FinancialTransaction FindAll")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, financial_transaction_id):
        try:
            financial_transaction = FinancialTransactionService.find_by_id(financial_transaction_id)
            Logger.info(f"FinancialTransaction FindById {financial_transaction_id}")
            return True, financial_transaction
        except Exception as e:
            Logger.error(f"{e} With Id {financial_transaction_id}")
            return False, e

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_transaction_type(transaction_type)
            Logger.info(f"FinancialTransaction FindByTransactionType {transaction_type}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByTransactionType Error: {e}")
            return False, e

    @classmethod
    def find_by_customer_id(cls, customer_id):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_customer_id(customer_id)
            Logger.info(f"FinancialTransaction FindByCustomerId {customer_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByCustomerId Error: {e}")
            return False, e

    @classmethod
    def find_by_employee_id(cls, employee_id):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_employee_id(employee_id)
            Logger.info(f"FinancialTransaction FindByEmployeeId {employee_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByEmployeeId Error: {e}")
            return False, e

    @classmethod
    def find_by_payment_id(cls, payment_id):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_payment_id(payment_id)
            Logger.info(f"FinancialTransaction FindByPaymentId {payment_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByPaymentId Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_date_time_range(start_date_time,
                                                                                             end_date_time)
            Logger.info(f"FinancialTransaction FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByDateTimeRange Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_date_time_range_and_customer_id(
                start_date_time, end_date_time, customer_id)
            Logger.info(
                f"FinancialTransaction FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_employee_id(cls, start_date_time, end_date_time, employee_id):
        try:
            financial_transaction_list = FinancialTransactionService.find_by_date_time_range_and_employee_id(
                start_date_time, end_date_time, employee_id)
            Logger.info(
                f"FinancialTransaction FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, employee: {employee_id}")
            return True, financial_transaction_list
        except Exception as e:
            Logger.error(f"FinancialTransaction FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e
