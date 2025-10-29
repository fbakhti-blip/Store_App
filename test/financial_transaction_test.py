import unittest
from model import FinancialTransaction
from controller import FinancialTransactionController


class TestFinancialTransactionController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = FinancialTransactionController

    def test_save_financial_transaction(self):
        """Test saving a financial transaction"""
        status, message = self.controller.save("sale", 1, 1, 500000, "2024/01/01", 1, "Sale transaction")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_financial_transactions(self):
        """Test finding all financial transactions"""
        status, transaction_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_id(self):
        """Test finding financial transaction by id"""
        status, message = self.controller.save("purchase", 2, 2, 300000, "2024/01/02", 2, "Purchase")
        if status:
            status_all, transaction_list = self.controller.find_all()
            if transaction_list:
                transaction_id = transaction_list[-1].financial_transaction_id
                status, transaction = self.controller.find_by_id(transaction_id)
                self.assertTrue(status)

    def test_update_financial_transaction(self):
        """Test updating a financial transaction"""
        status, message = self.controller.save("expense", 1, 1, 100000, "2024/01/03", 1, "Before update")
        if status:
            status_all, transaction_list = self.controller.find_all()
            if transaction_list:
                transaction_id = transaction_list[-1].financial_transaction_id
                status, message = self.controller.update(transaction_id, "expense", 1, 1, 150000, "2024/01/04", 1, "After update")
                self.assertTrue(status)

    def test_delete_financial_transaction(self):
        """Test deleting a financial transaction"""
        status, message = self.controller.save("salary", 1, 2, 2000000, "2024/01/05", 1, "To delete")
        if status:
            status_all, transaction_list = self.controller.find_all()
            if transaction_list:
                transaction_id = transaction_list[-1].financial_transaction_id
                status, message = self.controller.delete(transaction_id)
                self.assertTrue(status)

    def test_find_by_transaction_type(self):
        """Test finding transactions by type"""
        status, transaction_list = self.controller.find_by_transaction_type("sale")
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_customer_id(self):
        """Test finding transactions by customer id"""
        status, transaction_list = self.controller.find_by_customer_id(1)
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_employee_id(self):
        """Test finding transactions by employee id"""
        status, transaction_list = self.controller.find_by_employee_id(1)
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_payment_id(self):
        """Test finding transactions by payment id"""
        status, transaction_list = self.controller.find_by_payment_id(1)
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_date_time_range(self):
        """Test finding transactions by date range"""
        status, transaction_list = self.controller.find_by_date_time_range("2024/01/01", "2024/12/31")
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)


if __name__ == "__main__":
    unittest.main()
