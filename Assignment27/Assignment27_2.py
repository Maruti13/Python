class BankAccount:
    # Class Variable
    ROI = 10.5        

    def __init__(self, Name, Amount):
        self.Name = Name
        self.Amount = Amount

    def Display(self):
        print("Account Holder :",self.Name)
        print("Current Balance :",self.Amount)

    def Deposit(self, Money):
        self.Amount = self.Amount + Money
        print("Amount Deposited Successfully")

    def Withdraw(self, Money):
        if(Money <= self.Amount):
            self.Amount = self.Amount - Money
            print("Amount Withdraw Successfully")
        else:
            print("Insufficient Balance")

    def CalculateInterest(self):
        Interest = (self.Amount * BankAccount.ROI) / 100
        return Interest


def main():
    NoAccounts = int(input("Enter number of accounts : "))

    for i in range(NoAccounts):
        print("\nAccount", i + 1)

        Name = input("Enter Account Holder Name : ")
        Amount = float(input("Enter Initial Balance : "))

        obj = BankAccount(Name, Amount)

        obj.Display()

        DepositAmount = float(input("Enter Deposit Amount : "))
        obj.Deposit(DepositAmount)

        WithdrawAmount = float(input("Enter Withdraw Amount : "))
        obj.Withdraw(WithdrawAmount)

        obj.Display()

        print(f"Interest = {obj.CalculateInterest()}")

if __name__ == "__main__":
    main()