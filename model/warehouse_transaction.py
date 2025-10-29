from tools.warehouse_transaction_validator import *


class WarehouseTransaction:
    def __init__(self, warehouse_transaction_id, product_id, quantity, transaction_type, transaction_datetime,
                 customer_id, employee_id):
        self.warehouse_transaction_id = warehouse_transaction_id
        self.product_id = product_id
        self.quantity = quantity
        self.transaction_type = transaction_type
        self.transaction_datetime = transaction_datetime
        self.customer_id = customer_id
        self.employee_id = employee_id

    def validate(self):
        product_id_validator(self.product_id)
        quantity_validator(self.quantity)
        transaction_type_validator(self.transaction_type)
        datetime_validator(self.transaction_datetime)
        customer_id_validator(self.customer_id)
        employee_id_validator(self.employee_id)

    def __repr__(self):
        return f'{self.__dict__}'

    def to_tuple(self):
        from service import CustomerService, EmployeeService, ProductService

        customer = CustomerService.find_by_id(self.customer_id)
        employee = EmployeeService.find_by_id(self.employee_id)
        product = ProductService.find_by_id(self.product_id)

        return tuple(
            (self.warehouse_transaction_id,
             product.info(),
             self.quantity,
             self.transaction_type,
             self.transaction_datetime,
             customer.full_name(),
             employee.full_name(),
             ))
