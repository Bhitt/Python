import numpy

def main():
    # initialize the number of games
    numGames = 3

    # initialize the valid choices in a list
    validChoices = ["rock","paper","scissors"]
    
    for game in range(0,numGames):
        # ask for the user input
        print("~~~~~~~~~~~~~~~~~~~~")
        userChoice = input("Would you like rock, paper, or scissors:\n")
        while(userChoice not in validChoices):
            userChoice = input("Would you like rock, paper, or scissors:\n")
        
        # get the ai's input
        index = numpy.random.randint(0,len(validChoices))
        aiChoice = validChoices[index]

        # call the function
        print ("Game "+str(game)+":")
        determineWinner(userChoice, aiChoice)


def determineWinner(userChoice, aiChoice):
    print ("The ai chose: "+aiChoice)

    if (userChoice == "rock"):
        if (aiChoice == "rock"):
            print("Tie game.")
        elif (aiChoice == "paper"):
            print("rock loses to paper. You lose!")
        else:
            print("rock beats scissors. You win!")
    elif (userChoice == "paper"):
        if (aiChoice == "rock"):
            print("paper beats rock. You win!")
        elif (aiChoice == "paper"):
            print("Tie game.")
        else:
            print("paper loses to scissors. You lose!")
    else:
        if (aiChoice == "rock"):
            print("scissors loses to rock. You lose!")
        elif (aiChoice == "paper"):
            print("scissors beats paper. You win!")
        else:
            print("Tie game.")

if __name__ == '__main__':
    main()