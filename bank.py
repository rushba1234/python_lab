class BankAccount:
    def __init__(self, accno, name, acctype, balance):
        self.accno = accno
        self.name = name
        self.acctype = acctype
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance")
        else:
            self.balance -= amount
            print("Balance after withdrawal:", self.balance)


# take input from user
accno = input("Enter account number: ")
name = input("Enter name: ")
acctype = input("Enter type of account: ")
balance = float(input("Enter initial balance: "))

# create account object
account = BankAccount(accno, name, acctype, balance)

# deposit money
amount = float(input("Enter amount to deposit: "))
account.deposit(amount)

# withdraw money
amount = float(input("Enter amount to withdraw: "))
                                                                                                                                      1,18          Top
# withdraw money
amount = float(input("Enter amount to withdraw: "))
account.withdraw(amount)
     
