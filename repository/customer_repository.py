import sqlite3

from model import Customer


class CustomerRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, customer):
        self.connect()
        self.cursor.execute(
            "insert into customers (first_name, last_name, phone_number, address) values (?,?,?,?)",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address])
        customer.customer_id = self.cursor.lastrowid
        self.connection.commit()
        return customer

    def update(self, customer):
        self.connect()
        self.cursor.execute(
            "update customers set first_name=?, last_name=?, phone_number=?, address=? where id=?",
            [customer.first_name, customer.last_name, customer.phone_number, customer.address, customer.id])
        self.connection.commit()
        self.disconnect()
        return customer

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from customers where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from customers")
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_id(self, customer_id):
        self.connect()
        self.cursor.execute("select * from customers where id=?", [customer_id])
        customer = self.cursor.fetchone()
        self.disconnect()
        if customer:
            return Customer(*customer)
        return None

    def find_by_firstname_and_lastname(self,firstname, lastname):
        self.connect()
        self.cursor.execute("select * from customers where first_name=? and last_name=?", [firstname, lastname])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list

    def find_by_phone_number(self, phone_number):
        self.connect()
        self.cursor.execute("select * from customers where phone_number=? ", [phone_number])
        customer_list = [Customer(*customer) for customer in self.cursor.fetchall()]
        self.disconnect()
        return customer_list


