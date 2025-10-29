import sqlite3
from model import Order


class OrderRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, order):
        self.connect()
        self.cursor.execute("insert into orders (order_type, customer_id, employee_id,  date_time, payment_id, warehouse_transaction_id, tax, total_discount, total_amount) values (?,?,?,?,?,?,?,?,?)" ,
                            [order.order_type, order.customer_id, order.employee_id, order.date_time, order.payment_id, order.warehouse_transaction_id, order.tax, order.total_discount, order.total_amount])
        order.id = self.cursor.lastrowid
        self.connection.commit()
        return order

    def update(self, order):
        self.connect()
        self.cursor.execute("update orders set order_type=?, customer_id=?, employee_id=?, date_time=?, payment_id=?, warehouse_transaction_id=?, tax=?, total_discount=?, total_amount=? where id=?" ,
                            [order.order_type, order.customer_id, order.employee_id,  order.date_time, order.payment_id, order.warehouse_transaction_id, order.tax, order.total_discount, order.total_amount, order.order_id])
        self.connection.commit()
        self.disconnect()
        return order

    def delete(self,id):
        self.connect()
        self.cursor.execute("delete from orders where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from orders")
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_id(self, order_id):
        self.connect()
        self.cursor.execute("select * from orders where id=?", [order_id])
        order = self.cursor.fetchone()
        self.disconnect()
        if order:
            return Order(*order)
        return None

    def find_by_order_type(self, order_type):
        self.connect()
        self.cursor.execute("select * from orders where order_type=?", [order_type])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_customer_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from orders where customer_id=?", [customer_id])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_employee_id(self, employee_id):
        self.connect()
        self.cursor.execute("select * from orders where employee_id=?", [employee_id])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_date_time_range(self, start_date_time, end_date_time):
        self.connect()
        self.cursor.execute("select * from orders where date_time between ? and ?",
                            [start_date_time, end_date_time])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list

    def find_by_date_time_range_and_customer_id(self, start_date_time, end_date_time, customer_id):
        self.connect()
        self.cursor.execute("select * from orders where date_time between ? and ? and customer_id=?" ,
                            [start_date_time, end_date_time, customer_id])
        order_list = [Order(*order) for order in self.cursor.fetchall()]
        self.disconnect()
        return order_list