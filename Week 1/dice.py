# import the external library 'numpy' so that we have a random number generator
import numpy as np

# print some output
msg = "Rolling a dice..."
print (msg)

# print a random number from  (1-6]
# the left is included because it is inclusive : (1
# the right side is excluded because it is exclusive : 6]
# which then randoms any of the numbers : 1,2,3,4,5
print (np.random.randint(1,6))


msg = "Rolling again..."
print (msg)


myNumber = np.random.randint(1,6)
print(myNumber)
# if the random number assigned to the variable 'myNumber' is 3 or less, print 'I WIN'
if (myNumber <= 3) :
    print("I WIN")
# if the random number is 6, print 'Nichole Wins'
elif (myNumber == 6):
    print("Nichole Wins!!!!! EVILLLLLLL MOMMY")
# in all other cases, print 'MADDEN WINS'
else :
    print("MADDEN WINS")
