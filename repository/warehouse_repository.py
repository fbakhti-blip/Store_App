import sqlite3
from model import Warehouse


class WarehouseRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/selling_db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save(self, warehouse):
            self.connect()
            self.cursor.execute("""insert into warehouses (product_id,quantity) values (?,?)""", ([warehouse.product_id,warehouse.quantity]))
            warehouse.warehouse_id = self.cursor.lastrowid
            self.connection.commit()
            return warehouse

    def update(self, warehouse):
            self.connect()
            self.cursor.execute("""update warehouses set product_id=?,quantity=? where id=?""", ([warehouse.product_id, warehouse.quantity, warehouse.id]))
            self.connection.commit()
            self.disconnect()
            return warehouse

    def delete(self,id):
        self.connect()
        self.cursor.execute("delete from warehouses where id=?",[id])
        self.connection.commit()
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from warehouses")
        warehouse_list = [Warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_list

    def find_by_id(self, warehouse_id):
        self.connect()
        self.cursor.execute("select * from warehouses where id=?", [warehouse_id])
        warehouse = self.cursor.fetchone()
        self.disconnect()
        if warehouse:
            return Warehouse(*warehouse)
        return None

    def find_by_product_id(self,product_id):
        self.connect()
        self.cursor.execute("select * from warehouses where product_id=?", [product_id])
        warehouse_list = [Warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_list

    def find_by_quantity_less_than(self, quantity):
        self.connect()
        self.cursor.execute("select * from warehouses where quantity < ?", [quantity])
        warehouse_list = [Warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_list

    def find_by_quantity_more_than(self, quantity):
        self.connect()
        self.cursor.execute("select * from warehouses where quantity > ?", [quantity])
        warehouse_list = [Warehouse(*warehouse) for warehouse in self.cursor.fetchall()]
        self.disconnect()
        return warehouse_list

