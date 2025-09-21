import unittest

import bank.file_management as file

class TestDBInteraction(unittest.TestCase):
    
    def test_open_file(self):
        with self.assertRaises(FileNotFoundError):
            file.open_file("non_existent_file.csv")
            
    def test_get_row(self):
        file.data_list = [
{'account_id': 10004, 'frst_name': 'stacey', 'last_name': 'abrams','password': 'DEU8_qw3y72$', 'balance_checking': 2000, 'balance_savings': 20000}]
        self.assertEqual(file.get_row(10004), file.data_list[0])
        # testing when not found
        self.assertEqual(file.get_row(10009), -1)
    