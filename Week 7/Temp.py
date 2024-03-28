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
        #Update()

        # check for user input (1 action per loop)
        prCyan("-------------")
        keepPlaying = ProcessCommands()

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