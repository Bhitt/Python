### Purpose: 
###     Analyze the results of staying with the first door choice
###     or changing to the other door.

# library imports
import numpy
from datetime import datetime

# initialize some variables
winCount = 0
lossCount  = 0

# prompt the user for the number of games we want to play
print("#############################")
print("This is the Monty Hall Game,\n"
      "Let's make a deal!")

numGames = 1
numGames = input("How many games would you like to play? (1 - 4e9):\n")
if (not numGames.isnumeric()):
    numGames = "100"  # default to 100 games if there is bad input
numGames = int(numGames) # remember to change the input from a string to a numeric

# prompt the user to see if they would like to stay or change
stayChoice = "S"
stayChoice = input("\nAre you going to stay given the opportunity?\n"
                   "Type S for Stay or anything else to change:\n")

# if the number of games simulated is large, find 1 percent for output
if (numGames > 1000000):
    onePercent = numGames / 100

# print out the simulation start time
startTime = datetime.now()
print ("\nStart of simulation: " + startTime.strftime("%H:%M:%S"))
# loop to simulate the results
for x in range(1, numGames+1):
    # randomly choose your door
    ourDoor = numpy.random.randint(1,4)

    # randomly choose the prize door
    prizeDoor = numpy.random.randint(1,4)

    # randomly choose the door to open
    # the door can't be the same as our door or the prize door
    openDoor = numpy.random.randint(1,4)
    while ((openDoor == ourDoor) or(openDoor == prizeDoor)):
        openDoor = numpy.random.randint(1,4)
    
    # swap the door if given the opportunity and choosing to swap
    if ((stayChoice != 'S') and (stayChoice != 's')):
        # find what the other door needs to be so that we can swap
        # the other door can't be our door or the open door
        otherDoor = numpy.random.randint(1,4)
        while((otherDoor == openDoor) or (otherDoor == ourDoor)):
            otherDoor = numpy.random.randint(1,4)
        # we found the other door, so swap
        ourDoor = otherDoor
    
    # now statistically count how many wins and losses
    if (ourDoor == prizeDoor):
        winCount += 1
    else:
        lossCount += 1
    # if simulating a large number of games,
    # output each time you simulate 1 percent of the games
    if (numGames > 1000000):
        if (x % onePercent == 0):
            currentPercent = (x / numGames) * 100
            print ("simulated " + str(currentPercent) + "% of the games...")

# print the time it took to simulate
endTime = datetime.now()
print ("End of simulation: " + endTime.strftime("%H:%M:%S"))
totalTime = endTime - startTime
print ("Simulation time: " + str(totalTime))

# Find the percentage results
percentWin = (winCount / numGames) * 100
percentLoss = (lossCount / numGames) * 100

# convert the results to strings for output
percentWin = str(percentWin)
percentLoss = str(percentLoss)
numGames = str(numGames)
winCount = str(winCount)
lossCount = str(lossCount)

# Output the results
print("\nOut of " + numGames + " games played!")
if ((stayChoice == 'S') or (stayChoice == 's')):
    print("I am not changing my door and...\n")
else:
    print("I am changing my door and...\n")
print("I win -> " + winCount + " times : " + percentWin + "%")
print("vs losing -> " + lossCount + " times : " + percentLoss + "%")