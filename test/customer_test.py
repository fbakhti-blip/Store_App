import unittest
from model import Customer
from controller import CustomerController


class TestCustomerController(unittest.TestCase):

    def test_save_customer(self):
        """Test saving a customer"""
        status, message = CustomerController.save("Ahmad", "Rezaei", "09123456789", "Tehran_Iran_123")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_customers(self):
        """Test finding all customers"""
        status, customer_list = CustomerController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)

    def test_find_by_id(self):
        """Test finding customer by id"""
        status, message = CustomerController.save("Test", "Customer", "09987654321", "Test Address")
        if status:
            status_all, customer_list = CustomerController.find_all()
            if customer_list:
                customer_id = customer_list[-1].customer_id
                status, customer = CustomerController.find_by_id(customer_id)
                self.assertTrue(status)
                self.assertIsNotNone(customer)

    def test_update_customer(self):
        """Test updating a customer"""
        status, message = CustomerController.save("Update", "Test", "09111111111", "Address 1")
        if status:
            status_all, customer_list = CustomerController.find_all()
            if customer_list:
                customer_id = customer_list[-1].customer_id
                status, message = CustomerController.update(customer_id, "Updated", "Name", "09999999999",
                                                            "New Address")
                self.assertTrue(status)

    def test_delete_customer(self):
        """Test deleting a customer"""
        status, message = CustomerController.save("Delete", "Test", "09222222222", "Delete Address")
        if status:
            status_all, customer_list = CustomerController.find_all()
            if customer_list:
                customer_id = customer_list[-1].customer_id
                status, message = CustomerController.delete(customer_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_firstname_and_lastname(self):
        """Test finding customers by firstname and lastname"""
        status, customer_list = CustomerController.find_by_firstname_and_lastname("Ahmad", "Rezaei")
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)

    def test_find_by_phone_number(self):
        """Test finding customers by phone number"""
        status, customer_list = CustomerController.find_by_phone_number("09123456789")
        self.assertTrue(status)
        self.assertIsInstance(customer_list, list)

    def test_find_by_id_not_found(self):
        """Test finding non-existent customer"""
        status, result = CustomerController.find_by_id(999999)
        self.assertFalse(status)

    def test_update_nonexistent_customer(self):
        """Test updating a non-existent customer"""
        status, message = CustomerController.update(999999, "Test", "Name", "09999999999", "Test Address")
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
