# import the library numpy so we can generate random numbers
import numpy

# create some fun text for the treasure or for failing
treasureText = r"""         __________
        /\____;;___\
       | /         /
       `. ())oo() .
        |\(%()*^^()^\
       %| |-%-------|
      % \ | %  ))   |
      %  \|%________|"""
failureText = r"""                           ,--.
                          {    }
                          K,   }
                         /  `Y`
                    _   /   /
                   {_'-K.__/
                     `/-.__L._
                     /  ' /`\_}
                    /  ' /   
            ____   /  ' /
     ,-'~~~~    ~~/  ' /_
   ,'             ``~~~%%',
  (                     %  Y
 {                      %% I
{      -                 %  `.
|       ',                %  )
|        |   ,..__      __. Y
|    .,_./  Y ' / ^Y   J   )|
\           |' /   |   |   ||
 \          L_/    . _ (_,.'(
  \,   ,      ^^""' / |      )
    \_  \          /,L]     /
      '-_`-,       ` `   ./`
         `-(_            )
             ^^\..___,.--`"""

# create some intro text and print it
introText = """########################################

You find yourself in a dark and cold dungeon room.
Before you are three decrepit doors...

Open the correct one,
and you will manage to escape to the treasury full of gold.

However, if you choose poorly....

You will soon meet your DEMISE!!!

########################################"""
print (introText)

# prompt the user to choose a door
promptText = "Type in the door you wish to open: 1, 2, or 3\n"

# grab the first input from the user
doorChoice = input (promptText)
# initialize a boolean variable to False so that
# we can loop until the input is validated
isValidChoice = False

# we want to make sure the user types in a number in this case
# loop until we have valid input
while (not isValidChoice):
    # test to see if the input is numeric
    if (not doorChoice.isnumeric()):
        print ("That's not even a number! Pick again.\n")
    else:
        # if the input is numeric, cast it to an int
        doorNumeric = int (doorChoice)
        # after casting, test if the input is out of the correct range
        if (doorNumeric < 1 or doorNumeric > 3):
            print ("Please pick a valid door number.\n")
        # both conditions are satisfied, set the input validation variable to True
        else:
            isValidChoice = True
    # if the input wasn't validated from the above tests,
    # prompt for a new input and repeat the loop
    if (not isValidChoice):
        doorChoice = input (promptText)

# we now have valid input, cast it to the door number
doorChoice = int (doorChoice)

# pick the treasure door randomly!
treasureDoor = numpy.random.randint(1,4)

# output the success or failure
if (treasureDoor == doorChoice):
    print ("Congratulations!!!!!!\n You have found the treasure:\n")
    print (treasureText)
else:
    print (failureText)
    print ("This will be your end!!!")