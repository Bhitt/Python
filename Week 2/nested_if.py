# boolean type variable initialized to True
isTired = True
# prompt for a name
name = input ("What is your name?:")

# test against the boolean variable
if (isTired):
    # inside the if-block, we can test with a nested if-block
    # test against the input name
    if(name == "Uncle B"):
        print("Go get some coffee!")
    # if the test above fails, we always execute the else block below
    else:
        print("Who is this imposter?")
else:
    print("Really, you aren't sleepy?")