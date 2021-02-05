
todo_list = [{"item": "one", "import": "low"}, {"item": "two", "import": "med"}]


def menu():
    print("Press 1 to add task")
    print("Press 2 to delete task")
    print("Press 3 to view all tasks")
    print("Press q to quit")
    choice()
    

def print_todo():
    print("\nYou're todo list items are:\n")
    for index in range(0, len(todo_list)):
        numm = str(index + 1)
        task = todo_list[index]
        print(numm + " - " + task["item"] + " - " + task["import"])
    print("\n\n")
    menu()


def choice():
    char = input(">>")
    if char == "1":
        add()
    elif char == "2":
        delete()
    elif char == "3":
        print_todo()
    elif char == "q":
         quit()
    else:
        print("That's not a choice, please try again:")
        choice()

def add():
    new_task = input("What task are we adding? >  ")
    new_import = input("How important is the task? >  ")

    task = {"item": new_task, "import": new_import}

    todo_list.append(task)
    print("\n\n******** Task Has Been Added ********\n\n")
    menu()

def delete():
    print("\n\nYou're todo list items are:\n")
#Copied my print to clarify numbers before choice
    for index in range(0, len(todo_list)):
        numm = str(index + 1)
        task = todo_list[index]
        print(numm + " - " + task["item"] + " - " + task["import"])
#Now for the delete option
    remove = int(input("\nWhich number shall we remove?"))
    del todo_list[(remove-1)]
    print(f"\n ****** Number {remove} has been removed from your list. ******\n\n")
    menu()

def quit():
    print("\n\n ** Goodbye! **\n\n")


menu()

