import unittest
from model import Warehouse
from controller import WarehouseController


class TestWarehouseController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = WarehouseController

    def test_save_warehouse(self):
        """Test saving a warehouse"""
        status, message = self.controller.save(1, 100)
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_warehouses(self):
        """Test finding all warehouses"""
        status, warehouse_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(warehouse_list, list)

    def test_find_by_id(self):
        """Test finding warehouse by id"""
        status, message = self.controller.save(2, 50)
        if status:
            status_all, warehouse_list = self.controller.find_all()
            if warehouse_list:
                warehouse_id = warehouse_list[-1].warehouse_id
                status, warehouse = self.controller.find_by_id(warehouse_id)
                self.assertTrue(status)

    def test_update_warehouse(self):
        """Test updating a warehouse"""
        status, message = self.controller.save(3, 75)
        if status:
            status_all, warehouse_list = self.controller.find_all()
            if warehouse_list:
                warehouse_id = warehouse_list[-1].warehouse_id
                status, message = self.controller.update(warehouse_id, 3, 150)
                self.assertTrue(status)

    def test_delete_warehouse(self):
        """Test deleting a warehouse"""
        status, message = self.controller.save(4, 25)
        if status:
            status_all, warehouse_list = self.controller.find_all()
            if warehouse_list:
                warehouse_id = warehouse_list[-1].warehouse_id
                status, message = self.controller.delete(warehouse_id)
                self.assertTrue(status)

    def test_find_by_product_id(self):
        """Test finding warehouses by product id"""
        status, warehouse_list = self.controller.find_by_product_id(1)
        self.assertTrue(status)
        self.assertIsInstance(warehouse_list, list)

    def test_find_by_quantity_less_than(self):
        """Test finding warehouses with quantity less than"""
        status, warehouse_list = self.controller.find_by_quantity_less_than(100)
        self.assertTrue(status)
        self.assertIsInstance(warehouse_list, list)

    def test_find_by_quantity_more_than(self):
        """Test finding warehouses with quantity more than"""
        status, warehouse_list = self.controller.find_by_quantity_more_than(50)
        self.assertTrue(status)
        self.assertIsInstance(warehouse_list, list)


if __name__ == "__main__":
    unittest.main()
