import sqlite3
from model import WarehouseTransaction


class WarehouseTransactionRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, warehouse_transaction):
        self.connect()
        self.cursor.execute("""
                            insert into warehouse_transactions (product_id, quantity, transaction_type,
                                                                transaction_datetime, customer_id, employee_id)
                            values (?, ?, ?, ?, ?, ?)
                            """, ([warehouse_transaction.product_id, warehouse_transaction.quantity,
                                   warehouse_transaction.transaction_type, warehouse_transaction.transaction_datetime,
                                   warehouse_transaction.customer_id, warehouse_transaction.employee_id]))
        warehouse_transaction.warehouse_transaction_id = self.cursor.lastrowid
        self.connection.commit()
        return warehouse_transaction

    def update(self, warehouse_transaction):
        self.connect()
        self.cursor.execute("""update warehouse_transactions
                               set product_id=?,
                                   quantity=?,
                                   transaction_type=?,
                                   transaction_datetime=?,
                                   customer_id=?,
                                   employee_id=?
                               where id = ?""", ([warehouse_transaction.product_id, warehouse_transaction.quantity,
                                                  warehouse_transaction.transaction_type,
                                                  warehouse_transaction.transaction_datetime,
                                                  warehouse_transaction.customer_id, warehouse_transaction.employee_id,
                                                  warehouse_transaction.warehouse_transaction_id]))
        self.connection.commit()
        self.disconnect()
        return warehouse_transaction

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from warehouse_transactions where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions")
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_id(self, warehouse_transaction_id):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where id=?", [warehouse_transaction_id])
        warehouse_transaction = self.cursor.fetchone()
        self.disconnect()
        if warehouse_transaction:
            return WarehouseTransaction(*warehouse_transaction)
        return None

    def find_bye_product_id(self, product_id):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where product_id=?", [product_id])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_transaction_type(self, transaction_type):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where transaction_type=?", [transaction_type])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where customer_id=?", [customer_id])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_employee_id(self, employee_id):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where warehouse_transactions.employee_id=?",
                            [employee_id])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_date_time_range(self, start_date_time, end_date_time):
        self.connect()
        self.cursor.execute("select * from warehouse_transactions where transaction_datetime between ? and ?",
                            [start_date_time, end_date_time])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        self.connect()
        self.cursor.execute(
            "select * from warehouse_transactions where transaction_datetime between ? and ? and customer_id=?",
            [start_date_time, end_date_time, customer_id])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list

    def find_by_date_time_range_and_employee_id(self, start_date_time, end_date_time, employee_id):
        self.connect()
        self.cursor.execute(
            "select * from warehouse_transactions where transaction_datetime between ? and ? and employee_id=?",
            [start_date_time, end_date_time, employee_id])
        warehouse_transaction_list = [WarehouseTransaction(*warehouse_transaction) for warehouse_transaction in
                                      self.cursor.fetchall()]
        self.disconnect()
        return warehouse_transaction_list
