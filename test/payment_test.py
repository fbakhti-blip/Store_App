import unittest
from model import Payment
from controller import PaymentController


class TestPaymentController(unittest.TestCase):

    def test_save_payment(self):
        """Test saving a payment"""
        status, message = PaymentController.save("income", "cash", "2024/01/01", 1, 500000, 1, "Payment description")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_payments(self):
        """Test finding all payments"""
        status, payment_list = PaymentController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_id(self):
        """Test finding payment by id"""
        status, message = PaymentController.save("expense", "card", "2024/01/02", 2, 200000, 2, "Test payment")
        if status:
            status_all, payment_list = PaymentController.find_all()
            if payment_list:
                payment_id = payment_list[-1].payment_id
                status, payment = PaymentController.find_by_id(payment_id)
                self.assertTrue(status)
                self.assertIsNotNone(payment)

    def test_update_payment(self):
        """Test updating a payment"""
        status, message = PaymentController.save("income", "check", "2024/01/03", 1, 300000, 1, "Before update")
        if status:
            status_all, payment_list = PaymentController.find_all()
            if payment_list:
                payment_id = payment_list[-1].payment_id
                status, message = PaymentController.update(payment_id, "income", "transfer", "2024/01/04", 1, 350000, 1,
                                                           "After update")
                self.assertTrue(status)

    def test_delete_payment(self):
        """Test deleting a payment"""
        status, message = PaymentController.save("expense", "cash", "2024/01/05", 2, 100000, 2, "To delete")
        if status:
            status_all, payment_list = PaymentController.find_all()
            if payment_list:
                payment_id = payment_list[-1].payment_id
                status, message = PaymentController.delete(payment_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_transaction_type(self):
        """Test finding payments by transaction type"""
        status, payment_list = PaymentController.find_by_transaction_type("income")
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_payment_type(self):
        """Test finding payments by payment type"""
        status, payment_list = PaymentController.find_by_payment_type("cash")
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_date_time_range(self):
        """Test finding payments by date range"""
        status, payment_list = PaymentController.find_by_date_time_range("2024/01/01", "2024/12/31")
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_date_time_range_and_customer_id(self):
        """Test finding payments by date range and customer id"""
        status, payment_list = PaymentController.find_by_date_time_range_and_customer_id("2024/01/01", "2024/12/31", 1)
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_date_time_range_and_employee_id(self):
        """Test finding payments by date range and employee id"""
        status, payment_list = PaymentController.find_by_date_time_range_and_employee_id("2024/01/01", "2024/12/31", 1)
        self.assertTrue(status)
        self.assertIsInstance(payment_list, list)

    def test_find_by_id_not_found(self):
        """Test finding non-existent payment"""
        status, result = PaymentController.find_by_id(999999)
        self.assertFalse(status)

    def test_update_nonexistent_payment(self):
        """Test updating a non-existent payment"""
        status, message = PaymentController.update(999999, "income", "cash", "2024/01/01", 1, 100000, 1, "Test")
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
