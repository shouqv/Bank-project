# crediting https://codingtechroom.com/question/test-if-another-method-was-called 
# for knowing how to test if a method is called correctly, as im not intrested in the logic cus its alresady was tested

import unittest
from bank.customer import Customer
import tempfile


class TestCustomer(unittest.TestCase):
    def setUp(self):
        with tempfile.NamedTemporaryFile(mode='w', delete=False, newline='') as temp:
            self.temp = temp
            self.temp.write("account_id,first_name,balance_checking,balance_savings,status\n10001,suresh,2000,10000,active\n10002,james,10000,10000,active")
            self.temp.close()

        # the temp file is needed by customer constructor/init
        self.customer = Customer(self.temp.name)
        
    def test_add_new_customer(self):
        pass
    
    
