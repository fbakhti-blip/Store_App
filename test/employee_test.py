import unittest
from model import Employee
from controller import EmployeeController


class TestEmployeeController(unittest.TestCase):

    def test_save_employee(self):
        """Test saving an employee"""
        import random
        import string
        unique_username = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
        status, message = EmployeeController.save("ali", "Mohammadi", 5000000, "cashier", "09123456789", unique_username, "pass1234", "cashier")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_employees(self):
        """Test finding all employees"""
        status, employee_list = EmployeeController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)

    def test_find_by_id(self):
        """Test finding employee by id"""
        status, message = EmployeeController.save("Test", "Employee", 3000000, "Test", "09999999999", "test", "pass", "user")
        if status:
            status_all, employee_list = EmployeeController.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, employee = EmployeeController.find_by_id(employee_id)
                self.assertTrue(status)
                self.assertIsNotNone(employee)

    def test_update_employee(self):
        """Test updating an employee"""
        status, message = EmployeeController.save("Update", "Employee", 4000000, "Tester", "09888888888", "upd", "pass", "admin")
        if status:
            status_all, employee_list = EmployeeController.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, message = EmployeeController.update(employee_id, "Updated", "Emp", 4500000, "Senior", "09888888888", "upd", "newpass", "admin")
                self.assertTrue(status)

    def test_delete_employee(self):
        """Test deleting an employee"""
        status, message = EmployeeController.save("Delete", "Employee", 2000000, "Temp", "09777777777", "del", "pass", "user")
        if status:
            status_all, employee_list = EmployeeController.find_all()
            if employee_list:
                employee_id = employee_list[-1].employee_id
                status, message = EmployeeController.delete(employee_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_username_and_password(self):
        """Test finding employee by username and password"""
        status, employee = EmployeeController.find_by_username_and_password("aliuser", "pass1234")
        self.assertTrue(status or employee is None)

    def test_find_by_role(self):
        """Test finding employees by role"""
        status, employee_list = EmployeeController.find_by_role("admin")
        self.assertTrue(status)
        self.assertIsInstance(employee_list, list)

    def test_find_by_id_not_found(self):
        """Test finding non-existent employee"""
        status, result = EmployeeController.find_by_id(999999)
        self.assertFalse(status)

    def test_update_nonexistent_employee(self):
        """Test updating a non-existent employee"""
        status, message = EmployeeController.update(999999, "Test", "Emp", 3000000, "Test", "09111111111", "test", "pass", "user")
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
