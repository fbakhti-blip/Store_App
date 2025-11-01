import sqlite3
from model import Product


class ProductRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, product):
        self.connect()
        self.cursor.execute(
            "insert into products (name, brand, model, serial, category, unit, expiration_date) values (?,?,?,?,?,?,?)",
            [product.name, product.brand, product.model, product.serial, product.category, product.unit,
             product.expiration_date])
        product.product_id = self.cursor.lastrowid
        self.connection.commit()
        return product

    def update(self, product):
        self.connect()
        self.cursor.execute(
            "update products set name=?, brand=?, model=?, serial=?, category=?, unit=?, expiration_date=? where id=?",
            [product.name, product.brand, product.model, product.serial, product.category, product.unit,
             product.expiration_date, product.product_id])
        self.connection.commit()
        self.disconnect()
        return product

    def delete(self, id):
        self.connect()
        self.cursor.execute("delete from products where id=?",
                            [id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from products")
        product_list = [Product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list

    def find_by_id(self, product_id):
        self.connect()
        self.cursor.execute("select * from products where id=?", [product_id])
        product = self.cursor.fetchone()
        self.disconnect()
        if product:
            return Product(*product)
        return None

    def find_by_name_and_brand(self, name, brand):
        self.connect()
        self.cursor.execute("select * from products where name like ? and brand like ?", [name + "%", brand + "%"])
        product_list = [Product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list

    def find_by_category(self, category):
        self.connect()
        self.cursor.execute("select * from products where category=?", [category])
        product_list = [Product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list

    def find_by_expire_date_until(self, expire_date):
        self.connect()
        self.cursor.execute("select * from products where expiration_date=?", [expire_date])
        product_list = [Product(*product) for product in self.cursor.fetchall()]
        self.disconnect()
        return product_list
