import unittest
from model import Bank
from controller import BankController


class TestBankController(unittest.TestCase):

    def test_save_bank(self):
        """Test saving a bank"""
        status, message = BankController.save("Melli Bank", "saving", 1000000, "Test Description")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_banks(self):
        """Test finding all banks"""
        status, bank_list = BankController.find_all()
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)

    def test_find_by_id(self):
        """Test finding bank by id"""
        # First save a bank
        status, message = BankController.save("Test Bank", "999999", 500000, "Test")
        if status:
            # Find all to get the id of the last saved bank
            status_all, bank_list = BankController.find_all()
            if bank_list:
                bank_id = bank_list[-1].bank_id
                status, bank = BankController.find_by_id(bank_id)
                self.assertTrue(status)
                self.assertIsNotNone(bank)

    def test_update_bank(self):
        """Test updating a bank"""
        # First save a bank
        status, message = BankController.save("Update Test Bank", "checking", 200000, "Before Update")
        if status:
            status_all, bank_list = BankController.find_all()
            if bank_list:
                bank_id = bank_list[-1].bank_id
                status, message = BankController.update(bank_id, "Updated Bank", "checking", 300000, "After Update")
                self.assertTrue(status)

    def test_delete_bank(self):
        """Test deleting a bank"""
        # First save a bank
        status, message = BankController.save("Delete Test Bank", "current", 150000, "To Be Deleted")
        if status:
            status_all, bank_list = BankController.find_all()
            if bank_list:
                bank_id = bank_list[-1].bank_id
                status, message = BankController.delete(bank_id)
                self.assertTrue(status)
                self.assertIn("Deleted Successfully", message)

    def test_find_by_name(self):
        """Test finding banks by name"""
        status, bank_list = BankController.find_by_name("Melli")
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)

    def test_find_by_account(self):
        """Test finding banks by account"""
        status, bank_list = BankController.find_by_account("saving")
        self.assertTrue(status)
        self.assertIsInstance(bank_list, list)

    def test_find_by_id_not_found(self):
        """Test finding non-existent bank"""
        status, result = BankController.find_by_id(999999)
        self.assertFalse(status)

    def test_update_nonexistent_bank(self):
        """Test updating a non-existent bank"""
        status, message = BankController.update(999999, "Test", "account", 1000, "Test")
        self.assertFalse(status)


if __name__ == "__main__":
    unittest.main()
