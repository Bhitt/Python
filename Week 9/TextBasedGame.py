# external libraries / modules
import numpy as np

#////////////////////////////
# GLOBAL VARIABLES
#////////////////////////////
HAS_AXE = False
HAS_PICKAXE = False
HAS_FISHINGPOLE = False
INV_WOOD = 0
INV_ROCK = 0
INV_LEAF = 0
INV_TWINE = 0

TREE_HEALTH = 5
ROCK_HEALTH = 6
HAS_SMALLROCK = False
HAS_FIRE = False

AVAILABLE_COMMANDS = set(("Options","Exit","Harvest Wood"))
PREVIOUS_COMMAND = ""
DEV_COMMANDS = set(("skip to part 2", "error prevention"))

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
    UpdateRocks()
    
def UpdateTrees():
    # if the last tree was cut down, find a new tree with random health from 1 to 6
    global TREE_HEALTH
    if (TREE_HEALTH <= 0):
        TREE_HEALTH = np.random.randint(1,6+1)

def UpdateRocks():
    # if the last tree was cut down, find a new tree with random health from 1 to 6
    global ROCK_HEALTH
    if (ROCK_HEALTH <= 0):
        ROCK_HEALTH = np.random.randint(1,6+1)

def ProcessCommands():
    global AVAILABLE_COMMANDS
    global PREVIOUS_COMMAND
    global DEV_COMMANDS
    # get the command
    command = input("c~: ").lower()
    # check for repeat command
    if (command == "r"):
        command = PREVIOUS_COMMAND
    # check for dev command
    if (command == "dev"):
        AVAILABLE_COMMANDS.update(DEV_COMMANDS)
        return True
    # check if command is available
    if (command not in (c.lower() for c in AVAILABLE_COMMANDS)):
        PrintResponse("command: (" + command + ") not found. Type 'options' for a list of available commands")
        return True

        
    
    # check for valid commands
    if (command  == "options"):
        C_Options()
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
    elif (command == "count leaves"):
        C_CountLeaves()
    elif (command == "pick up rock"):
        C_PickUpRock()
    elif (command == "make pickaxe"):
        C_MakePickaxe()
    elif (command == "harvest rocks"):
        C_HarvestRocks()
    elif (command == "count twine"):
        C_CountTwine()
    elif (command == "count rocks"):
        C_CountRocks()
    elif (command == "make fire"):
        C_MakeFire ()

    # check for dev commands
    if (command == "skip to part 2"):
        C_SkipToPart2()
    # keep track of the command
    PREVIOUS_COMMAND = command

    # no exit command so keep playing
    return True

def C_LookAround():
    global AVAILABLE_COMMANDS
    if (not HAS_AXE):
        prInfo("Peering over your shoulder, you notice a rusty axe lodged in a stump.")
        AVAILABLE_COMMANDS.add("Pick up axe")
        return
    elif (not HAS_SMALLROCK):
        prInfo("You see a small rock, the only one small enough to pick up.")
        AVAILABLE_COMMANDS.add("Pick up rock")
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
        AVAILABLE_COMMANDS.add("Count Wood")
        AVAILABLE_COMMANDS.add("Count Leaves")
        AVAILABLE_COMMANDS.add("Count twine")

def C_CountWood():
    global INV_WOOD
    prInfo("I have " + str(INV_WOOD) + " wood.")
def C_CountLeaves():
    global INV_LEAF
    prInfo("I have " + str(INV_LEAF) + " leaves")

def C_HarvestWood():
    global AVAILABLE_COMMANDS
    global HAS_AXE
    global TREE_HEALTH
    global INV_WOOD
    global INV_LEAF
    global INV_TWINE
    # valiate the user has an axe first
    if (not HAS_AXE):
        prInfo("You attempt to harvest wood but do not yet have an axe...")
        prInfo("Perhaps you can [LOOK AROUND] for an axe to use.         ")
        AVAILABLE_COMMANDS.add("Look Around")
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
            leafGain = np.random.randint(50,1000 + 1)
            INV_LEAF += leafGain
            twineGain = np.random.randint(0, 2+1)
            INV_TWINE += twineGain
            s += " (+"
            s += str(woodGain)
            s += " wood)"
            s += " (+"
            s += str(leafGain)
            s += " leaves)"
            s += " (+"
            s += str(twineGain)
            s += " twine)"
            # output
            PrintResponse(s)
            AVAILABLE_COMMANDS.add("Make Fire")
        
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
def C_PickUpRock():
    global HAS_SMALLROCK
    if not HAS_SMALLROCK:
        HAS_SMALLROCK = True
        prInfo("You pick up the rock, maybe you could use it to make something.")
        AVAILABLE_COMMANDS.add("Make pickaxe")
    elif HAS_SMALLROCK:
        prInfo("You already have the small rock.")
        


def C_Options():
    global AVAILABLE_COMMANDS
    # combine the commands into an output string
    s = ""
    for gc in AVAILABLE_COMMANDS:
        s += gc + "\n"
    PrintResponse(s)


def C_MakePickaxe():
    global HAS_SMALLROCK
    global INV_WOOD
    global INV_TWINE
    global HAS_PICKAXE
    if HAS_PICKAXE:
        prInfo("You already have a pickaxe.")
    else:
        prInfo("This needs 1 wood, 1 rock, and 1 twine")
        prInfo("Type Y to create, type N to cancel")
        response = input("c~: ").lower()
        if (response == "y"):
            if ((INV_WOOD >= 1) and (INV_TWINE >= 1) and (HAS_SMALLROCK)):
                INV_TWINE -= 1; INV_WOOD -= 1; HAS_SMALLROCK = False
                prInfo("You now have a pickaxe")
                HAS_PICKAXE = True
                AVAILABLE_COMMANDS.add ("harvest rocks")
                AVAILABLE_COMMANDS.add ("count rocks")

            else:
                prInfo("You do not have enough matierals to make this")
                
def C_MakeFire():
    global HAS_FIRE
    global INV_WOOD
    global INV_ROCK
    global INV_LEAF
    if HAS_FIRE:
        prInfo("You already have a fire.")
    else:
        prInfo("This needs 6 wood, 6 rocks, and 30 leaves")
        prInfo("Type Y to create, type N to cancel.")
        response = input("c~: ").lower()
        if (response == "y"):
            if ((INV_WOOD >=6) and (INV_ROCK >=6) and (INV_LEAF >=30)):
                INV_WOOD -= 6; INV_ROCK -= 6; INV_LEAF -= 30
                prInfo("You now have a fire")
                HAS_FIRE = True 
                #add appends here
            else:
                prInfo("You do not have enough matierals to make this")



def C_HarvestRocks():
    global INV_ROCK
    global HAS_PICKAXE
    global ROCK_HEALTH
    # outcome strings
    successStrings = ["Your pickaxe strikes the rock and it crumbles to a pile of rocks.",
                      "Your mighty swing connects with perfect accuracy, causing the rock to crumble.",
                      "The force behind your blow is unyielding, as the rock explodes into a million pieces.",
                      "With a single precise strike, the rock is no match for you and turns to dust.",
                      "The sound of your pickaxe meeting its target echoes through the forest as the rock succumbs to your powerful blow.",
                      "In one swift motion, your pickaxe cuts through the air and breaks the boulder, proving your strength and precision."]
    progressSounds = ["*Thump*","*Thud*","*Crack*"]
    progressString = "Your pickaxe connects with the rock..."
    failureStrings = ["Your pickaxe glances off the top of the rock.",
                      "Unfortunately, your aim was off, and your pickaxe didn't hit the boulder.",
                      "You just couldn't quite hit the mark with your pickaxe on that boulder.",
                      "Miss"]
    
    # check for success or fail (10% chance to miss)
    hitResult = np.random.randint(0,10)
    isSuccessful = (hitResult > 0)

    # the hit was good
    if (isSuccessful):
        # We were successful so remove health from the tree
        ROCK_HEALTH -= 1
        # if the tree is dead
        if (ROCK_HEALTH <= 0):
            # choose a random success string
            n = len(successStrings)
            c = np.random.randint(0, n)
            s = successStrings[c]
            # choose a random amount of wood gained
            rockGain = np.random.randint(6,17+1)
            INV_ROCK += rockGain
            s += " (+"
            s += str(rockGain)
            s += " rocks)"
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


def C_CountTwine():
    global INV_TWINE
    prInfo("I have " + str(INV_TWINE) + " twine")

def C_CountRocks():
    global INV_ROCK
    prInfo("I have " + str(INV_ROCK) + " rocks")




























































































































def C_SkipToPart2():
    global HAS_AXE
    global HAS_PICKAXE
    global INV_WOOD
    global INV_ROCK
    global INV_LEAF
    global INV_TWINE
    global HAS_SMALLROCK
    global HAS_FIRE
    global AVAILABLE_COMMANDS
    HAS_AXE = True
    HAS_PICKAXE = True
    INV_WOOD = 100
    INV_ROCK = 50
    INV_LEAF = 1500
    INV_TWINE = 9
    HAS_SMALLROCK = False
    HAS_FIRE = True
    Part1Commands = set(("Look Around", "Pick Up Axe", "Count Wood", "Count Leaves", "Pick Up Rock", "Make Pickaxe", "Harvest Rocks", "Count Twine", "Count Rocks", "Make Fire"))
    AVAILABLE_COMMANDS.update(Part1Commands)


  


# Output Functions
#////////////////////////////

def PrintResponse(text):
    prInfo(text)


if __name__ == '__main__':
    main()