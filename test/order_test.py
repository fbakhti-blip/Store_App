import unittest
from model import Order
from controller import OrderController


class TestOrderController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = OrderController

    def test_save_order(self):
        """Test saving an order"""
        status, message = self.controller.save("frooshe", 1, 1, "2024/01/01", 1, 1, 100000, 5000, 95000)
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_orders(self):
        """Test finding all orders"""
        status, order_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(order_list, list)

    def test_find_by_id(self):
        """Test finding order by id"""
        status, message = self.controller.save("kharid", 1, 1, "2024/01/02", 2, 2, 200000, 10000, 180000)
        if status:
            status_all, order_list = self.controller.find_all()
            if order_list:
                order_id = order_list[-1].order_id
                status, order = self.controller.find_by_id(order_id)
                self.assertTrue(status)

    def test_update_order(self):
        """Test updating an order"""
        status, message = self.controller.save("frooshe", 2, 2, "2024/01/03", 3, 3, 150000, 7500, 142500)
        if status:
            status_all, order_list = self.controller.find_all()
            if order_list:
                order_id = order_list[-1].order_id
                status, message = self.controller.update(order_id, "updated", 2, 2, "2024/01/04", 3, 3, 160000, 8000, 152000)
                self.assertTrue(status)

    def test_delete_order(self):
        """Test deleting an order"""
        status, message = self.controller.save("kharid", 1, 1, "2024/01/05", 1, 1, 100000, 5000, 95000)
        if status:
            status_all, order_list = self.controller.find_all()
            if order_list:
                order_id = order_list[-1].order_id
                status, message = self.controller.delete(order_id)
                self.assertTrue(status)

    def test_find_by_order_type(self):
        """Test finding orders by type"""
        status, order_list = self.controller.find_by_order_type("frooshe")
        self.assertTrue(status)
        self.assertIsInstance(order_list, list)

    def test_find_by_customer_id(self):
        """Test finding orders by customer id"""
        status, order_list = self.controller.find_by_customer_id(1)
        self.assertTrue(status)
        self.assertIsInstance(order_list, list)

    def test_find_by_employee_id(self):
        """Test finding orders by employee id"""
        status, order_list = self.controller.find_by_employee_id(1)
        self.assertTrue(status)
        self.assertIsInstance(order_list, list)

    def test_find_by_date_time_range(self):
        """Test finding orders by date range"""
        status, order_list = self.controller.find_by_date_time_range("2024/01/01", "2024/12/31")
        self.assertTrue(status)
        self.assertIsInstance(order_list, list)


if __name__ == "__main__":
    unittest.main()
