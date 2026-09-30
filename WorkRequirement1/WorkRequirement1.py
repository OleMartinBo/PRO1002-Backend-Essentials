#1. Greeting and Age Check
name = input("Hello! Please enter your name: ")
age = int(input("Hello, " + name + "! How old are you)? "))

if age < 18:
    print("Sorry,"+ name + ", you are too young.")
else:
    print("Greetings, " + name + "! You can enter.")

    
#2. Number List Processor
n = int(input("Please enter a numbers of your choice: "))

numbers = []

for i in range(1, n + 1):
    numbers.append(i)
    
print("The list of numbers is: ", numbers)
    
if n > 5:  
    print("The list is too long.")
elif n == 5:
    print("The list is just right.")
else:
    print("The list is too short.")


#3. Sum of User Inputs
n= []

for i in range(3):
    inputNumbers = int(input("Please enter " + str(i + 1) + " number: "))
    n.append(inputNumbers)
    
print("The list of numbers is: ", n)


total = sum(n)
print("The sum of the numbers is: ", total)

if total %2 == 0:
    print("Your sum is even")
else: 
    print("Your sum is odd")


#4. Fruit Basket
fruitDictionary = {
    "apple": 1, 
    "banana": 5, 
    "orange": 2, 
    "grape": 10
    }

userPrompt = input("Please enter a fruit name: ").lower()

if userPrompt in fruitDictionary:
    if fruitDictionary[userPrompt] == 1:
        print("There is only " + str(fruitDictionary[userPrompt]) + " available " + userPrompt + " left in the basket.")
    else:
        print("There is " + str(fruitDictionary[userPrompt]) + " available " + userPrompt + "s" + " in the basket.")

    for letters in userPrompt:
        print(letters)
    
else:
    print("We don't have that fruit.")


#5. Temperature Converter
temperatureInput = input("Please enter the temperature in Celsius: ")

temperatureCelsius = float(temperatureInput)

convertFormula = (temperatureCelsius * 9/5) + 32
print("The temperature in Fahrenheit is: " + str(convertFormula))

if convertFormula > 80:
    print("It's hot!")
else:
    print("It's not too hot.")
    
differentTemperatures = [str(temperatureCelsius) + "°C", str(convertFormula) + "°F"] 
print("The list of temperatures is: ", differentTemperatures)