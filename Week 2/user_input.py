# we can use print statements like this to section off the output for easier reading.
print("#########################################\n\n")

# use the 'input' function to capture user input.
# inside of the function we can pass a prompt string that will get printed.
# store the output of the function into the 'favoriteColor' variable.
favoriteColor = input("What is your favorite Color?:\n")

# use string concatenation to combine some text with the string value
# inside the favoriteColor variable and output the result
print("Your favorite color is: " + favoriteColor)

print("#########################################\n\n")

# prompt for a numeric value
number = input("Pick a number between 1 and 10:\n")
# be sure to cast the input string to an int
number = int(number)

# use if, else if, and else blocks to test the input
# the first test that passes will get executed...
# the remaining tests will get skipped
if (number == 1):
    print("Found a 1")
elif (number == 2):
    print("Found a 2")
elif (number == 3):
    print("Found a 3")
elif (number == 4):
    print("Found a 4")
elif (number == 5):
    print("Found a 5")
elif (number == 6):
    print("Found a 6")
elif (number == 7):
    print("Found a 7")
elif (number == 8):
    print("Found a 8")
elif (number == 9):
    print("Found a 9")
elif (number == 10):
    print("Found a 10")
# default block that will get executed if no above test passes
else:
    print("Number out of range")

print("#########################################\n\n")

# prompt for another numeric input
number = input("Pick a number between 1 and 99:\n")
# we can test the negation of something : 'not numeric'
if (not number.isnumeric()):
    print("Invalid input. That's not even a number!")
# if the input is numeric then we are safe to cast it into an int type
if (number.isnumeric()):
    number = int(number)

# if statements can also be used for ranges using <, >, <=, and >=
if (number < 1):
    print("Invalid input. Your number was less than 1")

if (number >= 100):
    print("Invalid input. Your number was greater than or equal to 100")

