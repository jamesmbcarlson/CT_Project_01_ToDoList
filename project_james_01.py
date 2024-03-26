# James Carlson 
# Coding Temple - SE FT-144
# Module 2: Mini-project | To-Do list Application

# colors for color coordination
COLOR_RED = "\033[91m"
COLOR_YELLOW = "\033[93m"
COLOR_GREEN = "\033[92m"
COLOR_RESET = "\033[0m"

# global To-Do list for use across the application
task_list = []

def tasks_add():
    """
    Prompt user for new task to add to To-Do List.
    """

    new_task = input("What task shall we add? ")
    task_list.append(new_task)
    print(f"\"{new_task}\" added to your to-do list at position {len(task_list)}.\n")

def tasks_view():
    """
    Print To-Do List to terminal.
    """

    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. Hopefully, that means you can take it easy!\n")

    else:
        # display every item in numbered list
        print("To-Do:")
        for i in range(len(task_list)):

            # color coordinate urgency of tasks 
            # GREEN = COMPLETE
            if str(task_list[i]).startswith("COMPLETE: "):
                text_color = COLOR_GREEN
            # RED = PRIORITY
            elif str(task_list[i]).startswith("PRIORITY: "):
                text_color = COLOR_RED
            # YELLOW = NORMAL
            else:
                text_color = COLOR_YELLOW
            print(f"{text_color}{i + 1}. {task_list[i]}{COLOR_RESET}")
        print()

def find_input(action):
    """
    Prompt user for To-Do List item to find.
    
    Parameters
    ----------
    action: str
        Specify to user which operation is occuring.

    Returns
    -------
    task_to_find : str
        To-Do item searched for by user.
    None
        None is returned if operation is cancelled by user.
    """
    
    # display To-Do List for reference
    tasks_view()

    # get input for which item user would like to select
    while True:
        task_to_find = input(f"Which item would you like to {action}? ")

        # if task_to_find.startswith("COMPLETE: ") or task_to_find.startswith("PRIORITY: "):
        #     task_to_find = task_to_find[10:]

        # handle string match
        if task_to_find in task_list:
            return task_to_find
        
        # handle numerical selection
        elif task_to_find.isdigit() and int(task_to_find) > 0 and int(task_to_find) <= len(task_list):
            return task_list[int(task_to_find) - 1]
        
        # exit while loop without making selection
        elif task_to_find.casefold() == "cancel":
            return None
        
        # handle input not matching item on list
        else:
            print(f"Item \"{task_to_find}\" could not be found. Try again or enter \"cancel\" to return to the main menu.\n")

def get_binary_input(prompt):
    """
    Prompt user to give a yes or no answer for a given question.

    Parameters
    ----------
    prompt: str
        Pass in question for which a yes or no answer is required.

    Returns
    -------
    : bool
        Return True or False as determined by user.
    """
    while True:
        binary_input = input(prompt).casefold()
        if binary_input == "yes" or binary_input == "y":
            return True
        elif binary_input == "no" or binary_input == "n":
            return False
        else:
            print("Please respond with \"yes\" or \"no\"")


def tasks_complete():
    """
    Prompt user for task on To-Do List to mark as complete.

    Complete tasks will be displayed in green text, with the prefix "COMPLETE," and be placed at the bottom of the list.
    """
    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. Add some tasks so you can check them off!\n")

    else:
        # prompt user to specify which task to mark as complete
        task_to_mark = find_input("mark complete")

        # handle search cancel
        if task_to_mark == None:
            return
        
        # handle task already marked as complete
        elif str(task_to_mark).startswith("COMPLETE: "):
            print(f"\"{task_to_mark[10:]}\" has already been marked as complete!")
            if get_binary_input(f"Would you like to unmark \"{task_to_mark[10:]}\" as complete? (yes/no) "):
                task_list[task_list.index(task_to_mark)] = task_to_mark.replace("COMPLETE: ", "")

        # handle priority task changed to complete
        elif str(task_to_mark).startswith("PRIORITY: "):
            task_mark_slice = task_to_mark[10:]
            task_list.pop(task_list.index(task_to_mark))
            task_list.append("COMPLETE: " + task_mark_slice)
            print(f"\"{task_to_mark}\" has been marked as {COLOR_GREEN}COMPLETE{COLOR_RESET}!\n")

        # modify task to show as complete and move task to bottom of list
        else:
            task_list.append("COMPLETE: " + task_list.pop(task_list.index(task_to_mark)))
            print(f"\"{task_to_mark}\" has been marked as {COLOR_GREEN}COMPLETE{COLOR_RESET}!\n")

def tasks_prioritize():
    """
    Prompt user for task on To-Do List to mark as priority.

    Priority tasks will be displayed in red text, with the prefix "PRIORITY," and be placed at the bottom of the list.
    """
    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. Add a task to prioritize!")

    else:
        # prompt user to specify which task to mark a priority
        task_to_mark = find_input("prioritize")

        # handle search cancel
        if task_to_mark == None:
            return
        
        # handle task already marked as priority
        elif str(task_to_mark).startswith("PRIORITY: "):
            print(f"\"{task_to_mark[10:]}\" has already been marked as a priority!")
            if get_binary_input(f"Would you like to unmark \"{task_to_mark[10:]}\" as a priority? (yes/no) "):
                task_list[task_list.index(task_to_mark)] = task_to_mark.replace("PRIORITY: ", "")

        # handle completed task changed to priority
        elif str(task_to_mark).startswith("COMPLETED: "):
            task_mark_slice = task_to_mark[10:]
            task_list.pop(task_list.index(task_to_mark))
            task_list.append("PRIORITY: " + task_mark_slice)
            print(f"\"{task_to_mark}\" has been marked as a {COLOR_RED}PRIORITY{COLOR_RESET}!\n")

        # modify task to show as a priority and move task to the top of list
        else:
            task_to_mark = "PRIORITY: " + task_list.pop(task_list.index(task_to_mark))
            task_list.insert(0, task_to_mark)
            print(f"\"{task_to_mark[10:]}\" has been marked as a {COLOR_RED}PRIORITY{COLOR_RESET} and has been moved to the top of your list!\n")


def tasks_delete():
    """
    Prompt user for task on To-Do List to delete.
    """

    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. There is nothing to delete.\n")

    else:
        # prompt user to specify which task to delete
        task_to_delete = find_input("delete")

        # handle search cancel
        if task_to_delete == None:
            return
        
        # modify task to show as complete and move task to bottom of list
        else:
            task_list.remove(task_to_delete)
            print(f"\"{task_to_delete}\" has been removed from your to-do list.\n")

# welcome user and display main menu options
print("\nWelcome to the To-Do List App!\n")
while True:
    print("Menu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Prioritize a task")
    print("5. Delete a task")
    print("6. Quit")

    # call application function based on user input
    menu_input = input("Make a selection: ").casefold()
    print()

    if menu_input.startswith("1") or menu_input.startswith("add"):
        tasks_add()
    elif menu_input.startswith("2") or menu_input.startswith("view"):
        tasks_view()
    elif menu_input.startswith("3") or menu_input.startswith("mark"):
        tasks_complete()
    elif menu_input.startswith("4") or menu_input.startswith("prioritize"):
        tasks_prioritize()
    elif menu_input.startswith("5") or menu_input.startswith("delete"):
        tasks_delete()
    elif menu_input.startswith("6") or menu_input.startswith("quit"):
        print("Thank you for using the To-Do List App!")
        break
    else:
        print("Invalid input. Please try another selection.\n")