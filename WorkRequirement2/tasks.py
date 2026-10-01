#Exercise 2. Task List Manager (with separate module)

#Function: Add task to the list
def add_task(task_list, task):
    task_list.append(task)
       
#Function: Remove task from the list and handle the case where the task is not found in the list
def remove_task(task_list, task): 
    if task in task_list:
        task_list.remove(task)
        return True
    else:
        print(f'Task "{task}" not found in the list.')
        return False