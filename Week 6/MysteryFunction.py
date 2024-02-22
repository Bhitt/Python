def main():
    # prompt for a number, message, and name
    number = input ("Please enter a number:\n")
    while(not number.isnumeric):
        number = input ("Please enter a number:\n")
    number = int(number)
    message = input ("Please enter a message:\n")
    name = input("Please enter a name:\n")

    # call our mystery function
    MysteryFunction(number, message, name)


def MysteryFunction(num, m, name):
    # print the message over and over, taking away 1 character until none are left
    while(len(m) > 0):
        print(m)
        m = m[:-1]
    # print a silly statement
    print(name+", you owe me $"+str(num)+"!!!")



if __name__ == '__main__':
    main()