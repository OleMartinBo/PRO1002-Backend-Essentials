import tasks #In your main script, import tasks.py. (Exercise 2)




# Exercise 2. Task List Manager (with separate module)
task_list = [] #Starts with an empty list

#Repeatedly ask the user for input: "add " or "remove ".
while True:
    user_input = input('Add or remove task from list: ').lower() #Asks the user for input and converts it to lowercase
    
    if user_input.lower() == 'done': #Exit when the user types "done".
        print('Task List Manager closed.') #Prints a message indicating that the Task List Manager is closed
        break
    elif user_input.lower() == 'add': #Checks if the input is equal to 'add'
        task = input('Enter a task to add: ').lower() #Asks the user for a task to add
        tasks.add_task(task_list, task) 
    elif user_input.lower() == 'remove': #Checks if the input is equal to 'remove'
        task = input('Enter a task to remove: ').lower() #Asks the user for a task to remove
        tasks.remove_task(task_list, task)
    else:
        print('Input not valid!\n') #Prints an error message if the input is not valid
    
    print(f'Your task list: {task_list}') #Print the updated list after each operation.
    

#user_input[:] #Gets the task from the user input)