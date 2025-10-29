import sqlite3
from model import Delivery


class DeliveryRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, delivery):
        self.connect()
        self.cursor.execute(
                "insert into deliveries (first_name, last_name, address, description) values (?,?,?,?)",
                [delivery.first_name, delivery.last_name, delivery.address, delivery.description])
        delivery.delivery_id = self.cursor.lastrowid
        self.connection.commit()
        return delivery

    def update(self, delivery):
        self.connect()
        self.cursor.execute("update deliveries set first_name=?, last_name=?, address=?, description=? where id=?",
                            [delivery.first_name, delivery.last_name, delivery.address, delivery.description, delivery.id])
        self.connection.commit()
        self.disconnect()
        return delivery

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from deliveries where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from deliveries")
        delivery_list = [Delivery(*delivery) for delivery in self.cursor.fetchall()]
        self.disconnect()
        return delivery_list

    def find_by_id(self, delivery_id):
        self.connect()
        self.cursor.execute("select * from deliveries where id=?", [delivery_id])
        delivery = self.cursor.fetchone()
        self.disconnect()
        if delivery:
            return Delivery(*delivery)
        return None
