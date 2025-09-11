class BankAccount:
    def __init__(self):
        self.__balance=0
    def deposit(self,amount):
        self.__balance+=amount
        print("Deposit ₹",self.__balance)
    def get_balance(self):
        print(self.__balance)
    def withdraw(self,amount):
        if self.__balance>amount:
            self.__balance-=amount
            print("Withdraw ₹",self.__balance)

        else:
            print("Insufficient")
b=BankAccount()
b.deposit(5000)
b.get_balance()
b.withdraw(2000)
b.get_balance()

    
    