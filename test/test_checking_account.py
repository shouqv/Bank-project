import unittest
import tempfile
from bank.file_management import FileManagement
from bank.checking_account import CheckingAccount
from bank.custome_exceptions import OverdraftRejectedError , OverdraftLimitExceededError , InactiveAccountError
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
        self.account = CheckingAccount()

        
    def tearDown(self):
        os.remove(self.temp.name)
        
        
    def test_withdraw(self):
        # in the expected value i subtracted the checking balance of the id 10001 you csan see its diffrent from the inital set up value
        expected_value = [{"account_id": 10001, "first_name": "suresh","balance_checking": 0, "balance_savings": 10000, "status": "active"},
                            {"account_id": 10002, "first_name": "james","balance_checking": 10000, "balance_savings": 10000, "status": "active"}]
        # normal case
        self.assertNotEqual(self.file.data_list , expected_value)
        self.account.withdraw(self.file, 10001, 2000 )
        self.assertEqual(self.file.data_list , expected_value)
        
        # subtracting more than the allowed limit of an overdraft = -100 including fee, it will be rejected
        with self.assertRaises(OverdraftRejectedError):
            self.account.withdraw(self.file, 10001, 200 )
        
        # now testing that the overdraft fee is added 
        self.account.withdraw(self.file, 10001, 10 )
        expected_value = [{"account_id": 10001, "first_name": "suresh","balance_checking": -45, "balance_savings": 10000, "status": "active"},
                            {"account_id": 10002, "first_name": "james","balance_checking": 10000, "balance_savings": 10000, "status": "active"}]
        self.assertEqual(self.file.data_list , expected_value)
        
        self.account.withdraw(self.file, 10001, 10 )
        expected_value = [{"account_id": 10001, "first_name": "suresh","balance_checking": -90, "balance_savings": 10000, "status": "active"},
                            {"account_id": 10002, "first_name": "james","balance_checking": 10000, "balance_savings": 10000, "status": "active"}]
        self.assertEqual(self.file.data_list , expected_value)
        
        # now testing if he did 2 overdraft attemppt, and tried to attempt to overdraft again the attempt limit error will be raised and the status changes to inactive 
        with self.assertRaises(OverdraftLimitExceededError):
            self.account.withdraw(self.file, 10001, 1 )
        expected_value = [{"account_id": 10001, "first_name": "suresh","balance_checking": -90, "balance_savings": 10000, "status": "inactive"},
                            {"account_id": 10002, "first_name": "james","balance_checking": 10000, "balance_savings": 10000, "status": "active"}]
        self.assertEqual(self.file.data_list , expected_value)
        
        #  now if he tried to do an operation on an inactive account, it will raise InactiveAccountError error 
        with self.assertRaises(InactiveAccountError):
            self.account.withdraw(self.file, 10001, 10 )
            
        
        
        
        
    
    # def test_deposit(self):
    #     pass
    # def test_transfer(self):
    #     pass
    
    # def get_current_checking_balance(self):
    #     pass
    # def check_if_account_exist(self):
    #     pass