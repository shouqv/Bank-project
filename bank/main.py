from file_management import FileManagement

class Customer():
    # account_id =0
    def __init__(self, file_name):
        self.file_manager = FileManagement(file_name)
        self.checking_account = CheckingAccount()
        self.saving_account = SavingAccount()
        
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
    
        
        
        
    def login(self,account_id ):
        password = input("Password: ")
        regestired_password = self.file_manager.get_field_info(account_id , "password")
        if password == regestired_password:
            return True
        else:
            return False
        
    def withdraw(self,account_id):
        account = input("withdraw from: (checking/saving): ")
        if account == "checking":
            self.checking_account.withdraw(self.file_manager ,account_id )
        elif account == "saving":
            self.saving_account.withdraw(self.file_manager ,account_id)
            
    def deposit():
        pass
    def transfer():
        pass


class CheckingAccount():
    def withdraw(self ,file, account_id ):
        current_balance_checking = file.get_field_info(account_id, "balance_checking")
        print(f"Current checking balance:{current_balance_checking}")
        amount = int(input("Amount: "))
        new_balance_checking = current_balance_checking - amount
        print(f"The new checking balance: {new_balance_checking}")
        file.update_row(account_id, "balance_checking" , new_balance_checking)
        
    
    def deposit():
        pass
    
    def transfer():
        pass
    
    def add_account():
        pass

class SavingAccount():
    def withdraw(self ,file, account_id ):
        current_balance_saving = file.get_field_info(account_id, "balance_savings")
        print(f"Current saving balance:{current_balance_saving}")
        amount = int(input("Amount: "))
        new_balance_saving = current_balance_saving - amount
        print(f"The new saving balance: {new_balance_saving}")
        file.update_row(account_id, "balance_checking" , new_balance_saving)
    
    def deposit():
        pass
    
    def transfer():
        pass
    def add_account():
        pass
    
    
    
    
customer = Customer("data/bank.csv")

# customer.add_new_customer()

customer.withdraw(10)
