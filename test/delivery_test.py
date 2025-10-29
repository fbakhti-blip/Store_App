import unittest
from model import Delivery
from controller import DeliveryController


class TestDeliveryController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = DeliveryController

    def test_save_delivery(self):
        """Test saving a delivery"""
        status, message = self.controller.save("Ali", "Ahmadi", "Tehran, Street 1", "Express delivery")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_deliveries(self):
        """Test finding all deliveries"""
        status, delivery_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(delivery_list, list)

    def test_find_by_id(self):
        """Test finding delivery by id"""
        status, message = self.controller.save("Reza", "Mohammadi", "Isfahan, Street 2", "Standard delivery")
        if status:
            status_all, delivery_list = self.controller.find_all()
            if delivery_list:
                delivery_id = delivery_list[-1].delivery_id
                status, delivery = self.controller.find_by_id(delivery_id)
                self.assertTrue(status)

    def test_update_delivery(self):
        """Test updating a delivery"""
        status, message = self.controller.save("Hassan", "Karimi", "Shiraz, Street 3", "Test")
        if status:
            status_all, delivery_list = self.controller.find_all()
            if delivery_list:
                delivery_id = delivery_list[-1].delivery_id
                status, message = self.controller.update(delivery_id, "Updated", "Name", "New Address", "Updated description")
                self.assertTrue(status)

    def test_delete_delivery(self):
        """Test deleting a delivery"""
        status, message = self.controller.save("Mohammad", "Zare", "Qom, Street 4", "Delete test")
        if status:
            status_all, delivery_list = self.controller.find_all()
            if delivery_list:
                delivery_id = delivery_list[-1].delivery_id
                status, message = self.controller.delete(delivery_id)
                self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
