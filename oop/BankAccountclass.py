'''Task 4: BankAccount class
Attributes: account_holder, balance (default 0)

Methods: deposit(amount), withdraw(amount), get_balance()

Add error message if withdraw amount > balance'''

class BankAccount:
    def __init__(self,account_holder,balance=0): #balance is default 0
        self.account_holder=account_holder
        self.balance=balance
    
    def deposit(self,amount):
        self.balance=amount+self.balance
        return self.balance
    
    def withdraw(self,amount):
        if amount>self.balance:
            print(f"Balance is low RECHARGE PLZ!!! : {self.balance}")
        else:
            self.balance=self.balance-amount
            return self.balance
        
        
    def get_balance(self):
        return self.balance

# creating object

b1=BankAccount("Shahzaib")

while True:

    print("Choose the operation : 1 for deposit, 2 for withdraw, 3 for get_balance,  4 for exit")

    operation=input(f"Enter the operation  {b1.account_holder} :").strip().lower()

    if operation in ["1","2"]:
        amount=float(input("Entr the amount :"))

        if operation == "1":
            print(" The balance after deposit is:" , b1.deposit(amount))

        elif operation == "2":
            result = b1.withdraw(amount)
            if result is not None:
                print("Balance after withdrawal is:", result)
    

    elif operation == "3":
        print("The total balance is :" , b1.get_balance())

    elif operation == "4":
        print("THANK YOU!!! for using our Bank!")
        break

    else:
        print("Invalid! command  PLZ TRY AGAIN")


    
