from .file_management import FileManagement
# crediting https://www.geeksforgeeks.org/python/get-current-date-and-time-using-python/
import datetime
class Transaction():
    def __init__(self):
        self.transaction_file = FileManagement("data/transaction.csv")
        pass
    def add_transaction(self,account_id,name,operation_detail,before_balance,affected_account,new_balance):
        self.transaction_file.add_row(
            account_id = account_id,
            operation_id = 1, #for this to work i need to add new method in file mangement that searches the last row of a certin id to increment it
            name = name,
            operation_detail = operation_detail,
            time = datetime.datetime.now(),
            before_balance = before_balance,
            affected_account = affected_account,
            new_balance=new_balance
        )