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
            
    def deposit(self, account_id):
        account = input("deposit from: (checking/saving): ")
        if account == "checking":
            self.checking_account.deposit(self.file_manager ,account_id )
        elif account == "saving":
            self.saving_account.deposit(self.file_manager ,account_id)
    def transfer():
        pass


class CheckingAccount():
    def withdraw(self ,file, account_id ):
        current_balance_checking = file.get_field_info(account_id, "balance_checking")
        if str(current_balance_checking).lower() != "none":
            print(f"Current checking balance:{current_balance_checking}")
            amount = int(input("Amount: "))
            new_balance_checking = current_balance_checking - amount
            print(f"The new checking balance: {new_balance_checking}")
            file.update_row(account_id, "balance_checking" , new_balance_checking)
        else:
            answer = input("You dont have a checkingaccount, do you wish to create one? (yes/no)").lower()
            if answer == "yes":
                self.create_account(file,account_id )

    
    def deposit(self ,file, account_id ):
        current_balance_checking = file.get_field_info(account_id, "balance_checking")
        if str(current_balance_checking).lower() != "none":
            print(f"Current checking balance:{current_balance_checking}")
            amount = int(input("Amount: "))
            new_balance_checking = current_balance_checking + amount
            print(f"The new checking balance: {new_balance_checking}")
            file.update_row(account_id, "balance_checking" , new_balance_checking)
        else:
            answer = input("You dont have a checkingaccount, do you wish to create one? (yes/no) ").lower()
            if answer == "yes":
                self.create_account(file,account_id )
    
    def transfer():
        pass
    
    def create_account(self,file, account_id):
        new_balance_checking = int(input("Enter the chekcing account balance: "))
        file.update_row(account_id,"balance_checking",new_balance_checking)
        print(f"the checking account has been created")
        

class SavingAccount():
    def withdraw(self ,file, account_id ):
        current_balance_saving = file.get_field_info(account_id, "balance_savings")
        if str(current_balance_saving).lower() != "none":
            print(f"Current saving balance:{current_balance_saving}")
            amount = int(input("Amount: "))
            new_balance_saving = current_balance_saving - amount
            print(f"The new saving balance: {new_balance_saving}")
            file.update_row(account_id, "balance_checking" , new_balance_saving)
        else:
            answer = input("You dont have a saving account, do you wish to create one? (yes/no) ").lower()
            if answer == "yes":
                self.create_account(file,account_id )
    
    def deposit(self,file,account_id):
        current_balance_saving = file.get_field_info(account_id, "balance_savings")
        if str(current_balance_saving).lower() != "none":
            print(f"Current saving balance:{current_balance_saving}")
            amount = int(input("Amount: "))
            new_balance_saving = current_balance_saving + amount
            print(f"The new checking balance: {new_balance_saving}")
            file.update_row(account_id, "balance_checking" , new_balance_saving)
        else:
            answer = input("You dont have a saving account, do you wish to create one? (yes/no) ").lower()
            if answer == "yes":
                self.create_account(file,account_id )
    
    def transfer():
        pass
    
    def create_account(self, file, account_id):
        new_balance_saving = int(input("Enter the saving account balance: "))
        file.update_row(account_id,"balance_savings",new_balance_saving)
        print(f"the saving account has been created")
    
    
    
    
customer = Customer("data/bank.csv")

# # customer.add_new_customer()

# customer.withdraw(10)
# customer.deposit(10)