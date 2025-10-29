import sqlite3
from model import FinancialTransaction


class FinancialTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, financial_transaction):
        self.connect()
        self.cursor.execute("""insert into financial_transactions
                               (transaction_type, customer_id, employee_id, amount, date_time, payment_id, description)
                               values (?, ?, ?, ?, ?, ?, ?)""",
                            [financial_transaction.transaction_type, financial_transaction.customer_id,
                             financial_transaction.employee_id, financial_transaction.amount,
                             financial_transaction.date_time,
                             financial_transaction.payment_id, financial_transaction.description])
        financial_transaction.financial_transaction_id = self.cursor.lastrowid
        self.connection.commit()
        return financial_transaction

    def update(self, financial_transaction):
        self.connect()
        self.cursor.execute("""update financial_transactions
                               set transaction_type=?,
                                   customer_id=?,
                                   employee_id=?,
                                   amount=?,
                                   date_time=?,
                                   payment_id=?,
                                   description=?
                               where id = ?""",
                            [financial_transaction.transaction_type, financial_transaction.customer_id,
                             financial_transaction.employee_id, financial_transaction.amount,
                             financial_transaction.date_time,
                             financial_transaction.payment_id, financial_transaction.description,
                             financial_transaction.financial_transaction_id])
        self.connection.commit()
        self.disconnect()
        return financial_transaction

    def delete(self, financial_transaction_id):
        self.connect()
        self.cursor.execute("delete from financial_transactions where id=?", [financial_transaction_id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from financial_transactions")
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_id(self, financial_transaction_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where id=?", [financial_transaction_id])
        financial_transaction = self.cursor.fetchone()
        self.disconnect()
        if financial_transaction:
            return FinancialTransaction(*financial_transaction)
        return None

    def find_by_transaction_type(self, transaction_type):
        self.connect()
        self.cursor.execute("select * from financial_transactions where transaction_type=?", [transaction_type])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where customer_id=?", [customer_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_employee_id(self, employee_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where employee_id=?", [employee_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_payment_id(self, payment_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where payment_id=?", [payment_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_date_time_range(self, start_date_time, end_date_time):
        self.connect()
        self.cursor.execute("select * from financial_transactions where date_time between ? and ?",
                            [start_date_time, end_date_time])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where date_time between ? and ? and customer_id = ?",
                            [start_date_time, end_date_time, customer_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        self.connect()
        self.cursor.execute("select * from financial_transactions where date_time between ? and ? and employee_id = ?",
                            [start_date_time, end_date_time, employee_id])
        financial_transaction_list = [FinancialTransaction(*transaction) for transaction in self.cursor.fetchall()]
        self.disconnect()
        return financial_transaction_list
