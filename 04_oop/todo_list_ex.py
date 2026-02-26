class Task:
    def __init__(self, title):
        self._title = title
        self._done = False

    def get_title(self):
        return self._title

    def set_title(self, new_title):
        if not new_title.strip():
            return  False
        else:
            self._title = new_title
            return True
    def is_done(self):
        return self._done


    def mark_done(self):
        self._done = True

    def display(self):
        if self._done:
           return f'[X] {self._title}'
        else:
            return  f'[ ] {self._title}'

    def toggle(self):
        self._done = not self._done



class TodoList:
    def __init__(self):
        self.tasks: list[Task] = []   # plural is clearer

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_all(self):
        if not self.tasks:
            print("No tasks yet")
            return
        for i, t in enumerate(self.tasks):
            print(f"{i}: {t.display()}")

    def toggle_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].toggle()
            return True
        return False


    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
        else:
            print("Invalid index")

    def remove_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid index")

    def save_to_file(self,filename):
        with open(filename , 'w', encoding ="utf-8") as f:
            for task in self.tasks:
                done_flag = '1' if task.is_done() else "0"
                f.write(f"{done_flag}|{task.get_title()}\n")

    def show_completed(self):
        if not self.tasks:
            print("No tasks added.")
            return

        completed = []

        for task in self.tasks:
            if task.is_done():
                completed.append(task)

        if not completed:
            print("No completed tasks.")
            return

        for task in completed:
            print(task.display())


    def show_pending(self):
        if not self.tasks:
            return

        pending = []

        for task in self.tasks:
            if not task.is_done():
                pending.append(task)

        if not pending:
            print("No tasks are pending")
            return

        for task in pending:
            print(task.display())


    def load_from_file(self,filename):
        self.tasks = []

        try:
            with open(filename, "r" , encoding="utf-8") as f:
                for line in f:
                    line = line.rstrip("\n")
                    if not line:
                        continue
                    done_flag , title = line.split("|",1)
                    task = Task(title)
                    if done_flag == "1":
                        task.mark_done()
                    self.tasks.append(task)

        except FileNotFoundError:
            print("No file was found")

    def edit_title(self, index , new_title):

        if not new_title.strip():

            return False
        if 0 <= index < len(self.tasks):
            return self.tasks[index].set_title(new_title)

        else :
            return False
















def main():
    todo = TodoList()
    todo.load_from_file("tasks.txt")

    while True:
        print("\n1. Add task")
        print("2. Show tasks")
        print("3. Mark task done")
        print("4. Remove task")
        print("5. Exit")
        print("6. Save")
        print("7. Load")
        print("8. Show completed")
        print("9. Show pending")
        print("10. Edit task title")
        print("11. Toggle")

        choice = input("Choose option: ").strip()

        if choice == "1":
            title = input("Please enter title: ").strip()
            if not title:
                print("Title cannot be empty.")
            else:
                todo.add_task(title)

        elif choice == "2":
            todo.show_all()

        elif choice == "3":
            try :
                index = int(input("Please enter your index"))
                todo.mark_task_done(index)

            except ValueError:
                print("Index must be a number")

        elif choice == "4":

            try:
                index = int(input("Please enter your index"))
                todo.remove_task(index)
            except ValueError:
                print("Invalid input")

        elif choice == "6":
            todo.save_to_file("tasks.txt")
            print("Saved.")

        elif choice == "7":
            todo.load_from_file("tasks.txt")
            print("Loaded.")

        elif choice == "8":
            todo.show_completed()


        elif choice == "9":
            todo.show_pending()

        elif choice == "10":

            try:
                index = int(input("Please enter the index of the title you wish to update: "))
                new_title = input("Please enter the new title: ")

                result = todo.edit_title(index, new_title)

                if result:
                    print("Task updated successfully.")
                else:
                    print("Update failed.")

            except ValueError:
                print("Index must be a number.")





        elif choice == "5":
            todo.save_to_file("tasks.txt")
            print("Goodbye")
            break

        elif choice == "11":
            index = int(input("Please enter the index you wish to toggle:"))
            todo.toggle(index)






        else:
            print("Invalid option")


if __name__ == "__main__":
    main()



