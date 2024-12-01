name = input("What is your name?: ")

age = input("How old are you?: ")
age = int(age)

year = 2024 - age + 100

outputText = name
outputText += " you will be 100 years old in the year "
outputText += str(year)

print(outputText)