import numpy

# Purpose:
#   Use a simple method to sort a list of numbers
#   Runtime : O(n^2)

def SelectionSort(arr):
    # get the array size
    n = len(arr)

    # return early if the array is too small
    if (n <= 1): 
        return arr

    # traverse through all array elements
    for i in range(n):
        # find the minimun element for the remaining unsorted portion
        minIndex = i
        for j in range(i+1, n):
             # found a new minimum
             if (arr[j] < arr[minIndex]):
                 minIndex = j
        
        # swap the two elements using python convention
        # x, y = y, x
        arr[i], arr[minIndex] = arr[minIndex], arr[i]

def CreateRandomArray():
    # create the empty array
    arr = []
    # fill the array with 10 random numbers
    n = 10
    for i in range(n):
        r = numpy.random.randint(1,30)
        arr.append(r)
    # return the resulting array
    return arr

def PrintArray(arr):
    # get the size of the array
    n = len(arr)
    # traverse through all elements and print them
    outputString = ""
    for i in range(n):
        # add commas between entries
        if (i > 0):
            outputString += ","
        outputString += str(arr[i])
    # output
    print(outputString)

def main():
    # get a random list of numbers
    arr = CreateRandomArray()

    # print before sorting
    print("Before Sorting:")
    PrintArray(arr)

    # call the selection sort
    SelectionSort(arr)

    # print after sorting
    print("After Sorting:")
    PrintArray(arr)


if __name__ == "__main__":
    main()