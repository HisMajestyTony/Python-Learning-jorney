class Task:
    def __init__(self, title):
        self.title = title
        self.done = False


    def mark_done(self):
        self.done = True

    def display(self):
        if self.done:
           return f'[X] {self.title}'
        else:
            return  f'[ ] {self.title}'








class TodoList:
    def __init__(self):
        self.tasks = []   # plural is clearer

    def add_task(self, title):
        task = Task(title)
        self.tasks.append(task)

    def show_all(self):
        for i, t in enumerate(self.tasks):
            print(f"{i}: {t.display()}")


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
                done_flag = '1' if task.done else "0"
                f.write(f"{done_flag}|{task.title}\n")


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
            index = int(input("Please enter your index"))
            todo.mark_task_done(index)

        elif choice == "4":
            index = int(input("Please enter your index"))
            todo.remove_task(index)

        elif choice == "6":
            todo.save_to_file("tasks.txt")
            print("Saved.")

        elif choice == "7":
            todo.load_from_file("tasks.txt")
            print("Loaded.")


        elif choice == "5":

            break

        else:
            print("Invalid option")


if __name__ == "__main__":
    main()



