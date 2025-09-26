# Bank System Project


## Description

This project implements a banking system in **Python**, allowing cashiers to manage customer accounts stored in a CSV file. It leverages **file handling**, **exception handling**, and is developed following a **test-driven development (TDD)** approach.  

The system supports functionalities including:  
- Adding new customers  
- Depositing and withdrawing money  
- Transferring funds between accounts, including to other customers' accounts  
- Overdraft protection with rules and account reactivation  

## Features
- **Add New Customer**  
  - Can create a checking account, savings account, both, or neither  
  - Account ID is automatically generated  


- **Withdraw Money** (requires login)  
  - From checking or savings accounts  
  - Checking accounts adhere to overdraft rules  
  - Savings accounts do not allow overdrafts  

- **Deposit Money** (requires login)  
  - Into checking or savings accounts  

- **Transfer Money** (requires login)  
  - Between own accounts  
  - To other customers’ accounts  

- **Overdraft Protection**  
  - $35 fee for overdraft  
  - Prevents account balance from going below -$100  
  - Account deactivation after 2 successful overdrafts  
  - Reactivation after clearing overdraft and fees  


## File Structure
```
Banking-With-Python/
│
├── bank/ # Directory for main files for bank system 
│ ├── checking_account.py
│ ├── custome_exceptions.py
│ ├── customer.py
│ ├── file_management.py
│ └── saving_account.py
|
├── data/
│ └── bank.csv #CSV file storing customer data
|
├── test/ # Directory for TDD unit tests
│ ├── test_checking_account.py
│ ├── test_customer.py
│ ├── test_file_management.py
│ └── test_saving_account.py
|
├── main.py
└── README.md

```