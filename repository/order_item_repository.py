import sqlite3
from model import OrderItem


class OrderItemRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, order_item):
        self.connect()
        self.cursor.execute("insert into order_items (order_id, product_id , quantity,"
                            " price, discount, description) values (?,?,?,?,?,?)" ,
                            [order_item.order_id, order_item.product_id, order_item.quantity,
                             order_item.price, order_item.discount, order_item.description])
        order_item.id = self.cursor.lastrowid
        self.connection.commit()
        return order_item

    def update(self, order_item):
        self.connect()
        self.cursor.execute("update order_items set order_id=?, product_id=?, quantity=?,"
                            " price=?, discount=?, description=? where id=?" ,
                            [order_item.order_id, order_item.product_id, order_item.quantity,
                             order_item.price, order_item.discount, order_item.description, order_item.order_item_id])
        self.connection.commit()
        self.disconnect()
        return order_item

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from order_items where id=?", [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from order_items")
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

    def find_by_id(self, order_item_id):
        self.connect()
        self.cursor.execute("select * from order_items where id=?", [order_item_id])
        order_item = self.cursor.fetchone()
        self.disconnect()
        if order_item:
            return OrderItem(*order_item)
        return None

    def find_by_order_id(self, order_id):
        self.connect()
        self.cursor.execute("select * from order_items where order_id=?", [order_id])
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

    def find_by_product_id(self, product_id):
        self.connect()
        self.cursor.execute("select * from order_items where product_id=?", [product_id])
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

    def find_by_quantity_less_than(self, quantity):
        self.connect()
        self.cursor.execute("select * from order_items where quantity < ?", [quantity])
        order_item_list = [OrderItem(*order_item) for order_item in self.cursor.fetchall()]
        self.disconnect()
        return order_item_list

