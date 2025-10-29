import unittest
from model import Sample
from controller import SampleController


class TestSampleController(unittest.TestCase):

    def setUp(self):
        """Setup method called before each test method"""
        self.controller = SampleController

    def test_save_sample(self):
        """Test saving a sample"""
        status, message = self.controller.save("Sample 1", "This is a test sample")
        self.assertTrue(status)
        self.assertIn("Saved Successfully", message)

    def test_find_all_samples(self):
        """Test finding all samples"""
        status, sample_list = self.controller.find_all()
        self.assertTrue(status)
        self.assertIsInstance(sample_list, list)

    def test_find_by_id(self):
        """Test finding sample by id"""
        status, message = self.controller.save("Sample 2", "Another test sample")
        if status:
            status_all, sample_list = self.controller.find_all()
            if sample_list:
                sample_id = sample_list[-1].sample_id
                status, sample = self.controller.find_by_id(sample_id)
                self.assertTrue(status)

    def test_update_sample(self):
        """Test updating a sample"""
        status, message = self.controller.save("Sample 3", "Before update")
        if status:
            status_all, sample_list = self.controller.find_all()
            if sample_list:
                sample_id = sample_list[-1].sample_id
                status, message = self.controller.update(sample_id, "Updated Sample", "After update")
                self.assertTrue(status)

    def test_delete_sample(self):
        """Test deleting a sample"""
        status, message = self.controller.save("Sample 4", "To delete")
        if status:
            status_all, sample_list = self.controller.find_all()
            if sample_list:
                sample_id = sample_list[-1].sample_id
                status, message = self.controller.delete(sample_id)
                self.assertTrue(status)


if __name__ == "__main__":
    unittest.main()
