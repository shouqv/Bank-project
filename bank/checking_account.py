
class CheckingAccount():
    overdrafts_count = {}
    
    def withdraw(self ,file, account_id, amount , flag=True):
        status = file.get_field_info(account_id, "status").lower()
        
        current_balance_checking = self.get_current_checking_balance(file,account_id)
        if status == "active":
            # if str(current_balance_checking).lower() != "none":
            if self.check_if_account_exist(file,account_id):


                amount = int(amount)
                new_balance_checking = current_balance_checking - amount

                if account_id not in CheckingAccount.overdrafts_count:
                    CheckingAccount.overdrafts_count[account_id] = 0



                if CheckingAccount.overdrafts_count[account_id] >= 2:
                    file.update_row(account_id, "status" , "inactive")

                    print("You have exceeded the overcraft limit, account deactivated")
                    return

                if amount > current_balance_checking:
                    if new_balance_checking - 35 < -100:
                        print("you have exceeded the limit of overdrafts! operation canceled")
                        return 
                    else:
                        if account_id in CheckingAccount.overdrafts_count:
                            if CheckingAccount.overdrafts_count[account_id] <3:
                                new_balance_checking -= 35
                                print("Overdraft! 35 fee applied.")
                                CheckingAccount.overdrafts_count[account_id] +=1


                if flag:
                    print(f"The new checking balance: {new_balance_checking}")
                file.update_row(account_id, "balance_checking" , new_balance_checking)
            else:
                answer = input("You dont have a checkingaccount, do you wish to create one? (yes/no)").lower()
                if answer == "yes":
                    self.create_account(file,account_id)
        else:
            print("Your account is inactive, please pay", current_balance_checking * -1)

    
    
    def deposit(self ,file, account_id, amount , flag = True):
        current_balance_checking = self.get_current_checking_balance(file,account_id)
        # if str(current_balance_checking).lower() != "none":
        if self.check_if_account_exist(file,account_id):
            
            amount = int(amount)
            new_balance_checking = current_balance_checking + amount
            
            status = file.get_field_info(account_id, "status").lower()
            if status == "inactive" and new_balance_checking>=0:
                file.update_row(account_id, "status" , "active")
                CheckingAccount.overdrafts_count[account_id] = 0
                print("Account reactivated")
            
            if flag:
                print(f"The new checking balance: {new_balance_checking}")
            file.update_row(account_id, "balance_checking" , new_balance_checking)
        else:
            answer = input("You dont have a checkingaccount, do you wish to create one? (yes/no) ").lower()
            if answer == "yes":
                self.create_account(file,account_id )
    
    def transfer(self,file ,  account_id,saving_account , amount):
        saving_account.withdraw(file,account_id, amount)
        self.deposit(file,account_id , amount)
    
    def create_account(self,file, account_id):
        new_balance_checking = int(input("Enter the chekcing account balance: "))
        file.update_row(account_id,"balance_checking",new_balance_checking)
        print(f"the checking account has been created")
        
        
    def get_current_checking_balance(self,file,account_id):
        current_checking_balance= file.get_field_info(account_id, "balance_checking")
        # print(f"Current checking balance: {current_checking_balance}")
        return current_checking_balance
        
    def check_if_account_exist(self,file ,account_id):
        # current_balance_checking = file.get_field_info(account_id, "balance_checking")
        current_balance = self.get_current_checking_balance(file,account_id)
        if str(current_balance).lower() == "none":
            return False
        else:
            return True
        
        