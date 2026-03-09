class Transaction:

    def __init__(self, amount, category, date, type, note=""):

        self.amount = amount
        self.category = category
        self.date = date
        self.type = type
        self.note = note

    def __repr__(self):
        return f"{self.category} ({self.amount})"

    def to_file_string(self):
        result = f"{self.amount}|{self.category}|{self.date}|{self.type}|{self.note}"
        return result

    def display(self):
        return f"{self.amount} euro * {self.category} * ({self.date}) | {self.type} - {self.note}"


class FinanceTracker:

    def __init__(self):

        self.transactions = []


    def add_transaction(self,transaction):
        if not transaction:
            return None
        self.transactions.append(transaction)

        return "Transaction added"




    def list_transactions(self):
        if not self.transactions:
            return []

        return [transaction.display() for transaction in self.transactions]



    def total_income(self):

        return sum(t.amount for t in self.transactions if t.type.lower() == "income")


    def total_expenses(self):

        return sum(t.amount for t in self.transactions if t.type.lower() == "expense")

    def balance(self):
        income = self.total_income()
        expenses = self.total_expenses()

        return income - expenses

    def save_to_file(self,filename):
        pass

    def load_from_file(self):
        pass


transaction_list = FinanceTracker()
new_trans1= Transaction(100,"Gaming","2026-10-01","expense","Video Game")
new_trans2= Transaction(900,"Gym","2026-11-01","expense","Video Game")
new_trans3 = Transaction(300,"Salary","2026-01-01","income","Salary for January")
new_trans4 = Transaction(500,"Bonus","2026-05-05","income","BONUSCHEE")

transaction_list.add_transaction(new_trans1)
transaction_list.add_transaction(new_trans2)
transaction_list.add_transaction(new_trans3)
transaction_list.add_transaction(new_trans4)
print(transaction_list.balance())




















