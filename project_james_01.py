# James Carlson 
# Coding Temple - SE FT-144
# Module 2: Mini-project | To-Do list Application

'''

    Implement input validation to handle unexpected user input gracefully.
IV. Error Handling:
    Implement error handling using try, except, else, and finally blocks to handle potential issues.
V. Code Organization:
    Organize your code into functions to promote modularity and readability.
    Use meaningful function names with appropriate comments and docstrings for clarity.
VI. Testing and Debugging:
    Thoroughly test your application to identify and fix any bugs.
    Consider edge cases, such as empty task lists or incorrect user input.
VII. Documentation:
    Include a README file that explains how to run the application and provides a brief overview of its features.
VIII. Optional Features (Bonus):
    If you feel adventurous, you can add extra features like task priorities, due dates, or color-coding tasks based on their status.
IX. GitHub Repository:
    Create a GitHub repository for your project.
    Commit your code to the repository regularly.
    Include a link to your GitHub repository in your project documentation.
'''

task_list = []

# add task to list
def tasks_add():
    new_task = input("What task shall we add? ")
    task_list.append(new_task)
    print(f"\"{new_task}\" added to your to-do list at position {len(task_list)}.")

# view to-do list
def tasks_view():
    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. Hopefully, that means you can take it easy!")
    else:
        # display every item in numbered list
        print("To-Do:")
        for i in range(len(task_list)):
            print(f"{i + 1}. {task_list[i]}")
        print()

# TO-DO: DELETE AFTER TESTING
# mark provided task as complete
# def mark_as_complete(task):
#     # TO-DO: ensure item is not already marked "COMPLETE: "
#     if str(task).startswith("COMPLETE: "):
#        print(f"\"{task}\" has already been marked as complete!")
#     else:
#         # move completed item to bottom of list
#         completed_task = "COMPLETE: " + task_list.pop(task_list.index(task))
#         task_list.append(completed_task)
#         print(f"\"{task}\" has been marked as COMPLETE!")

def find_input(action):
    tasks_view()
    # get input for which item user would like to select
    while True:
        task_to_find = input(f"Which item would you like to {action}? ")
        # handle string match
        if task_list.count(task_to_find) > 0:
            return task_to_find
        # handle numerical selection
        elif task_to_find.isdigit() and int(task_to_find) > 0 and int(task_to_find) <= len(task_list):
            return task_list[int(task_to_find) - 1]
        # exit while loop without making selection
        elif task_to_find.casefold() == "cancel":
            break
        # handle input not matching item on list
        else:
            print(f"Item \"{task_to_find}\" could not be found. Try again or enter \"cancel\" to return to the main menu.\n")

# mark task in list as complete
def tasks_complete():
    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. Add some tasks so you can check them off!")
    else:
        task_to_mark = find_input("mark complete")
        if task_to_mark == None:
            return
        elif str(task_to_mark).startswith("COMPLETE: "):
            print(f"\"{task_to_mark[10:]}\" has already been marked as complete!")
        else:
            # move completed item to bottom of list
            task_list.append("COMPLETE: " + task_list.pop(task_list.index(task_to_mark)))
            print(f"\"{task_to_mark}\" has been marked as COMPLETE!")

# TO-DO: DELETE AFTER TESTING
# def tasks_complete():
#     # handle empty list
#     if task_list == []:
#         print("Your to-do list is empty. Add some tasks so you can check them off!")
#     else:
#         tasks_view()
#         # get input for which item user would like to mark complete
#         while True:
#             task_to_mark = input("Which item would you like to mark complete? ")
#             # handle string match
#             if task_list.count(task_to_mark) > 0:
#                 mark_as_complete(task_to_mark)
#                 break
#             # handle numerical selection
#             elif task_to_mark.isdigit() and int(task_to_mark) > 0 and int(task_to_mark) <= len(task_list):
#                 mark_as_complete(task_list[int(task_to_mark) - 1])
#                 break
#             # cancel mark as complete task and return to main menu
#             elif task_to_mark.casefold() == "cancel":
#                 break
#             # handle input not matching item on list
#             else:
#                 print(f"Item \"{task_to_mark}\" could not be found. Try again or enter \"cancel\" to return to the main menu.\n")

# delete task in to-do list
def tasks_delete():
    # handle empty list
    if task_list == []:
        print("Your to-do list is empty. There is nothing to delete.")
    else:
        tasks_view()
        # get input for which item user would like to delete
        while True:
            task_to_remove = input("Which item would you like to delete? ")
            # handle string match
            if task_list.count(task_to_remove) > 0:
                task_list.remove(task_to_remove)
                print(f"\"{task_to_remove}\" has been removed from your to-do list.")
                break
            # handle numerical selection
            elif task_to_remove.isdigit() and int(task_to_remove) > 0 and int(task_to_remove) <= len(task_list):
                task_list.remove(task_list[int(task_to_remove) - 1])
                print(f"Item {task_to_remove} has been removed from your to-do list.")
                break
            # cancel delete task and return to main menu
            elif task_to_remove.casefold() == "cancel":
                break
            # handle input not matching item on list
            else:
                print(f"Item \"{task_to_remove}\" could not be found. Try again or enter \"cancel\" to return to the main menu.\n")


print("\nWelcome to the To-Do List App!")

while True:
    print("\nMenu:")
    print("1. Add a task")
    print("2. View tasks")
    print("3. Mark a task as complete")
    print("4. Delete a task")
    print("5. Quit")

    menu_input = input("\nMake a selection: ").casefold()
    print()

    if menu_input.startswith("1") or menu_input.startswith("add"):
        tasks_add()
    elif menu_input.startswith("2") or menu_input.startswith("view"):
        tasks_view()
    elif menu_input.startswith("3") or menu_input.startswith("mark"):
        tasks_complete()
    elif menu_input.startswith("4") or menu_input.startswith("delete"):
        tasks_delete()
    elif menu_input.startswith("5") or menu_input.startswith("quit"):
        print("Thank you for using the To-Do List App!")
        break
    else:
        print("Invalid input. Please try another selection.")