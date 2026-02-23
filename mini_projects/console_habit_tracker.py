from datetime import datetime

habits = []
name = None
created_date = ""
filename = "Habits.txt"


def add_habit(habits, name, created_date):
    active = True
    

    if not name or not name.strip() :
        return "Name cannot be empty!"
    
    date_format = '%Y-%m-%d'
    try :
        parsed_date = datetime.strptime(created_date, "%Y-%m-%d")
    except ValueError:
        return "Invalid date format"
    
    for habit in habits:
        if str(name).lower() == habit['name'].lower():
            return "This habit already exists!"
        
            
            
    new_habit = {'name': name ,'active' : active, "created" : created_date ,"done_dates" : []}

    habits.append(new_habit)

    return habits



def list_habits(habits):

    if len(habits) <= 0:
        print("No habits yet.")
        return
    
    itr = 0
    for habit in habits:
        itr+=1
        print(f"{itr}) {habit['name']} | {habit['active']} | created: {habit['created']} | done: {len(habit['done_dates'])}" )



def mark_done(habits, name, date):
    is_found = False

    for habit in habits:
        if habit["name"].lower() == str(name).lower():
            is_found = True

            if habit["active"] is False:
                print("The habit is inactive!")
                return

            if date in habit["done_dates"]:
                print("Already marked for this date.")
                return
            else:
                habit["done_dates"].append(date)
                print("Habit completed!")
                return

    if is_found is False:
        print("This habit is not found.")
        return




def toggle_habit(habits, name):

    for habit in habits:
        if habit['name'] == name:
            if habit['active'] is True:
                habit['active'] = False
            else:
                habit['active'] = True
    return

def total_done(habits):
    total = 0

    for habit in habits:
        total+= (len(habit['done_dates']))
    print(f'Total number of done habits: {total}')
    return 

def progress_by_habit(habits):
    new_dict = {}
    key = ''
    value = ''

    for habit in habits:
        key = habit['name']
        value = len(habit['done_dates'])
        new_dict[key] = value
    print(new_dict)
    return

def filter_active(habits):
    active = []

    for habit in habits:
        if habit['active'] is True:
            active.append(habit)
    if not active :
        print("No active habits!")

    print(active)
    return

def save_habits(habits, filename):
    with open(filename, "w") as file:
        for habit in habits:
            line = f"{habit['name']}|{habit['active']}|{habit['created']}|{habit['done_dates']}"
            file.write(line + "\n")


def load_habits(filename):

    habits = []

    try:
        with open(filename, "r") as file:
            for line in file:
                name, active, created, done_dates = line.strip().split("|")

                
                active = True if active == "1" else False

                
                if done_dates:
                    done_dates = done_dates.split(",")
                else:
                    done_dates = []

                habit = {
                    "name": name,
                    "active": active,
                    "created": created,
                    "done_dates": done_dates
                }

                habits.append(habit)

    except FileNotFoundError:
        return []

    return habits

def main():


    while True:

        print('1) Add habit')
        print('2) List habits')
        print('3) Mark done')
        print('4) Toggle active')
        print('5) Total done')
        print('6) Progress by habit')
        print('7) Show active only')
        print('8) Save')
        print('9) Load')
        print('0) Exit')

        option = int(input())

        if option == 1:
            name = input("Enter name:")
            created_date = input("Enter date:")
            add_habbit(habits , name , created_date)
            print("Habit added successfully")
        elif option == 2:
            list_habits(habits)
        elif option == 3:
            name = input("Enter name:")
            date = input("Enter date when done:")
            mark_done(habits, name , date)
        elif option == 4:
            name = input("Enter name:")
            toggle_habit(habits, name)
        elif option == 5:
            total_done(habits)
        elif option == 6:
            progress_by_habit(habits)
        elif option == 7:
            filter_active(habits)
        elif option == 8:
            save_habits(habits ,filename)
        elif option == 9:
            habits = load_habits(filename)
        elif option == 0:
             return
            
        else:
            print("Invalid input")
            break
           


if __name__ == "__main__":
    main()

        

        








##def save_expenses(expenses, filename):
  #  with open(filename, "w") as file:
    #    for expense in expenses:
     #       line = f"{expense['amount']}|{expense['category']}|{expense['note']}|{expense['date']}\n"
      #      file.write(line)


#test_habit3 = add_habbit(habits, "ym5" , "1992-12-1")
#test_habit1 = add_habbit(habits, "gym" , "1993-10-1")
#test_habit2 = add_habbit(habits, "ym" , "1992-10-1")


#mark_done(habits, "gym", "2020-01-02")
#mark_done(habits, "ym5", "1211-11-11")
#mark_done(habits, "gym", "2021-01-01")
#mark_done(habits, "ym", "1111-12-11")

#toggle_habit(habits,'ym5')
#toggle_habit(habits,'gym')
#toggle_habit(habits,'ym')



