from model import Order
from service import OrderService
from tools.logging import Logger


class OrderController:
    @classmethod
    def save(cls, order_type, customer_id, employee_id, date_time,
             payment_id, warehouse_transaction_id, tax, total_discount,
             total_amount):
        try:
            order = Order(None, order_type, customer_id, employee_id, date_time,
                          payment_id, warehouse_transaction_id, tax, total_discount,
                          total_amount)
            order.validate()
            order = OrderService.save(order)
            Logger.info(f"Order {order} saved")
            return True, f"Order Saved Successfully"
        except Exception as e:
            Logger.error(f"Order Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, order_id, order_type, customer_id, employee_id, date_time,
               payment_id, warehouse_transaction_id, tax, total_discount,
               total_amount):
        try:
            order = Order(order_id, order_type, customer_id, employee_id, date_time,
                          payment_id, warehouse_transaction_id, tax, total_discount,
                          total_amount)
            order.validate()
            order = OrderService.update(order)
            Logger.info(f"Order {order} updated")
            return True, "Order Updated Successfully"
        except Exception as e:
            Logger.error(f"Order Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, order_id):
        try:
            order = OrderService.delete(order_id)
            Logger.info(f"Order {order} deleted")
            return True, f"Order Deleted Successfully"
        except Exception as e:
            Logger.error(f"Order Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            order_list = OrderService.find_all()
            Logger.info("Order FindAll")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, order_id):
        try:
            order = OrderService.find_by_id(order_id)
            Logger.info(f"Order FindById {order_id}")
            return True, order
        except Exception as e:
            Logger.error(f"{e} With Id {order_id}")
            return False, e

    @classmethod
    def find_by_order_type(cls, order_type):
        try:
            order_list = OrderService.find_by_order_type(order_type)
            Logger.info(f"Order FindByOrderType {order_type}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByOrderType Error: {e}")
            return False, e

    @classmethod
    def find_by_customer_id(cls, customer_id):
        try:
            order_list = OrderService.find_by_customer_id(customer_id)
            Logger.info(f"Order FindByCustomerId {customer_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByCustomerId Error: {e}")
            return False, e

    @classmethod
    def find_by_employee_id(cls, employee_id):
        try:
            order_list = OrderService.find_by_employee_id(employee_id)
            Logger.info(f"Order FindByEmployeeId {employee_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByEmployeeId Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        try:
            order_list = OrderService.find_by_date_time_range(start_date_time, end_date_time)
            Logger.info(f"Order FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByDateTimeRange Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        try:
            order_list = OrderService.find_by_date_time_range_and_customer_id(start_date_time, end_date_time,
                                                                              customer_id)
            Logger.info(
                f"Order FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, order_list
        except Exception as e:
            Logger.error(f"Order FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e
