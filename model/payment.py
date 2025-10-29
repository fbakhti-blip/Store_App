from tools.payment_validator import *


class Payment:
    def __init__(self, payment_id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                 description):
        self.payment_id = payment_id
        self.transaction_type = transaction_type
        self.payment_type = payment_type
        self.date_time = date_time
        self.customer_id = customer_id
        self.total_amount = total_amount
        self.employee_id = employee_id
        self.description = description

    def validate(self):
        transaction_type_validator(self.transaction_type)
        payment_type_validator(self.payment_type)
        date_time_validator(self.date_time)
        customer_id_validator(self.customer_id)
        total_amount_validator(self.total_amount)
        employee_id_validator(self.employee_id)
        description_validator(self.description)

    def __repr__(self):
        return f"{self.__dict__}"

    def to_tuple(self):
        from service import CustomerService, EmployeeService

        customer = CustomerService.find_by_id(self.customer_id)
        employee = EmployeeService.find_by_id(self.employee_id)

        return tuple((self.payment_id, self.transaction_type, self.payment_type,
                      self.date_time, customer.full_name(), self.total_amount, employee.full_name(), self.description))
