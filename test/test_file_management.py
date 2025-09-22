import unittest

from bank.file_management import FileManagement

class TestDBInteraction(unittest.TestCase):
    def setUp(self):
        self.file = FileManagement("")
    
    def test_is_number(self):
        self.assertTrue(self.file.is_number("11"))
        self.assertTrue(self.file.is_number("-11"))
        self.assertFalse(self.file.is_number("hello"))
        
        
    def test_load_data(self):
        with self.assertRaises(FileNotFoundError):
            FileManagement("non_existent_file.csv")
            
    def test_get_row(self):
        self.file.data_list = [
{'account_id': 10004, 'frst_name': 'stacey', 'last_name': 'abrams','password': 'DEU8_qw3y72$', 'balance_checking': 2000, 'balance_savings': 20000}]
        self.assertEqual(self.file.get_row(10004), self.file.data_list[0])
        # testing when not found
        self.assertEqual(self.file.get_row(10009), -1)
    
    def test_write_to_file(self):
        pass
    
    def test_update_row(self):
        pass
    
    def test_add_row(self):
        pass