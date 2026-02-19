from datetime import datetime
expenses = []
amount = 0.0
category = ""
note = ""
date = ""
filename = "console_expense_tracker.txt"

def add_expense(expenses, amount, category, note, date):

    if amount < 0:
        return "Invalid amount"
    if  not category:
        return "Invalid category"
    date_format = '%Y-%m-%d'
    try :
        parsed_date = datetime.strptime(date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format"
    expense = {"amount": amount ,"category" : category,"note" : note, "date" : date}
    expenses.append(expense)
    return expenses
    

def list_expenses(expenses):

    if not expenses:
        print("No expenses yet.")
        return 
    itr = 0
    for i in expenses:
        itr+=1
        print(f"{itr}){i['amount']} | {i['category']} | {i['note']} | {i['date']}")

        
def total_spent(expenses) :
    total = 0.0
    for i in expenses:
        total+= i['amount']
    return total

def total_by_category(expenses):
    result = {}
    
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        
        if category in result:
            result[category] += amount
        else:
            result[category] = amount
    
    return result


def filter_by_category(expenses, category):
    result = []
    
    for expense in expenses:
        if expense['category'] == category:
            result.append(expense)


    return result


def save_expenses(expenses, filename):
    with open(filename, "w") as file:
        for expense in expenses:
            line = f"{expense['amount']}|{expense['category']}|{expense['note']}|{expense['date']}\n"
            file.write(line)

def load_expenses(filename):
    expenses = []
    
    try:
        with open(filename, "r") as file:
            for line in file:
                amount, category, note, date = line.strip().split("|")
                
                expense = {
                    "amount": float(amount),
                    "category": category,
                    "note": note,
                    "date": date
                }
                
                expenses.append(expense)
    
    except FileNotFoundError:
        return []
    
    return expenses

def main():
    while True:
        print("1) Add expense")
        print("2) List expenses")
        print("3) Total spent")
        print("4) Totals by category")
        print("5) Filter by category")
        print("6) Save")
        print("7) Load")
        print("0) Exit")

        task = input("Enter choice: ").strip()

        if task == "1":
            amount = float(input("Enter amount: "))
            category = input("Enter category: ")
            note = input("Enter note: ")
            date = input("Enter date (YYYY-MM-DD): ")
            print(add_expense(expenses, amount, category, note, date))  # optional feedback

        elif task == "2":
            list_expenses(expenses)

        elif task == "3":
            print(total_spent(expenses))

        elif task == "4":
            print(total_by_category(expenses))

        elif task == "5":
            cat = input("Which category? ")
            filtered = filter_by_category(expenses, cat)
            list_expenses(filtered)

        elif task == "6":
            save_expenses(expenses, filename)
            print(f"Saved to {filename}")

        elif task == "7":
            loaded = load_expenses(filename)
            expenses.clear()
            expenses.extend(loaded)
            print(f"Loaded {len(expenses)} expenses from {filename}")

        elif task == "0":
            break

        else:
            print("Invalid choice.")
    
if __name__ == "__main__":
    main()
