from repository import OrderRepository


class OrderService:
    order_repository = OrderRepository()

    @classmethod
    def save(cls, order):
        return cls.order_repository.save(order)

    @classmethod
    def update(cls, order):
        order_result = cls.order_repository.find_by_id(order.order_id)
        if order_result:
            return cls.order_repository.update(order)
        else:
            raise Exception("Order Not Found !!!")

    @classmethod
    def delete(cls, order_id):
        order = cls.order_repository.find_by_id(order_id)
        if order:
            cls.order_repository.delete(order_id)
            return order
        else:
            raise Exception("Order Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.order_repository.find_all()

    @classmethod
    def find_by_id(cls, order_id):
        order = cls.order_repository.find_by_id(order_id)
        if order:
            return order
        else:
            raise Exception("Order Not Found !!!")

    @classmethod
    def find_by_order_type(cls, order_type):
        return cls.order_repository.find_by_order_type(order_type)

    @classmethod
    def find_by_customer_id(cls, customer_id):
        return cls.order_repository.find_by_customer_id(customer_id)

    @classmethod
    def find_by_employee_id(cls, employee_id):
        return cls.order_repository.find_by_employee_id(employee_id)

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        return cls.order_repository.find_by_date_time_range(start_date_time, end_date_time)

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        return cls.order_repository.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
