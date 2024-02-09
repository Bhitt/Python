# import the library numpy so that we can use a random number generator and the array type
import numpy

# initialize an array of strings
myArray = numpy.array(['a','b','c','d','e','f','g','h'])

# loop over the values in the array
# = "for the variable x equal to 0, run the below statement, then increment x by 1 until it is equal to the array size"
for x in range(0,myArray.size):
    # for each loop execution, test if the array element at the index x is equal to 'd'
    if (myArray[x] == 'd'):
        # if the test passed, print the index where the element was found
        print ("found the element at index: "+str(x))