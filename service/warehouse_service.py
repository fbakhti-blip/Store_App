from repository import WarehouseRepository


class WarehouseService:
    warehouse_repository = WarehouseRepository()

    @classmethod
    def save(cls, warehouse):
        return cls.warehouse_repository.save(warehouse)

    @classmethod
    def update(cls, warehouse):
        warehouse_result = cls.warehouse_repository.find_by_id(warehouse.warehouse_id)
        if warehouse_result:
            return cls.warehouse_repository.update(warehouse)
        else:
            raise Exception("Warehouse Not Found !!!")

    @classmethod
    def delete(cls, warehouse_id):
        warehouse = cls.warehouse_repository.find_by_id(warehouse_id)
        if warehouse:
            cls.warehouse_repository.delete(warehouse_id)
            return warehouse
        else:
            raise Exception("Warehouse Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.warehouse_repository.find_all()

    @classmethod
    def find_by_id(cls, warehouse_id):
        warehouse = cls.warehouse_repository.find_by_id(warehouse_id)
        if warehouse:
            return warehouse
        else:
            raise Exception("Warehouse Not Found !!!")

    @classmethod
    def find_by_product_id(cls, product_id):
        return cls.warehouse_repository.find_by_product_id(product_id)

    @classmethod
    def find_by_quantity_less_than(cls, quantity):
        return cls.warehouse_repository.find_by_quantity_less_than(quantity)

    @classmethod
    def find_by_quantity_more_than(cls, quantity):
        return cls.warehouse_repository.find_by_quantity_more_than(quantity)
