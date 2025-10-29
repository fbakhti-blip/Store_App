import unittest
from model import OrderItem
from controller import OrderItemController


class TestOrderItemController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = OrderItemController

    def test_save_order_item(self):
        """Test saving an order item"""
        status, message = self.controller.save(1, 1, 2, 100000, 5000, "Test order item")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_order_items(self):
        """Test finding all order items"""
        status, order_item_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(order_item_list, list)

    def test_find_by_id(self):
        """Test finding order item by id"""
        status, message = self.controller.save(1, 2, 3, 150000, 7500, "Test")
        if status:
            status_all, order_item_list = self.controller.find_all()
            if order_item_list:
                order_item_id = order_item_list[-1].order_item_id
                status, order_item = self.controller.find_by_id(order_item_id)
                self.assertTrue(status)

    def test_update_order_item(self):
        """Test updating an order item"""
        status, message = self.controller.save(2, 3, 4, 200000, 10000, "Before update")
        if status:
            status_all, order_item_list = self.controller.find_all()
            if order_item_list:
                order_item_id = order_item_list[-1].order_item_id
                status, message = self.controller.update(order_item_id, 2, 3, 5, 250000, 12500, "After update")
                self.assertTrue(status)

    def test_delete_order_item(self):
        """Test deleting an order item"""
        status, message = self.controller.save(1, 1, 1, 50000, 2500, "To delete")
        if status:
            status_all, order_item_list = self.controller.find_all()
            if order_item_list:
                order_item_id = order_item_list[-1].order_item_id
                status, message = self.controller.delete(order_item_id)
                self.assertTrue(status)

    def test_find_by_order_id(self):
        """Test finding order items by order id"""
        status, order_item_list = self.controller.find_by_order_id(1)
        self.assertTrue(status)
        self.assertIsInstance(order_item_list, list)

    def test_find_by_product_id(self):
        """Test finding order items by product id"""
        status, order_item_list = self.controller.find_by_product_id(1)
        self.assertTrue(status)
        self.assertIsInstance(order_item_list, list)

    def test_find_by_quantity_less_than(self):
        """Test finding order items by quantity less than"""
        status, order_item_list = self.controller.find_by_quantity_less_than(10)
        self.assertTrue(status)
        self.assertIsInstance(order_item_list, list)


if __name__ == "__main__":
    unittest.main()
