class Payment:
    def pay(self,amount):
        print(f"{amount} paid")
class CashPayment(Payment):
    def pay(self, amount):
        print("Paid ₹<",amount,"> in cash")
class CardPayment(Payment):
    def pay(self, amount):
        print("Paid ₹<",amount,"> using credit/debit cards")
class UPIPayment(Payment):
    def pay(self, amount):
        print("Paid ₹<",amount,"> using UPI")
l1=[CashPayment(),CardPayment(),UPIPayment()]
for i in l1:
    i.pay(1000)

















       
