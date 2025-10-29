from model import Warehouse
from service import WarehouseService
from tools.logging import Logger


class WarehouseController:

    @classmethod
    def save(cls, product_id, quantity):
        try:
            warehouse = Warehouse(None, product_id, quantity)
            warehouse.validate()
            warehouse = WarehouseService.save(warehouse)
            Logger.info(f"Warehouse {warehouse} saved")
            return True, f"Warehouse Saved Successfully"
        except Exception as e:
            Logger.error(f"Warehouse Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, warehouse_id, product_id, quantity):
        try:
            warehouse = Warehouse(warehouse_id, product_id, quantity)
            warehouse.validate()
            warehouse = WarehouseService.update(warehouse)
            Logger.info(f"Warehouse {warehouse} updated")
            return True, "Warehouse Updated Successfully"
        except Exception as e:
            Logger.error(f"Warehouse Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, warehouse_id):
        try:
            warehouse = WarehouseService.delete(warehouse_id)
            Logger.info(f"Warehouse {warehouse} deleted")
            return True, f"Warehouse Deleted Successfully"
        except Exception as e:
            Logger.error(f"Warehouse Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            warehouse_list = WarehouseService.find_all()
            Logger.info("Warehouse FindAll")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, warehouse_id):
        try:
            warehouse = WarehouseService.find_by_id(warehouse_id)
            Logger.info(f"Warehouse FindById {warehouse_id}")
            return True, warehouse
        except Exception as e:
            Logger.error(f"{e} With Id {warehouse_id}")
            return False, e

    @classmethod
    def find_by_product_id(cls, product_id):
        try:
            warehouse_list = WarehouseService.find_by_product_id(product_id)
            Logger.info(f"Warehouse FindByProductId {product_id}")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindByProductId Error: {e}")
            return False, e

    @classmethod
    def find_by_quantity_less_than(cls, quantity):
        try:
            warehouse_list = WarehouseService.find_by_quantity_less_than(quantity)
            Logger.info(f"Warehouse FindByQuantityLessThan {quantity}")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindByQuantityLessThan Error: {e}")
            return False, e

    @classmethod
    def find_by_quantity_more_than(cls, quantity):
        try:
            warehouse_list = WarehouseService.find_by_quantity_more_than(quantity)
            Logger.info(f"Warehouse FindByQuantityMoreThan {quantity}")
            return True, warehouse_list
        except Exception as e:
            Logger.error(f"Warehouse FindByQuantityMoreThan Error: {e}")
            return False, e
