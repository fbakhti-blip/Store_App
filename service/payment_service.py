from repository import PaymentRepository


class PaymentService:
    payment_repository = PaymentRepository()

    @classmethod
    def save(cls, payment):
        return cls.payment_repository.save(payment)

    @classmethod
    def update(cls, payment):
        payment_result = cls.payment_repository.find_by_id(payment.payment_id)
        if payment_result:
            return cls.payment_repository.update(payment)
        else:
            raise Exception("Payment Not Found !!!")

    @classmethod
    def delete(cls, payment_id):
        payment = cls.payment_repository.find_by_id(payment_id)
        if payment:
            cls.payment_repository.delete(payment_id)
            return payment
        else:
            raise Exception("Payment Not Found !!!")

    @classmethod
    def find_all(cls):
        return cls.payment_repository.find_all()

    @classmethod
    def find_by_id(cls, payment_id):
        payment = cls.payment_repository.find_by_id(payment_id)
        if payment:
            return payment
        else:
            raise Exception("Payment Not Found !!!")

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        return cls.payment_repository.find_by_transaction_type(transaction_type)

    @classmethod
    def find_by_payment_type(cls, payment_type):
        return cls.payment_repository.find_by_payment_type(payment_type)

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        return cls.payment_repository.find_by_date_time_range(start_date_time, end_date_time)

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        return cls.payment_repository.find_by_date_time_range_and_customer_id(start_date_time, end_date_time,
                                                                              customer_id)

    @classmethod
    def find_by_date_time_range_and_employee_id(cls, start_date_time, end_date_time, employee_id):
        return cls.payment_repository.find_by_date_time_range_and_employee_id(start_date_time, end_date_time,
                                                                              employee_id)
