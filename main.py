# TO_DO LIST APPP (CONSOLE)

import sys


tasks = []

#  Function to display a task
def view_task():
    if not tasks:
        print("Your To-Do list is empty!\n")
        return 
    else:
        print("These are you tasks : ")
        for index, task in enumerate(tasks, start=1):
            print(f"{index}. {task}")
        print("")

# Function to remove a task
def remove_task():
    # Prevent in case the list is empty
    if not tasks:
        print("No task to remove!\n")
        return 
    
    view_task()
    task_to_remove = input("Enter the number of the task you want to remove  : ").strip()

    # Check if the input is a number
    if not task_to_remove.isdigit():
        print("Invalid input, enter a number.\n")
        return
    
    index = int(task_to_remove) - 1
    if 0 <= index < len(tasks):
        removed_task = tasks.pop(index)
        print(f"Task successfully deleted: {removed_task}\n")
    else:
        print("Number out of range, try again.")
        return

    print("Updated tasks :")
    view_task()
    # for i, task in enumerate(tasks, start=1):
    #     print(f"{i}. {task}")


while True:

    print("+------------------------+")
    print("|     MENU PRINCIPAL     |")
    print("+------------------------+")
    print("")

    print(" 1. Add task \n 2. View tasks \n 3. Remove task \n 4. Quit")
    print("")

    # Ask the user what he want to do
    choice = input("What do you want to do ? Choose in the menu : ").strip()
    print("")
    # Add a task
    if choice == "1":
        task_to_add = input("Add a task: ").strip()
        if not task_to_add:
            print("Task cannot be empty!\n")
        elif task_to_add in tasks:
            print("This task already exists in your list!\n")
        else:
            tasks.append(task_to_add)
            print("Task added successfully! \n")

    # View tasks
    elif choice == "2":
        view_task()

    # Remove task
    elif choice == "3":
        remove_task()
      
    # Exit the program
    elif choice == "4":
        print("Goodbyyyyyye!\n")
        sys.exit()
    
    else:
        print("This number does not correspond to any menu item.")


        







