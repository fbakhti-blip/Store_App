from repository import WarehouseTransactionRepository


class WarehouseTransactionService:
    warehouse_transaction_repository = WarehouseTransactionRepository()

    @classmethod
    def save(cls, warehouse_transaction):
        return cls.warehouse_transaction_repository.save(warehouse_transaction)

    @classmethod
    def update(cls, warehouse_transaction):
        warehouse_transaction_result = cls.warehouse_transaction_repository.find_by_id(
            warehouse_transaction.warehouse_transaction_id)
        if warehouse_transaction_result:
            return cls.warehouse_transaction_repository.update(warehouse_transaction)
        else:
            raise Exception("Warehouse Transaction Not Found !!!")

    @classmethod
    def delete(cls, warehouse_transaction_id):
        warehouse_transaction = cls.warehouse_transaction_repository.find_by_id(warehouse_transaction_id)
        if warehouse_transaction:
            cls.warehouse_transaction_repository.delete(warehouse_transaction_id)
            return warehouse_transaction
        else:
            raise Exception("Warehouse Transaction Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.warehouse_transaction_repository.find_all()

    @classmethod
    def find_by_id(cls, warehouse_transaction_id):
        warehouse_transaction = cls.warehouse_transaction_repository.find_by_id(warehouse_transaction_id)
        if warehouse_transaction:
            return warehouse_transaction
        else:
            raise Exception("Warehouse Transaction Not Found !!!")

    @classmethod
    def find_by_product_id(cls, product_id):
        return cls.warehouse_transaction_repository.find_bye_product_id(product_id)

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        return cls.warehouse_transaction_repository.find_by_transaction_type(transaction_type)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        return cls.warehouse_transaction_repository.find_by_customer_id(customer_id)

    @classmethod
    def find_by_employee_id(cls, employee_id):
        return cls.warehouse_transaction_repository.find_by_employee_id(employee_id)

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        return cls.warehouse_transaction_repository.find_by_date_time_range(start_date_time, end_date_time)

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        return cls.warehouse_transaction_repository.find_by_date_time_range_and_customer_id(start_date_time,
                                                                                            end_date_time, customer_id)

    @classmethod
    def find_by_date_time_range_and_employee_id(cls, start_date_time, end_date_time, employee_id):
        return cls.warehouse_transaction_repository.find_by_date_time_range_and_employee_id(start_date_time,
                                                                                            end_date_time, employee_id)
