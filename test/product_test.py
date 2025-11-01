import unittest
from model import Product
from controller import ProductController


class TestProductController(unittest.TestCase):

    def test_save_product(self):
        """Test saving a product"""
        status, message = ProductController.save("Laptop", "Dell", "XPS15", "SN123456", "Electronics", "Piece",
                                                 "2025/12/31")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_products(self):
        """Test finding all products"""
        status, product_list = ProductController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(product_list, list)

    def test_find_by_id(self):
        """Test finding product by id"""
        status, message = ProductController.save("Mouse", "Logitech", "MX3", "SN789", "Electronics", "Piece", None)
        if status:
            status_all, product_list = ProductController.find_all()
            if product_list:
                product_id = product_list[-1].product_id
                status, product = ProductController.find_by_id(product_id)
                self.assertTrue(status)
                self.assertIsNotNone(product)

    def test_update_product(self):
        """Test updating a product"""
        status, message = ProductController.save("Keyboard", "Corsair", "K95", "SN456", "Electronics", "Piece", None)
        if status:
            status_all, product_list = ProductController.find_all()
            if product_list:
                product_id = product_list[-1].product_id
                status, message = ProductController.update(product_id, "Keyboard Pro", "Corsair", "K95", "SN456",
                                                           "Electronics", "Piece", None)
                self.assertTrue(status)

    def test_delete_product(self):
        """Test deleting a product"""
        status, message = ProductController.save("Monitor", "LG", "27GL850", "SN999", "Electronics", "Piece", None)
        if status:
            status_all, product_list = ProductController.find_all()
            if product_list:
                product_id = product_list[-1].product_id
                status, message = ProductController.delete(product_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_name_and_brand(self):
        """Test finding products by name and brand"""
        status, product_list = ProductController.find_by_name_and_brand("Laptop", "Dell")
        self.assertTrue(status)
        self.assertIsInstance(product_list, list)

    def test_find_by_category(self):
        """Test finding products by category"""
        status, product_list = ProductController.find_by_category("Electronics")
        self.assertTrue(status)
        self.assertIsInstance(product_list, list)

    def test_find_by_expire_date_until(self):
        """Test finding products by expiration date"""
        status, product_list = ProductController.find_by_expire_date_until("2025/12/31")
        self.assertTrue(status)
        self.assertIsInstance(product_list, list)

    def test_find_by_id_not_found(self):
        """Test finding non-existent product"""
        status, result = ProductController.find_by_id(999999)
        self.assertFalse(status)

    def test_update_nonexistent_product(self):
        """Test updating a non-existent product"""
        status, message = ProductController.update(999999, "Test", "Brand", "Model", "SN", "Category", "Number", None)
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
