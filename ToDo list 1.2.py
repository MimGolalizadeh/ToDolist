description = f"\nThis is Handy, Handy is ToDo application which helps you to make your list of daily" \
              f" tasks and duties and check which is done and which is undone."
print(description)

# Definition CheckStatus - this module check the number of task and screen the proper message
def checkstatus(number_of_tasks):
    if number_of_tasks <= 4:
        print(f"{user_name}, you have {number_of_tasks} task(s) for today, you can do more.")
    elif number_of_tasks >= 6:
        print(f"{user_name}, you have {number_of_tasks}, you have no time to do more today.")

# Getting information from user and building a list of tasks
user_name = input("Please write your name: ").title()
todolist = [(input(f"Hello {user_name}, what's your plan for today? "))]

# First page menu - this while loop works until exit command
stop = True
while stop != False:
    number_of_tasks = len(todolist)
    checkstatus(number_of_tasks)
    description = f" {'-' * 50}\nChoose an option for more: \n 1.Add more tasks for today \n" \
                  f" 2.Delete a task from your list \n " \
                  f"3.Show your ToDo list \n 4.Remove first item from the list \n 5.exit\n {'-' * 50}"
    print(description)
    action = input(f">? ")
    action = int(action)
    quit = "yes"
    # Add a task to the list
    if action == 1:
        while quit != "no":
            todolist.append(input(f"what's your next task? "))
            quit = input(f"Do you want to continue?(Yes/No) ").lower()
    # Delete a custom tasks from list
    elif action == 2:
        while quit != "no":
            for index, items in enumerate(todolist):
                print(index + 1, items)
            todolist_item_remove = input(f"Which task do you want to remove? (indicate task by its number) ")
            todolist_item_remove = int(todolist_item_remove)
            todolist.pop(todolist_item_remove - 1)
            for index, items in enumerate(todolist):
                print(index + 1, items)
            quit = input(f"Do you want to continue?(Yes/No) ").lower()
    # Show thi list of tasks
    elif action == 3:
        number_of_tasks = len(todolist)
        if number_of_tasks <= 4:
            print(f"{user_name}, you have {number_of_tasks}, you have can do more today.")
        elif number_of_tasks >= 6:
            print(f"{user_name}, you have {number_of_tasks}, you have no time to do more today.")
        for index, items in enumerate(todolist):
            print(index+1,items)
    # Remove the first item from the list
    elif action == 4:
        del todolist[0]
        for index, items in enumerate(todolist):
            print(index + 1, items)
    # Exit option works with number 5 or any other numbers
    else:
        stop = False
