from datetime import datetime
habits = []
name = None
created_date = ""


def add_habbit(habits ,name, created_date):
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

    new_list = []
    is_found = False

    for habit in habits:
        if str(name).lower() in habit['name'].lower():

            is_found = True

            if habit['active'] is False:
                print("The habit is inactive!")
                return 
            if habit['done_dates'] == date:
                pass
            else:
                habit['done_dates'].append(date)
    
    if is_found == False :
        print("This habit is not found.")
        return
        
    print('Habit completed!')
    return
    
    
test_habit3 = add_habbit(habits, "ym5" , "1992-12-1")
test_habit1 = add_habbit(habits, "gym" , "1993-10-1")
test_habit2 = add_habbit(habits, "ym" , "1992-10-1")


mark_done(habits, "gym", "2020-01-02")
mark_done(habits, "ym5", "1211-11-11")
mark_done(habits, "gym", "2021-01-01")
mark_done(habits, "ym", "1111-12-11")

     
list_habits(habits)   
