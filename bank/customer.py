from .file_management import FileManagement
from .checking_account import CheckingAccount
from .saving_account import SavingAccount

class Customer():
    # account_id =0
    def __init__(self, file_name):
        self.file_manager = FileManagement(file_name)
        self.checking_account = CheckingAccount()
        self.saving_account = SavingAccount()
        
    def add_new_customer(self, account_id, first_name, last_name, password, balance_checking, balance_savings):
        status = "active"
        self.file_manager.add_row(
            account_id=account_id,
            first_name=first_name,
            last_name=last_name,
            password=password,
            balance_checking=balance_checking,
            balance_savings=balance_savings,
            status=status)

    
        
        
        
    def login(self,account_id, password):
        regestired_password = self.file_manager.get_field_info(account_id , "password")
        if password == regestired_password:
            return True
        else:
            return False
        
    def withdraw(self,account_id , account, amount ):
        if account == "checking":
            self.checking_account.withdraw(self.file_manager ,account_id, amount)
        elif account == "saving":
            self.saving_account.withdraw(self.file_manager ,account_id , amount)
        else:
            print("invalid choice")
            
    def deposit(self, account_id,account, amount):

        if account == "checking":
            self.checking_account.deposit(self.file_manager ,account_id , amount)
        elif account == "saving":
            self.saving_account.deposit(self.file_manager ,account_id, amount)
        else:
            print("invalid choice")
            
    def transfer(self,account_id , choice, amount, from_account=None, other_customer=None):
        # print("Please enter a valid choice")
        # print("a) Transfer from checking to saving: ")
        # print("b) Transfer from saving to checking: ")
        # print("c) Transfer to another customer account: ")
        # choice = input("Choice: ").lower()
        # self.get_current_balance(account_id , "checking")
        # self.get_current_balance(account_id , "saving")
        
        # if choice.lower() == "c":
        #     account = input("Transfer from checking or saving (checking/saving): ")            
        # amount = int(input("Amount: "))
        
        match choice:
            case "a":
                self.saving_account.transfer(self.file_manager,account_id,self.checking_account,amount)
            case "b":
                self.checking_account.transfer(self.file_manager,account_id,self.saving_account,amount)
            case "c":
                if not from_account or not other_customer:
                    raise ValueError("the account to transfer from and the id of the other customer must be provided for this choice")
                
                if not self.checking_account.check_if_account_exist(self.file_manager,other_customer):
                    raise ValueError(f"The customer {other_customer} does not have an account, cant transfer!")
                self.withdraw(account_id , from_account, amount)
                # other_customer = int(input("Enter the account id to transfer it to: "))
                if other_customer != account_id:
                    self.checking_account.deposit(self.file_manager ,other_customer,amount, False)
            case _:
                print("Invalid choice")
                
    def get_current_balance(self ,account_id , account ):
        if account == "checking":
            return self.checking_account.get_current_checking_balance(self.file_manager ,account_id )
        elif account == "saving":
            return self.saving_account.get_current_saving_balance(self.file_manager ,account_id)