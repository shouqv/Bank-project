from bank.bank import Customer

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
            password = int(input("Account ID: "))
            
            if customer.login(account_id,password):
                # get customer name
                while True:
                    print("1) Withdraw  2) Deposit 3) Transfer 4) Logout")
                    selection = input("Choice: ")
                    match selection:
                        case "1":
                            account = input("withdraw from: (checking/saving): ")
                            amount = input("Amount: ")
                            customer.withdraw(account_id,amount , account)
                        case "2":
                            account = input("Deposit from: (checking/saving): ")
                            amount = input("Amount: ")
                            customer.withdraw(account_id,amount , account)
                        case "3":
                            customer.transfer()
                        case "4":
                            break
        case "3":
            break
        case _:
            print("invalid option")
        
    