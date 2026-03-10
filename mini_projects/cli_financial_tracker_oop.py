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


def prompt_transaction(transaction_type):
    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Invalid input")
        return None
    if amount <= 0:
        print("Amount cannot be negative or 0")
        return None

    category = input("Enter category: ").strip()
    if not category:
        print("Category cannot be empty")
        return None


    date = input("Enter date: ")

    try:
        datetime.date.fromisoformat(date)
    except ValueError:
        print("Date format must be as follows YYYY-MM-DD")
        return None

    note = input("Enter note: ").strip()


    return Transaction(amount, category, date, transaction_type, note)


class FinanceTracker:

    def __init__(self):

        self.transactions = []
        self.load_from_file("transactions.txt")


    def add_transaction(self, transaction):
        if not isinstance(transaction, Transaction):
            return False


        self.transactions.append(transaction)
        self.save_to_file("transactions.txt")
        return "Transaction added"



    def delete_transaction(self,index):
        self.transactions.pop(index)



    def list_transactions(self):
        if not self.transactions:
            return []

        return self.transactions



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
        print("7) Delete transaction+")
        print("0) Exit")


        option = input("Please select your option:")

        if option == "1":
            transaction = prompt_transaction("income")

            if transaction is None:
                continue

            transaction_list.add_transaction(transaction)
            print("Transaction is added to the file")



        elif option == "2":

               transaction = prompt_transaction("expense")

               if transaction is None:
                   continue

               transaction_list.add_transaction(transaction)
               print("Transaction is added to the file")


        elif option == "3":
            if not transaction_list.transactions:
                print("The list is empty")
                continue

            for i , transaction in enumerate(transaction_list.list_transactions(), start=1):
                print(i , transaction.display())


        elif option == "4":
            print(transaction_list.total_income())

        elif option == "5":
            print(transaction_list.total_expenses())
        elif option == "6":
            print(transaction_list.balance())
        elif option == "7":

            try:
                index = int(input("Please enter the number of the transaction you are willing to delete: "))
            except ValueError:
                print("Invalid input")
                continue
            if index > len(transaction_list.transactions):
                print("Invalid index")
                continue
            if index < 0:
                print("Invalid index")
                continue
            double_check = input("Are you sure that you want to delete this transaction ? Please select y or n").strip()

            if double_check == "n":
                continue
            else:
                transaction_list.delete_transaction(index -1)
                transaction_list.save_to_file("transactions.txt")
                print("Transaction deleted successfully")



        elif option == "0":
            break

        else:
            print("Invalid input")















if __name__ == "__main__":
    main()









# filter by income/expense
#
# filter by category
#
# monthly summary
#
# search by keyword in note/category













