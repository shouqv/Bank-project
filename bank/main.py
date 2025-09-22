from file_management import FileManagement

class Customer():
    # account_id =0
    def __init__(self, file_name):
        self.file_manager = FileManagement(file_name)
        
    def add_new_customer(self):
        account_id = input("Enter account id ")
        first_name = input("Enter first name ")
        last_name = input("Enter last name ")
        password = input("Enter your password ")
        print("Type None if you dont wish to create any of the below account")
        balance_checking = input("Chekcing account balance ")
        balance_savings = input("Saving account balance ")
        status="active"
        
        
        self.file_manager.add_row(
            account_id=account_id,
            frst_name=first_name,
            last_name=last_name,
            password=password,
            balance_checking=balance_checking,
            balance_savings=balance_savings,
            status=status
        )
    
        
        
        
    def login(self):
        account_id = int(input("Account id: "))
        password = input("Password: ")
        regestired_password = self.file_manager.get_field_info(account_id , "password")
        if password == regestired_password:
            return True
        else:
            return False
        
    def withdraw():
        pass
    def deposit():
        pass
    def transfer():
        pass

customer = Customer("data/bank.csv")

# customer.add_new_customer()

print(customer.login())
