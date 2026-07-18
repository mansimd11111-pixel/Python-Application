class BankAccount:
    ROI = 10.5

    def _init_(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Name:", self.Name)
        print("Balance:", self.Amount)

    def Deposit(self, amt):
        self.Amount += amt
        print("Amount Deposited:", amt)

    def Withdraw(self, amt):
        if amt <= self.Amount:
            self.Amount -= amt
            print("Amount Withdrawn:", amt)
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest


obj1 = BankAccount("Mansi", 10000)
obj1.Display()
obj1.Deposit(2000)
obj1.Withdraw(3000)
print("Interest:", obj1.CalculateInterest())
obj1.Display()

obj2 = BankAccount("Rahul", 5000)
obj2.Display()
print("Interest:", obj2.CalculateInterest())