import sqlite3
from model import Payment


class PaymentRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, payment):
        self.connect()
        self.cursor.execute(
            "insert into payments (transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description) values (?,?,?,?,?,?,?)",
            [payment.transaction_type, payment.payment_type, payment.date_time, payment.customer_id,
             payment.total_amount, payment.employee_id, payment.description])
        payment.payment_id = self.cursor.lastrowid
        self.connection.commit()
        return payment

    def update(self, payment):
        self.connect()
        self.cursor.execute(
            "update payments set transaction_type=?, payment_type=?, date_time=?, customer_id=?, total_amount=?, employee_id=?, description=? where id=?",
            [payment.transaction_type, payment.payment_type, payment.date_time, payment.customer_id,
             payment.total_amount, payment.employee_id, payment.description, payment.id])
        self.connection.commit()
        self.disconnect()
        return payment

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from payments where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from payments")
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_id(self, payment_id):
        self.connect()
        self.cursor.execute("select * from payments where id=?", [payment_id])
        payment = self.cursor.fetchone()
        self.disconnect()
        if payment:
            return Payment(*payment)
        return None

    def find_by_transaction_type(self, transaction_type):
        self.connect()
        self.cursor.execute("select * from payments where transaction_type=?", [transaction_type + "%"])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_payment_type(self, payment_type):
        self.connect()
        self.cursor.execute("select * from payments where payment_type=?", [payment_type + "%"])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_date_time_range(self, start_date_time, end_date_time):
        self.connect()
        self.cursor.execute("select * from payments where date_time between ? and ?", [start_date_time, end_date_time])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        self.connect()
        self.cursor.execute("select * from payments where date_time between ? and ? and customer_id = ?",
                            [start_date_time, end_date_time, customer_id])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        self.connect()
        self.cursor.execute("select * from payments where date_time between ? and ? and employee_id = ?",
                            [start_date_time, end_date_time, employee_id])
        payment_list = [Payment(*payment) for payment in self.cursor.fetchall()]
        self.disconnect()
        return payment_list
