""" Simple Bank Account Manager
Goal:
Build a Python program to manage simple bank accounts, practicing:

String manipulation

Lists, tuples, sets, dictionaries

Conditionals (if/elif/else)

Loops (while, for, nested loops)

Functions

Classes and objects

Exit confirmation

📊 Learning Objectives
Create and use classes and objects.

Use methods to operate on object data.

Organize code with functions for modularity.

Use loops and conditionals inside functions and methods.

Practice searching, statistics, and exit confirmation logic.

📌 Features to Implement
Create Account – Store account holder’s name, account number, and initial balance.

Deposit Money – Add an amount to the account balance.

Withdraw Money – Subtract an amount from the balance (check for insufficient funds).

View All Accounts – Display all account details.

Search Account by Name or Number – Case-insensitive search.

Show Statistics – Total accounts, total balance, average balance.

Exit – Ask for confirmation before quitting.

📂 Data Structures
Class BankAccount with attributes:

class BankAccount:

           def __init__(self, name, account_number,
           balance):

                         self.name = name

                         self.account_number = account_number

                         self.balance = balance
List → stores all BankAccount objects.

Set → optional, to store unique account numbers.

📜 Menu System
The program should output 7 options to the user:

               1. Create Account
               2. Deposit Money
               3. Withdraw Money
               4. View All Accounts
               5. Search Account
               6. Show Statistics
               7. Exit

Then, it has to:

Ask the user to enter the number of the action it wishes to carry out.

If the number is not in the range 1 to 7, send and error message and ask for a correct option and keep looping this action until the user chooses an option in the list.

If the number is in the range 1 to 7 redirect them to the correct block of code.

🛠 Classes and Functions to Create
Class BankAccount

Attributes: name, account_number, balance.

Methods:

deposit(amount) → adds to balance

withdraw(amount) → subtracts from balance if sufficient funds

display() → prints account info

create_account(accounts_list)

Ask for name → format with .title().

Ask for account number → validate uniqueness.

Ask for initial balance → validate as number.

Create BankAccount object and append to list.

deposit_to_account(accounts_list)

Ask for account number.

Search and deposit amount using the deposit method.

withdraw_from_account(accounts_list)

Ask for account number.

Search and withdraw amount using the withdraw method.

view_all_accounts(accounts_list)

Loop through accounts and call each account’s display() method.

search_account(accounts_list, query)

Search by name or account number (case-insensitive).

Display account info if found.

show_statistics(accounts_list)

Total accounts (len(accounts_list)).

Total balance (sum of balances).

Average balance.

confirm_exit()

Ask "Are you sure you want to exit? (yes/no)".

Return True if yes, otherwise False."""

print("Welcome to the Simple Bank Account Manager!")

# BankAccount (class)          ← Any BankAccount object is created from this class
#     ↓
# accounts_list (list)         ← All BankAccount objects are stored here
#     ↓
# Functions                    ← Manage the list and interact with BankAccount objects
#     ↓
# while True (ana döngü)       ← Menu system to call functions based on user input

# ── Global Variables ───────────────────────────────────────────────
accounts_list = []
account_numbers = set()

# ── BankAccount Class ──────────────────────────────────────────────
class BankAccount:
    def __init__(self, name, account_number, balance):
        self.name = name
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.balance += amount
        print(f"Successfully deposited €{amount:.2f}. New balance: €{self.balance:.2f}")
        return True

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.balance:
            print(f"Insufficient funds. Current balance: €{self.balance:.2f}")
            return False
        self.balance -= amount
        print(f"Successfully withdrew €{amount:.2f}. New balance: €{self.balance:.2f}")
        return True

    def display(self):
        print(f"  Name          : {self.name}")
        print(f"  Account Number: {self.account_number}")
        print(f"  Balance       : €{self.balance:.2f}")
        print(f"  {'-'*35}")

# ── Functions ────────────────────────────────────────────────────
def find_account(accounts_list, account_number):
    for account in accounts_list:
        if account.account_number == account_number.upper():
            return account
    return None

def create_account(accounts_list, account_numbers):
    print("\n----- Create Account -----")
    name = input("Enter account holder's name: ").strip().title()
    while True:
        account_number = input("Enter account number: ").strip().upper()
        if account_number in account_numbers:
            print("This account number already exists. Please enter a unique number.")
            continue
        break
    while True:
        balance_input = input("Enter initial balance: ").strip()
        try:
            balance = float(balance_input)
            if balance < 0:
                print("Initial balance cannot be negative.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    new_account = BankAccount(name, account_number, balance)
    accounts_list.append(new_account)
    account_numbers.add(account_number)
    print(f"\nAccount for '{name}' (#{account_number}) created successfully!")

def deposit_to_account(accounts_list):
    print("\n----- Deposit Money -----")
    account_number = input("Enter account number: ").strip()
    account = find_account(accounts_list, account_number)
    if account is None:
        print(f"No account found with number '{account_number}'.")
        return
    while True:
        amount_input = input("Enter deposit amount: ").strip()
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    account.deposit(amount)

def withdraw_from_account(accounts_list):
    print("\n----- Withdraw Money -----")
    account_number = input("Enter account number: ").strip()
    account = find_account(accounts_list, account_number)
    if account is None:
        print(f"No account found with number '{account_number}'.")
        return
    while True:
        amount_input = input("Enter withdrawal amount: ").strip()
        try:
            amount = float(amount_input)
            break
        except ValueError:
            print("Invalid input. Please enter a number.")
    account.withdraw(amount)

def view_all_accounts(accounts_list):
    print("\n----- All Accounts -----")
    if not accounts_list:
        print("No accounts found.")
        return
    for i, account in enumerate(accounts_list):
        print(f"\nAccount #{i+1}:")
        account.display()

def search_account(accounts_list, query):
    print("\n----- Search Results -----")
    query_lower = query.strip().lower()
    found = False
    for account in accounts_list:
        name_match   = query_lower in account.name.lower()
        number_match = query_lower in account.account_number.lower()
        if name_match or number_match:
            account.display()
            found = True
    if not found:
        print(f"No account found matching '{query}'.")

def show_statistics(accounts_list):
    print("\n----- Statistics -----")
    total = len(accounts_list)
    if total == 0:
        print("No accounts to show statistics for.")
        return
    total_balance   = sum(account.balance for account in accounts_list)
    average_balance = total_balance / total
    print(f"Total accounts : {total}")
    print(f"Total balance  : €{total_balance:.2f}")
    print(f"Average balance: €{average_balance:.2f}")

def confirm_exit():
    answer = input("Are you sure you want to exit? (yes/no): ").strip().lower()
    if answer in ('yes', 'y'):
        print("Goodbye!")
        return True
    print("Exit cancelled. Returning to menu.")
    return False

# ── Main While Loop ────────────────────────────────────────────────
while True:
    print("\n=============================")
    print("  Simple Bank Account Manager")
    print("=============================")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View All Accounts")
    print("5. Search Account")
    print("6. Show Statistics")
    print("7. Exit")

    choice = input("Enter your choice (1-7): ").strip()

    if choice == '1':
        create_account(accounts_list, account_numbers)
    elif choice == '2':
        deposit_to_account(accounts_list)
    elif choice == '3':
        withdraw_from_account(accounts_list)
    elif choice == '4':
        view_all_accounts(accounts_list)
    elif choice == '5':
        query = input("Enter name or account number to search: ").strip()
        search_account(accounts_list, query)
    elif choice == '6':
        show_statistics(accounts_list)
    elif choice == '7':
        if confirm_exit():
            break
    else:
        print("Invalid choice. Please enter a number between 1 and 7")