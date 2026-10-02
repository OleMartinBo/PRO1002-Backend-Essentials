#Exercise 1. File to List Converter

#Prompt the user for a filename.
filename = input('Enter the filename you want to convert to a list: ')

#Handles the try/except for file to List Converter
try:
    #Open the file
    with open(filename, 'r') as f:
        languageList = f.readlines()  # Read all lines from the file into a list.
    #Strip whitespace from each line
    languages =[lang.strip() for lang in languageList]

except FileNotFoundError as err:
    #Handle the case where the file doesn't exist
    print(err, 'Try again!')
else:
    #Print the resulting list.
    print(languages)
    