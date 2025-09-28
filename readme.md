# Bank System Project

Find the [updated bank system](https://github.com/shouqv/bank_project_updated)

## Description

This project implements a banking system in **Python**, allowing cashiers to manage customer accounts stored in a CSV file. It leverages **file handling**, **exception handling**, and is developed following a **test-driven development (TDD)** approach.  

The system supports functionalities including:  
- Adding new customers  
- Depositing and withdrawing money  
- Transferring funds between accounts, including to other customers' accounts  
- Overdraft protection with rules and account reactivation
- Custom exceptions to handle invalid inputs and errors (e.g., invalid options, incorrect IDs, empty files, invalid numeric values, inactive accounts, overdraft-related errors, etc.)

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

- **Exception Handling & Custom Exceptions**
  - Provides robust error handling for all user inputs and banking operations.  
  - Ensures the application can handle errors gracefully without crashing.  
  - Includes **custom domain-specific exceptions**:  
    - **InactiveAccountError**: Raised when attempting to operate on an inactive account.  
    - **AccountIsNoneError**: Raised when accessing an account that was not created.  
    - **OverdraftRejectedError**: Raised when an overdraft attempt is invalid (e.g., on a savings account or exceeding allowed amount limits).  
    - **OverdraftLimitExceededError**: Raised when overdraft attempts exceed allowed count.  
    - **CustomerNotFoundError**: Raised when a non-existent customer ID is used.  
    - **InvalidChoiceError**: Raised when the user selects an invalid menu option or account type.  
  - Handles **built-in Python exceptions** with custom messages for clarity:  
    - **ValueError**: Raised for invalid numeric inputs (e.g., non-numeric deposits/withdrawals).  
  - Some exceptions allow **recovery actions**:  
    - Prompting users to create a missing account (`AccountIsNoneError`).  
    - Preventing transfers to invalid accounts while guiding the user to valid options.  
  - Helps maintain **data integrity** and ensures **realistic banking rules** are enforced consistently across all operations.


## File Structure
```
Banking-With-Python/
│
├── bank/                   # Core banking logic
│ ├── checking_account.py
│ ├── custome_exceptions.py
│ ├── customer.py
│ ├── file_management.py
│ └── saving_account.py
|
├── data/
│ └── bank.csv              # Stores customer data
|
├── test/                   # Unit tests (TDD approach)
│ ├── test_checking_account.py
│ ├── test_customer.py
│ ├── test_file_management.py
│ └── test_saving_account.py
|
├── main.py                 # Main user interface
└── README.md

```

# What I Learned

- How to design and implement a project using Test-Driven Development (TDD) from the ground up.

- The importance of modularity by separating concerns into classes (Customer, CheckingAccount, SavingAccount, FileManagement).

- How to implement custom exceptions to handle domain-specific errors gracefully.

- Practical experience with file I/O, data persistence in CSV, and input validation.

- Building a CLI banking system that feels close to real-world workflows.
