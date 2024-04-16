# Create a Account class with 2 attributes & account no. Create method for debit, Credit & printing the balance .

class Account :

    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    def debit(self,amount):
        self.balance -= amount
        print("Rs. ", amount , "was debited")
        print("total balance = ",self.get_balance())

    def credit(self,amount):
        self.balance +=amount
        print("Rs. ", amount , "was debited")
        print("total balance = ",self.get_balance())

    def get_balance(self):
        return self.balance
    
acc1 = Account(10000,12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)