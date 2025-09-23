from .custome_exceptions import OverdraftRejectedError , AccountIsNoneError

class SavingAccount():
    def withdraw(self ,file, account_id ,amount, flag = True):
        current_balance_saving = self.get_current_saving_balance(file,account_id)
        if self.check_if_account_exist(file,account_id):

            amount = int(amount)
            
            if amount > current_balance_saving:
                # print("Not enought money in saving account for this transaction. Operation canceled")
                # return
                raise OverdraftRejectedError("Cant have an overdraft of a saving account!")
            new_balance_saving = current_balance_saving - amount
            if flag:
                print(f"The new saving balance: {new_balance_saving}")
            file.update_row(account_id, "balance_savings" , new_balance_saving)
            
        else:
            # answer = input("You dont have a saving account, do you wish to create one? (yes/no) ").lower()
            # if answer == "yes":
            #     self.create_account(file,account_id )
            raise AccountIsNoneError(f"Error: the saving account with id={account_id}, have not been initated yet", "balance_savings")
    
    def deposit(self,file,account_id ,amount,flag=True):
        current_balance_saving = self.get_current_saving_balance(file , account_id)
        if self.check_if_account_exist(file,account_id):
        
            amount = int(amount)

            new_balance_saving = current_balance_saving + amount
            if flag:
                print(f"The new saving balance: {new_balance_saving}")
                
            file.update_row(account_id, "balance_savings" , new_balance_saving)
        else:
            # answer = input("You dont have a saving account, do you wish to create one? (yes/no) ").lower()
            # if answer == "yes":
            #     self.create_account(file,account_id )
            raise AccountIsNoneError(f"Error: the saving account with id={account_id}, have not been initated yet", "balance_savings")
    
    def transfer(self,file ,  account_id,checking_account , amount):
        checking_account.withdraw(file,account_id, amount)
        self.deposit(file,account_id , amount)
        
    
    # def create_account(self, file, account_id):
    #     new_balance_saving = int(input("Enter the saving account balance: "))
    #     file.update_row(account_id,"balance_savings",new_balance_saving)
    #     print(f"the saving account has been created")
        
    
    def get_current_saving_balance(self,file,account_id):
        current_saving_balance = file.get_field_info(account_id, "balance_savings")
        return current_saving_balance
        
        
    def check_if_account_exist(self,file ,account_id):
        current_balance = self.get_current_saving_balance(file,account_id)
        if str(current_balance).lower() == "none":
            return False
        else:
            return True
        