import tasks #Main script imports tasks.py for Exercise 2




#Exercise 2. Task List Manager (with separate module)
#Starts with an empty list.
task_list = [] 

#Repeatedly ask the user for input: "add", "remove", or "done".
while True:
    #Asks the user for input and converts it to lowercase
    user_input = input('Write "add" or "remove" to modify the task list. Enter "done" to finish: ').lower() 
   
   #Exit when the user types "done", prints a message indicating that the Task List Manager is closed, and the final task list.
    if user_input == 'done': 
        print(f'Task List Manager closed.\nYour final task list: {task_list}') 
        break
    
    #Checks if the input is equal to 'add' and asks the user for new input to add a task.
    elif user_input == 'add': 
        task = input('Enter a task to add: ').lower()
        tasks.add_task(task_list, task) 
        print(f'You have added "{task}" to the list.') 
 
    #Checks if the input is equal to 'remove' and asks the user for new input to remove a task.
    elif user_input == 'remove': 
        task = input('Enter a task to remove: ').lower() 
        
        # If the wanted removed task is in the list, it will return True and remove the task.
        if tasks.remove_task(task_list, task):
            print(f'You have removed "{task}" from the list.')
    
    #Prints an error message if the input is not valid and prompts the user to try again.
    else:
        print('Input not valid! Try again. Please enter "add", "remove" or "done".')
    
    #Print the updated list after each operation.
    print(f'Your current task list: {task_list}')