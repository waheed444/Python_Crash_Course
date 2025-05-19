# Encapsulation is data (attributes) and methods that operate on the data within a class,
# while restricting direct access to some components to maintain controlled data management.
# Note :
# It describes the idea of wrapping data and the methods that work on data within one unit.
# This puts restrictions on accessing variables and methods directly To prevent 
# accidental change, an object’s variable can only be changed by an object’s method.

class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner=owner
        self.__balance=balance
    
    def get_balance(self):
        return self.__balance
    
    def deposit(self,amount):
        if amount>0:
            self.__balance += amount
            print(f"Deposited {amount}. New Balance: {self.__balance}")
        else:
            print("Deposit amount must be positive.")
    
    def withdraw(self,amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New Balance: {self.__balance}")
        else:
            print("Insufficient funds or invalid amount.")
        

# Creating an object of BankAccount
account = BankAccount("Waheed", 500)

# Accessing balance through methods
account.deposit(200)        # Deposited 200. New Balance: 700
account.withdraw(100)       # Withdrew 100. New Balance: 600

