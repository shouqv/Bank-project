import unittest

import bank.file_management as file

class TestDBInteraction(unittest.TestCase):
    
    def test_open_file(self):
        with self.assertRaises(FileNotFoundError):
            file.open_file("non_existent_file.csv")