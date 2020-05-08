class BankAccount(): 

    balance = 100
    accountNumber = 1234

    def __init__(self, number):
        self.number = number

    def withdrawl(self):
              self.balance = self.balance - self.number
    
    def deposit(self): 
        self.balance = self.balance + self.number

    def getBalance(self):
        print(f"""You're account balance is ${self.balance}""")


class CheckingAccount(BankAccount):

    fees = 5
    minimumBalance = 50

    def deductFees(self):
        self.balance = self.balance - self.fees

    def checkMinimumBalance(self):
        if(self.balance < self.minimumBalance):
            print(f"""You're balance of ${self.balance} is below the minimum required balance of ${self.minimumBalance}, please make a deposit""")
        else:
            print(f"""You're account balance of ${self.balance} is above the minimum required balance.""")
    

class SavingsAccount(BankAccount):

    interestRate = 1.02

    def addInterest(self):
        self.balance = self.balance * self.interestRate
        print(self.balance)

checking = CheckingAccount(50)
savings = SavingsAccount(50)
account = BankAccount(50)

checking.deductFees()
checking.checkMinimumBalance()






