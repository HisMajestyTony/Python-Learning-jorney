import datetime


class Transaction:

    def __init__(self, amount, category, date, transaction_type, note=""):

        self.amount = amount
        self.category = category
        self.date = date
        self.transaction_type = transaction_type
        self.note = note

    def __repr__(self):
        return f"{self.category} ({self.amount})"

    def to_file_string(self):
        result = f"{self.amount}|{self.category}|{self.date}|{self.transaction_type}|{self.note}"
        return result

    def display(self):
        return f"{self.amount} euro * {self.category} * ({self.date}) | {self.transaction_type} - {self.note}"



class FinanceTracker:

    def __init__(self):

        self.transactions = []
        self.load_from_file("transactions.txt")


    def add_transaction(self, transaction):
        self.transactions.append(transaction)
        self.save_to_file("transactions.txt")

        return "Transaction added"




    def list_transactions(self):
        if not self.transactions:
            return []

        return [transaction.display() for transaction in self.transactions]



    def total_income(self):

        return sum(t.amount for t in self.transactions if t.transaction_type.lower() == "income")


    def total_expenses(self):

        return sum(t.amount for t in self.transactions if t.transaction_type.lower() == "expense")

    def balance(self):
        income = self.total_income()
        expenses = self.total_expenses()

        return income - expenses

    def save_to_file(self,filename):
        with open (filename , "w" , encoding="utf-8") as f:
            for transaction in self.transactions:
                f.write(transaction.to_file_string())
                f.write("\n")


    def load_from_file(self,filename):
        self.transactions = []

        try:
            with open(filename, "r", encoding="utf-8") as f:

                for line in f:
                    line = line.strip()

                    if not line:
                        continue

                    amount , category , date , transaction_type , note = line.split("|")
                    amount = float(amount)


                    transaction = Transaction(amount,category,date,transaction_type,note)
                    self.transactions.append(transaction)
        except FileNotFoundError:
            return "File not found"


def main():
    transaction_list = FinanceTracker()

    while True:
        print("1) Add income")
        print("2) Add expense")
        print("3) List all transactions")
        print("4) Show total income")
        print("5) Show total expense")
        print("6) Balance")
        print("0) Exit")


        option = input("Please select your option:")

        if option == "1":

            try:

                amount = float(input("Please enter the amount of your transaction: "))
            except ValueError:
                print("Invalid input")
                continue

            category_tran = input("Please enter the category of your transaction: ").strip()

            try:
                date = input("Please enter the date of your transaction: ")
                datetime.date.fromisoformat(date)
            except ValueError:
                print("Incorrect data format, should be YYYY-MM-DD")
                continue




            transaction_type = "income"
            note = input("Please enter an additional note or skip by pressing enter: ")

            transaction = Transaction(amount, category_tran,date,transaction_type,note)

            transaction_list.add_transaction(transaction)

            print("Transaction is added to the file")

        elif option == "2":
                try:

                    amount = float(input("Please enter the amount of your transaction: "))
                except ValueError:
                    print("Invalid input")
                    continue

                category_tran = input("Please enter the category of your transaction: ").strip()


                try:
                    date = input("Please enter the date of your transaction: ")
                    datetime.date.fromisoformat(date)
                except ValueError:
                    print("Incorrect data format, should be YYYY-MM-DD")
                    continue

                transaction_type = "expense"
                note = input("Please enter an additional note or skip by pressing enter: ")

                transaction = Transaction(amount, category_tran, date, transaction_type, note)

                transaction_list.add_transaction(transaction)

                print("Transaction is added to the file")

        elif option == "3":
            if not transaction_list.transactions:
                print("The list is empty")
                continue

            for transaction in transaction_list.transactions:
                print(transaction.display())

        elif option == "4":
            print(transaction_list.total_income())

        elif option == "5":
            print(transaction_list.total_expenses())
        elif option == "6":
            print(transaction_list.balance())


        elif option == "0":
            break

        else:
            print("Invalid input")















if __name__ == "__main__":
    main()























