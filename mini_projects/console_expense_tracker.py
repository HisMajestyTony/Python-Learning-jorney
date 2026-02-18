from datetime import datetime
expenses = []

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
    



result = add_expense(expenses, 20 , "food" , "burger", "2026-02-18")
result2 = add_expense(expenses, 30 , "videogames" , "for honor", "2026-02-12")
#print(result)


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
    
    category_dict = {}

    for i in expenses:
        for key , value in i.items():
            if key is "category":
                category_dict.update(key,value)
    return category_dict


print(total_by_category(expenses))