# Purpose:
#   Calculate a pay check
#

def main():
    # declare some function variables
    hoursWorked = 0
    payRate = 0
    otRate = 1.5 # multiplicative factor
    ot = 40 # when overtime begins (hr)
    payCheck = 0

    # prompt for inputs
    hoursWorked = int(input("How many hours did you work this week:\n"))
    payRate = int(input("What is your pay rate ($'s/hr):\n"))

    # calculate the paycheck
    if (hoursWorked < ot):
        payCheck = payRate * hoursWorked
    else:
        payCheck = payRate * (hoursWorked + (otRate-1)*(hoursWorked-ot))

    # output the paycheck
    print("Gross pay = $"+str(payCheck))

    payTaxes = input("\nWould you like to pay taxes(y/n):\n")
    if (payTaxes == "y"):
        print("Take home = $"+str(payCheck - (payCheck*0.20)))

if __name__ == '__main__':
    main()