import unittest
from model import WarehouseTransaction
from controller import WarehouseTransactionController


class TestWarehouseTransactionController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = WarehouseTransactionController

    def test_save_warehouse_transaction(self):
        """Test saving a warehouse transaction"""
        status, message = self.controller.save(1, 10, "input", "2024/01/01", 1, 1)
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_warehouse_transactions(self):
        """Test finding all warehouse transactions"""
        status, transaction_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_id(self):
        """Test finding warehouse transaction by id"""
        status, message = self.controller.save(2, 5, "output", "2024/01/02", 1, 1)
        if status:
            status_all, transaction_list = self.controller.find_all()
            if transaction_list:
                transaction_id = transaction_list[-1].warehouse_transaction_id
                status, transaction = self.controller.find_by_id(transaction_id)
                self.assertTrue(status)

    def test_update_warehouse_transaction(self):
        """Test updating a warehouse transaction"""
        status, message = self.controller.save(3, 15, "input", "2024/01/03", 1, 1)
        if status:
            status_all, transaction_list = self.controller.find_all()
            if transaction_list:
                transaction_id = transaction_list[-1].warehouse_transaction_id
                status, message = self.controller.update(transaction_id, 3, 20, "input", "2024/01/04", 1, 1)
                self.assertTrue(status)

    def test_delete_warehouse_transaction(self):
        """Test deleting a warehouse transaction"""
        status, message = self.controller.save(1, 3, "output", "2024/01/05", 1, 1)
        if status:
            status_all, transaction_list = self.controller.find_all()
            if transaction_list:
                transaction_id = transaction_list[-1].warehouse_transaction_id
                status, message = self.controller.delete(transaction_id)
                self.assertTrue(status)

    def test_find_by_product_id(self):
        """Test finding transactions by product id"""
        status, transaction_list = self.controller.find_by_product_id(1)
        self.assertTrue(status)
        self.assertIsInstance(transaction_list, list)

    def test_find_by_transaction_type(self):
        """Test finding transactions by type"""
        status, transaction_list = self.controller.find_by_transaction_type("input")
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


if __name__ == "__main__":
    unittest.main()
