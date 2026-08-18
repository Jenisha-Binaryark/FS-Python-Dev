class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited amount is: {amount} \n New Balance is: {self.balance}")
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew amount is: {amount} \n New balance is: {self.balance}")
    def show_balance(self):
        print(f"{self.owner}'s balance: Rs{self.balance}")

account = BankAccount("Jenisha", 1000)
account.show_balance()
account.deposit(500)
account.withdraw(2000)
account.withdraw(300)