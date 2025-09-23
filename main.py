from bank.customer import Customer

customer = Customer("data/bank.csv")
print("welcome to the bank")

while True:
    print("1) Add customer  2) Login 3) Exit")
    choice = input("Choice: ")
    
    match choice:
        case "1":
            customer.add_new_customer()
        case "2":
            account_id = int(input("Account ID: "))
            password = input("password: ")
            
            if customer.login(account_id,password):
                # get customer name
                while True:
                    print("1) Withdraw  2) Deposit 3) Transfer 4) Logout")
                    selection = input("Choice: ")
                    match selection:
                        case "1":
                            account = input("Withdraw from (checking/saving): ")
                            customer.get_current_balance(account_id , account)
                            amount = int(input("Amount: "))
                            customer.withdraw(account_id, account , amount)
                        case "2":
                            account = input("Deposite from (checking/saving): ")
                            customer.get_current_balance(account_id , account)
                            amount = int(input("Amount: "))               
                            
                            customer.deposit(account_id, account , amount)
                        case "3":

                            customer.transfer(account_id)
                        case "4":
                            break
            else:
                print("Password incorrect!")
        case "3":
            break
        case _:
            print("invalid option")
        
    