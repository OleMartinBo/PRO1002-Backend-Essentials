# Exercise 1. File to List Converter

# Prompt the user for a filename.
filename = input("Enter the filename you want to convert to a list: ")

#Open the file
with open(filename, 'r') as f:
    languageList = f.readlines()  # Read all lines from the file into a list.
#Strip whitespace from each line
languages =[lang.strip() for lang in languageList] 
#Print the resulting list.
print(languages)

#Handle the case where the file doesn't exist using try/except and print an error message.
