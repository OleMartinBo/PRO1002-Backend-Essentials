# Exercise 2. Task List Manager (with separate module)

#Create a Python module named tasks.py that contains two functions:

#add_task(task_list, task)
def add_task(task_list, task):
    task_list.append(task)
       
#remove_task(task_list, task)
def remove_task(task_list, task):
    task_list.remove(task)
   
#Start with an empty list, repeatedly ask the user for input: "add " or "remove ".
#Use the imported functions to modify the list, and print the updated list after each operation.
#Exit when the user types "done".