from model import WarehouseTransaction
from service import WarehouseTransactionService
from tools.logging import Logger


class WarehouseTransactionController:

    @classmethod
    def save(cls, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(None, product_id, quantity, transaction_type,
                                                         transaction_datetime, customer_id, employee_id)
            warehouse_transaction.validate()
            warehouse_transaction = WarehouseTransactionService.save(warehouse_transaction)
            Logger.info(f"WarehouseTransaction {warehouse_transaction} saved")
            return True, f"WarehouseTransaction Saved Successfully"
        except Exception as e:
            Logger.error(f"WarehouseTransaction Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, warehouse_transaction_id, product_id, quantity, transaction_type, transaction_datetime, customer_id, employee_id):
        try:
            warehouse_transaction = WarehouseTransaction(warehouse_transaction_id, product_id, quantity, transaction_type,
                                                         transaction_datetime, customer_id, employee_id)
            warehouse_transaction.validate()
            warehouse_transaction = WarehouseTransactionService.update(warehouse_transaction)
            Logger.info(f"WarehouseTransaction {warehouse_transaction} updated")
            return True, "WarehouseTransaction Updated Successfully"
        except Exception as e:
            Logger.error(f"WarehouseTransaction Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, warehouse_transaction_id):
        try:
            warehouse_transaction = WarehouseTransactionService.delete(warehouse_transaction_id)
            Logger.info(f"WarehouseTransaction {warehouse_transaction} deleted")
            return True, f"WarehouseTransaction Deleted Successfully"
        except Exception as e:
            Logger.error(f"WarehouseTransaction Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_all()
            Logger.info("WarehouseTransaction FindAll")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, warehouse_transaction_id):
        try:
            warehouse_transaction = WarehouseTransactionService.find_by_id(warehouse_transaction_id)
            Logger.info(f"WarehouseTransaction FindById {warehouse_transaction_id}")
            return True, warehouse_transaction
        except Exception as e:
            Logger.error(f"{e} With Id {warehouse_transaction_id}")
            return False, e

    @classmethod
    def find_by_product_id(cls, product_id):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_product_id(product_id)
            Logger.info(f"WarehouseTransaction FindByProductId {product_id}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByProductId Error: {e}")
            return False, e

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_transaction_type(transaction_type)
            Logger.info(f"WarehouseTransaction FindByTransactionType {transaction_type}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByTransactionType Error: {e}")
            return False, e

    @classmethod
    def find_by_customer_id(cls, customer_id):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_customer_id(customer_id)
            Logger.info(f"WarehouseTransaction FindByCustomerId {customer_id}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByCustomerId Error: {e}")
            return False, e

    @classmethod
    def find_by_employee_id(cls, employee_id):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_employee_id(employee_id)
            Logger.info(f"WarehouseTransaction FindByEmployeeId {employee_id}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByEmployeeId Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_date_time_range(start_date_time, end_date_time)
            Logger.info(f"WarehouseTransaction FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByDateTimeRange Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
            Logger.info(f"WarehouseTransaction FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_employee_id(cls, start_date_time, end_date_time, employee_id):
        try:
            warehouse_transaction_list = WarehouseTransactionService.find_by_date_time_range_and_employee_id(start_date_time, end_date_time, employee_id)
            Logger.info(f"WarehouseTransaction FindByDateTimeRangeAndEmployeeId {start_date_time} to {end_date_time}, employee: {employee_id}")
            return True, warehouse_transaction_list
        except Exception as e:
            Logger.error(f"WarehouseTransaction FindByDateTimeRangeAndEmployeeId Error: {e}")
            return False, e
