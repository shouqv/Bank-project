from bank.customer import Customer

customer = Customer("data/bank.csv")
print("welcome to the bank")

while True:
    print("1) Add customer  2) Login 3) Exit")
    choice = input("Choice: ")
    
    match choice:
        case "1":
            account_id = int(input("Enter account id: "))
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            password = input("Enter your password: ")
            print("Type None if you don’t want to create any of the below accounts")
            balance_checking = input("Checking account balance: ")
            balance_savings = input("Saving account balance: ") 
            customer.add_new_customer(account_id, first_name, last_name, password, balance_checking, balance_savings)
            print("Customer added successfully.")
            
            
        case "2":
            account_id = int(input("Account ID: "))
            password = input("password: ")
            
            if customer.login(account_id,password):
                # get customer name
                while True:
                    try:
                        print("1) Withdraw  2) Deposit 3) Transfer 4) Logout")
                        selection = input("Choice: ")
                        match selection:
                            case "1":
                                account = input("Withdraw from (checking/saving): ")
                                print(customer.get_current_balance(account_id , account))
                                amount = int(input("Amount: "))
                                customer.withdraw(account_id, account , amount)

                            case "2":
                                account = input("Deposite from (checking/saving): ")
                                print(customer.get_current_balance(account_id , account))
                                amount = int(input("Amount: "))               
                                customer.deposit(account_id, account , amount)


                            case "3":
                                    print("a) Transfer from checking to saving")
                                    print("b) Transfer from saving to checking")
                                    print("c) Transfer to another customer account")
                                    print()
                                    print(customer.get_current_balance(account_id , "checking"))
                                    print(customer.get_current_balance(account_id , "saving"))
                                    print()                           
                                    choice = input("Choice: ").lower()
                                    if choice == "c":
                                        from_account = input("Transfer from (checking/saving): ").lower() #just personal preference, he chooses the account then the ammount                                   
                                    amount = int(input("Amount: "))


                                    if choice == "c":
                                        other_customer = int(input("Enter the account ID to transfer to: "))
                                        customer.transfer(account_id, choice, amount, from_account=from_account, other_customer=other_customer)
                                        print(f"Transferred {amount} from {from_account} to customer {other_customer}")
                                    else:
                                        customer.transfer(account_id, choice, amount)
                                        print("Transfer completed successfully.")

                            case "4":
                                break
                    except ValueError as e:
                        print(e)
            else:
                print("Password incorrect!")
        case "3":
            break
        case _:
            print("invalid option")
        
    