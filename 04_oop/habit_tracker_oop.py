class Habit:
    def __init__(self, name):
        self.name = name
        self.done = False


    def mark_done(self):
        self.done = True

    def show(self):
        status = "Done" if self.done else "Not done"
        print(f"{self.name} [{status}]")
    def toggle(self):
        self.done = not self.done



def add_habit(habit_list , name):
    new_habit = Habit(name)
    habit_list.append(new_habit)

def show_habits(habit_list):
    for index, habit in enumerate(habit_list):
        status = "Done" if habit.done else "Not done"
        print(f"{index}) {habit.name} [{status}]")


def complete_habit(habit_lst , index):
    if 0 <= index < len(habit_lst):
            habit_lst[index].mark_done()

def toggle_habit(habit_list, index):

    if 0 <= index < len(habit_list):
        habit_list[index].toggle()
        return True
    return False

def delete_habit(habit_list, index):
    if 0 <= index < len(habit_list):
        habit_list.pop(index)
        return True
    else:
        return False


def save_habits(habit_list ,filename):
    with open(filename ,"w", encoding="utf-8") as f:
        for habit in habit_list:
            f.write(f"{habit.name}|{int(habit.done)}\n")

def load_habits(filename):
    habits = []

    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                name, done = line.split("|", 1)

                habit = Habit(name)
                if done == "1":
                    habit.mark_done()

                habits.append(habit)

    except FileNotFoundError:
        return []

    return habits





def main():
    filename = "habits.txt"
    habits = load_habits(filename)


    while True:
        print("\n1 Add habit")
        print("2 Show habit")
        print("3 Complete habit")
        print("4 Save")
        print("5 Toggle")
        print("6 Delete habit")
        print("0 Exit")


        choice = input("Please select an option:")

        if choice == "1":
            name = input("Please enter a name:").strip()
            if not name:
                print("Name cannot be empty!")
                continue
            add_habit(habits, name)

        elif choice == "2":
            if not habits:
                print("There is currently no added habits")
            else:
                show_habits(habits)
        elif choice == "3":
            try:
                index = int(input("Please enter your index:"))
                if 0 <= index < len(habits):
                    complete_habit(habits,index)
                else:
                    print("Invalid index")
            except ValueError:
                print("Invalid input")

        elif choice == "4":
            save_habits(habits,filename)
            print("Saved")


        elif choice == "5":
            try :
                index = int(input("Please enter your index"))
                if 0 <= index < len(habits):
                    toggle_habit(habits, index)
                    print("Toggled")
                else:
                    print("Invalid index")
            except ValueError:
                print("Invalid input")
        elif choice == "6":
            if not habits:
                print("There is not habits for you to delete.")
                continue
            else :
                try:
                    index = int(input("Please enter the index you want to delete."))
                    if 0 <= index < len(habits):
                        delete_habit(habits,index)
                        print("Habit deleted")
                    else:
                        print("Invalid index")
                except ValueError:
                    print("Invalid input")



        elif choice == "0":
            save_habits(habits,filename)
            break

        else:
            print("Invalid option")









if __name__ == "__main__":
    main()





















