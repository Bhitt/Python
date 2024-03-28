# external libraries / modules
import numpy as np

#////////////////////////////
# GLOBAL VARIABLES
#////////////////////////////
HAS_AXE = False
HAS_PICKAXE = False
HAS_FISHINGPOLE = False

INV_WOOD = 0

TREE_HEALTH = 5

AVAILABLE_COMMANDS = ["Help","Exit","Harvest Wood"]
PREVIOUS_COMMAND = ""

#////////////////////////////
# terminal text color functions
#////////////////////////////
def prBold(s): print("\033[2m {}\033[00m" .format(s))
def prUnderline(s): print("\033[4m {}\033[00m" .format(s))
def prDanger(s): print("\033[31m {}\033[00m" .format(s))
def prInfo(s): print("\033[34m {}\033[00m" .format(s))
def prSpecial(s): print("\033[35m {}\033[00m" .format(s))
def prCyan(s): print("\033[36m {}\033[00m" .format(s))
def prChapterText(s): print("\033[46m {}\033[00m" .format(s))

def main():
    # output the game start text
    prChapterText("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    prChapterText("You find yourself deep in the woods, cold and alone...")
    prChapterText("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    prInfo("I should [HARVEST WOOD] for a campfire...           ")

    # core game loop
    keepPlaying = True
    while(keepPlaying):
        # call our core update function once per loop
        Update()

        # check for user input (1 action per loop)
        prCyan("-------------")
        keepPlaying = ProcessCommands()

def Update():
    # Check the status of resources
    UpdateTrees()
    

def UpdateTrees():
    # if the last tree was cut down, find a new tree with random health from 1 to 6
    global TREE_HEALTH
    if (TREE_HEALTH <= 0):
        TREE_HEALTH = np.random.randint(1,6+1)

def ProcessCommands():
    global AVAILABLE_COMMANDS
    global PREVIOUS_COMMAND
    # get the command
    command = input("c~: ").lower()
    # check for repeat command
    if (command == "r"):
        command = PREVIOUS_COMMAND

    # check for valid commands
    if (command  == "help"):
        C_Help()
    elif (command == "exit"):
        return False
    elif (command  == "harvest wood"):
        C_HarvestWood()
    elif (command == "look around"):
        C_LookAround()
    elif (command == "pick up axe"):
        C_PickUpAxe()
    elif (command == "count wood"):
        C_CountWood()
    else:
        PrintResponse("command: (" + command + ") not found. Type 'Help' for a list of commands")
        return True

    # keep track of the command
    PREVIOUS_COMMAND = command

    # no exit command so keep playing
    return True

def C_LookAround():
    global AVAILABLE_COMMANDS
    if (not HAS_AXE):
        prInfo("Peering over your shoulder, you notice a rusty axe lodged in a stump.")
        AVAILABLE_COMMANDS.append("Pick up axe")
    else:
        prInfo("You don't notice anything useful...")

def C_PickUpAxe():
    global AVAILABLE_COMMANDS
    global HAS_AXE
    # make sure the user does not already have an axe
    if (HAS_AXE):
        PrintResponse("You are already carrying an axe...")
    else:
        PrintResponse("You pull the axe from the stump.")
        HAS_AXE = True
        AVAILABLE_COMMANDS.append("Count Wood")

def C_CountWood():
    global INV_WOOD
    prInfo("I have " + str(INV_WOOD) + " wood.")

def C_HarvestWood():
    global AVAILABLE_COMMANDS
    global HAS_AXE
    global TREE_HEALTH
    global INV_WOOD
    # valiate the user has an axe first
    if (not HAS_AXE):
        prInfo("You attempt to harvest wood but do not yet have an axe...")
        prInfo("Perhaps you can [LOOK AROUND] for an axe to use.         ")
        AVAILABLE_COMMANDS.append("Look Around")
        return

    # outcome strings
    successStrings = ["Your axe strikes true and fells the tree.",
                      "Your mighty swing connects with perfect accuracy, causing the tree to come crashing down.",
                      "The force behind your axe blow is unyielding, resulting in the tree being brought down swiftly and effectively.",
                      "With a single precise strike, the tree is no match for your and falls to the ground.",
                      "The sound of your axe meeting its target echoes through the forest as the tree succumbs to your powerful blow.",
                      "In one swift motion, your axe cuts through the air and brings the towering tree to the ground, proving your strength and precision."]
    progressSounds = ["*Thump*","*Thud*","*Thwack*","*Crack*","*Chop*","*Smack*"]
    progressString = "Your axe connects with the tree..."
    failureStrings = ["The swing of your axe failed to connect with the tree.",
                      "Unfortunately, your aim was off, and your axe didn't hit the tree.",
                      "You just couldn't quite hit the mark with your axe on that tree.",
                      "Miss"]
    
    # check for success or fail (10% chance to miss)
    hitResult = np.random.randint(0,10)
    isSuccessful = (hitResult > 0)

    # the hit was good
    if (isSuccessful):
        # We were successful so remove health from the tree
        TREE_HEALTH -= 1
        # if the tree is dead
        if (TREE_HEALTH <= 0):
            # choose a random success string
            n = len(successStrings)
            c = np.random.randint(0, n)
            s = successStrings[c]
            # choose a random amount of wood gained
            woodGain = np.random.randint(5,10+1)
            INV_WOOD += woodGain
            s += " (+"
            s += str(woodGain)
            s += " wood)"
            # output
            PrintResponse(s)
        # if the tree is still alive after the hit
        else:
            # choose a random progress sound
            n = len(progressSounds)
            c = np.random.randint(0,n)
            s = progressSounds[c]
            PrintResponse(s + " " + progressString)
    # we missed
    else:
        # choose a random failure string
        n = len(failureStrings)
        c = np.random.randint(0,n)
        s = failureStrings[c]
        PrintResponse(s)


def C_Help():
    global AVAILABLE_COMMANDS
    # combine the commands into an output string
    s = ""
    for gc in AVAILABLE_COMMANDS:
        s += gc + "\n"
    PrintResponse(s)


# Output Functions
#////////////////////////////

def PrintResponse(text):
    prInfo(text)


if __name__ == '__main__':
    main()