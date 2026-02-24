class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transaction_history = []

    def deposit(self, amount):
        self.balance += amount
        self.transaction_history.append(amount)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transaction_history.append(-abs(amount))

    def display_balance(self):
        print(f"{self.name}'s balance: {self.balance}")


    def print_transaction_history(self):
        for t in self.transaction_history:
            if t > 0:
                print(f"Deposited: {t}")
            else:
                print(f"Withdrew: {-t}")


