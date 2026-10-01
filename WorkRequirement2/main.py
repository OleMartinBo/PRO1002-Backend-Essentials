import tasks #In your main script, import tasks.py. (Exercise 2)




# Exercise 2. Task List Manager (with separate module)
task_list = [] #Start with an empty list

#Repeatedly ask the user for input: "add " or "remove ".
while True:
    user_input = input('Add or remove task from list: ').lower() #Asks the user for input and converts it to lowercase
    
    if user_input.lower() == 'done': #Exit when the user types "done".
        break
    elif user_input.lower() == 'add': #Checks if the input is equal to 'add'
        break
    elif user_input.lower() == 'remove': #Checks if the input is equal to 'remove'
        break
    else:
        print('Input not valid!') #Prints an error message if the input is not valid
    
    print(f'Your task list: {task_list}') #Print the updated list after each operation.