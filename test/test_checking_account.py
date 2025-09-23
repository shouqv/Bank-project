import unittest
import tempfile
from bank.file_management import FileManagement
import os

# to check later https://www.geeksforgeeks.org/python/python-testing-output-to-stdout/


class TestCheckingAccount(unittest.TestCase):
    def setUp(self):

        with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='') as temp:
            self.temp = temp
            # i removed some fields to simplfy test
            self.temp.write("account_id,first_name,balance_checking,balance_savings,status\n10001,suresh,2000,10000,active\n10002,james,10000,10000,active")
            self.temp.close()
        
        # needed to be passed 
        self.file = FileManagement(self.temp.name)
        
        

        
    def tearDown(self):
        os.remove(self.temp.name)
        
        
    def test_withdraw(self):
        pass
    
    def test_deposit(self):
        
        pass
    def test_transfer(self):
        pass
    
    def get_current_checking_balance(self):
        pass
    def check_if_account_exist(self):
        pass