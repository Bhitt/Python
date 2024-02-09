# Purpose:
#   Show that there is an effecient way to find an item
#       in a list of sorted items (in our case, numbers 1 to 1000).
#   Practice functions with the function findNextGuess()
#

# define the main function, where our program will begin
def main():
    # import numpy so that we can generate random numbers
    import numpy

    # print out the intro
    print("______________")
    print("If you pick a number from 1 to 1000, \nI promise I can guess it \nin 10 guesses or less.")
    input("Press enter to begin:")

    # initialize how many guesses we have left
    guessesRemaining = 10

    # initialize our first guess
    currentGuess = 500

    # initialize a starting low and high
    low = 0
    high = 1000

    # loop until we run out of guesses
    while (guessesRemaining > 0):
        # output how many guesses remain
        print("______________")
        print("GUESSES REMAINING: " + str(guessesRemaining))
        # output our next guess
        print("Is your number: " + str(currentGuess) + " ?")
        guessesRemaining = guessesRemaining - 1 # decrement the guesses remaining
        isCorrect = input("Type 1 for yes, or anything else for no: \n")
        # if we are correct, exit early
        if (isCorrect == "1"):
            break
        # prompt the user to find if their number is 
        # higher or lower than the current guess
        print("Was my guess too high or too low?")
        isTooLow = input("Type 'low' for too low, or anything else for too high:\n")
        # adjust the ranges based on the response
        if (isTooLow == "low"):
            low = currentGuess
        else:
            high = currentGuess
        # find the next guess using our function
        currentGuess = findNextGuess(low, high)
    
    # output the win or loss
    print("______________")
    if (guessesRemaining >= 0):
        print("Haha! I've guessed your number!")
    else:
        print("Uh oh?! How did I not guess your number correctly?...")


def findNextGuess(l, h):
    # divide the remaining area by 2
    nextGuess = (int)(l + ((h - l)/ 2))
    # return the halfway point
    return nextGuess

if __name__ == '__main__':
    main()