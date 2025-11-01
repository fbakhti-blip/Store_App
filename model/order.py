from tools.order_validator import *


class Order:
    def __init__(self, order_id, order_type, customer_id, employee_id, date_time,
                 payment_id, warehouse_transaction_id, tax=None, total_discount=None,
                 total_amount=None):
        self.order_id = order_id
        self.order_type = order_type
        self.customer_id = customer_id
        self.employee_id = employee_id
        self.date_time = date_time
        self.payment_id = payment_id
        self.warehouse_transaction_id = warehouse_transaction_id
        self.tax = tax
        self.total_discount = total_discount
        self.total_amount = total_amount

    def validate(self):
        datetime_validator(self.date_time)
        tax_validator(self.tax)
        total_discount_validator(self.total_discount)
        total_amount_validator(self.total_amount)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        from service import CustomerService, EmployeeService

        customer = CustomerService.find_by_id(self.customer_id)
        employee = EmployeeService.find_by_id(self.employee_id)

        return tuple((
            self.order_id,
            self.order_type,
            customer.full_name(),
            employee.full_name(),
            self.date_time,
            self.payment_id,
            self.warehouse_transaction_id,
            self.tax,
            self.total_discount,
            self.total_amount))
