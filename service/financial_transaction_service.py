from repository import FinancialTransactionRepository


class FinancialTransactionService:
    financial_transaction_repository = FinancialTransactionRepository()

    @classmethod
    def save(cls, financial_transaction):
        return cls.financial_transaction_repository.save(financial_transaction)

    @classmethod
    def update(cls, financial_transaction):
        financial_transaction_result = cls.financial_transaction_repository.find_by_id(financial_transaction.financial_transaction_id)
        if financial_transaction_result:
            return cls.financial_transaction_repository.update(financial_transaction)
        else:
            raise Exception("Financial Transaction Not Found !!!")

    @classmethod
    def delete(cls, financial_transaction_id):
        financial_transaction = cls.financial_transaction_repository.find_by_id(financial_transaction_id)
        if financial_transaction:
            cls.financial_transaction_repository.delete(financial_transaction_id)
            return financial_transaction
        else:
            raise Exception("Financial Transaction Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.financial_transaction_repository.find_all()

    @classmethod
    def find_by_id(cls, financial_transaction_id):
        financial_transaction = cls.financial_transaction_repository.find_by_id(financial_transaction_id)
        if financial_transaction:
            return financial_transaction
        else:
            raise Exception("Financial Transaction Not Found !!!")

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        return cls.financial_transaction_repository.find_by_transaction_type(transaction_type)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        return cls.financial_transaction_repository.find_by_customer_id(customer_id)

    @classmethod
    def find_by_employee_id(cls, employee_id):
        return cls.financial_transaction_repository.find_by_employee_id(employee_id)

    @classmethod
    def find_by_payment_id(cls, payment_id):
        return cls.financial_transaction_repository.find_by_payment_id(payment_id)

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        return cls.financial_transaction_repository.find_by_date_time_range(start_date_time, end_date_time)

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        return cls.financial_transaction_repository.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
