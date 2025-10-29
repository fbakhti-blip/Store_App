from model import Payment
from service import PaymentService
from tools.logging import Logger


class PaymentController:
    @classmethod
    def save(cls, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id, description):
        try:
            payment = Payment(None, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            payment.validate()
            payment = PaymentService.save(payment)
            Logger.info(f"Payment {payment} saved")
            return True, f"Payment Saved Successfully"
        except Exception as e:
            Logger.error(f"Payment Save Error: {e}")
            return False, e

    @classmethod
    def update(cls, payment_id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
               description):
        try:
            payment = Payment(payment_id, transaction_type, payment_type, date_time, customer_id, total_amount, employee_id,
                              description)
            payment.validate()
            payment = PaymentService.update(payment)
            Logger.info(f"Payment {payment} updated")
            return True, "Payment Updated Successfully"
        except Exception as e:
            Logger.error(f"Payment Update Error: {e}")
            return False, e

    @classmethod
    def delete(cls, payment_id):
        try:
            payment = PaymentService.delete(payment_id)
            Logger.info(f"Payment {payment} deleted")
            return True, f"Payment Deleted Successfully"
        except Exception as e:
            Logger.error(f"Payment Delete Error: {e}")
            return False, e

    @classmethod
    def find_all(cls):
        try:
            payment_list = PaymentService.find_all()
            Logger.info("Payment FindAll")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindAll Error: {e}")
            return False, e

    @classmethod
    def find_by_id(cls, payment_id):
        try:
            payment = PaymentService.find_by_id(payment_id)
            Logger.info(f"Payment FindById {payment_id}")
            return True, payment
        except Exception as e:
            Logger.error(f"{e} With Id {payment_id}")
            return False, e

    @classmethod
    def find_by_transaction_type(cls, transaction_type):
        try:
            payment_list = PaymentService.find_by_transaction_type(transaction_type)
            Logger.info(f"Payment FindByTransactionType {transaction_type}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByTransactionType Error: {e}")
            return False, e

    @classmethod
    def find_by_payment_type(cls, payment_type):
        try:
            payment_list = PaymentService.find_by_payment_type(payment_type)
            Logger.info(f"Payment FindByPaymentType {payment_type}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByPaymentType Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range(cls, start_date_time, end_date_time):
        try:
            payment_list = PaymentService.find_by_date_time_range(start_date_time, end_date_time)
            Logger.info(f"Payment FindByDateTimeRange {start_date_time} to {end_date_time}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByDateTimeRange Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_customer_id(cls, start_date_time, end_date_time, customer_id):
        try:
            payment_list = PaymentService.find_by_date_time_range_and_customer_id(start_date_time, end_date_time, customer_id)
            Logger.info(f"Payment FindByDateTimeRangeAndCustomerId {start_date_time} to {end_date_time}, customer: {customer_id}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByDateTimeRangeAndCustomerId Error: {e}")
            return False, e

    @classmethod
    def find_by_date_time_range_and_employee_id(cls, start_date_time, end_date_time, employee_id):
        try:
            payment_list = PaymentService.find_by_date_time_range_and_employee_id(start_date_time, end_date_time, employee_id)
            Logger.info(f"Payment FindByDateTimeRangeAndEmployeeId {start_date_time} to {end_date_time}, employee: {employee_id}")
            return True, payment_list
        except Exception as e:
            Logger.error(f"Payment FindByDateTimeRangeAndEmployeeId Error: {e}")
            return False, e
