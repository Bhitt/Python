# initialize some variables that we randomly chose before looking at the story text
bodyPart = "Arm"
actionWord = "Run"
aFeeling = "Happy"
adjective = "Cold"
things = "Cube"
holiday = "Christmas"
bodyPart2 = "Leg"
things2 = "Sphere"
things3 = "Cylinder"
bodyPart3 = "Buttcheeks"
place = "Nebraska"
number = "2"
noun = "Bouncy Ball"
noun2 = "Fish"
noun3 = "Clay"
food = "Pizza"

# create a variable for the story title
# include some simple formatting using the '\n' escape character for new lines
storyTitle = "THE GRINCH GROWS A HEART\n ***************************** \n"
# create a variable for the story text
# use string concatenation to piece together the story text with the variables from above
storyText = "The Grinch put his [" + bodyPart + "] to his ear.\n And he did hear a sound rising over the snow.\n It started in low. Then it started to grow.\n"
storyText += "But the sound wasn't [" + aFeeling + "]! Why, this sound sounded glad!\n\n Every Who down in Whoville, the tall and the ["
storyText += adjective + "],\n Was singing without any [" + things + "] at all!\n He HADN'T stopped [" + holiday + "] from coming! IT CAME!\n Somehow or "
storyText += "other, it came just the same!\n\n And the Grinch, with his grinch-[" + bodyPart2 + "] ice-cold in the snow,\n Stood puzzling and puzzling: How "
storyText += "could it be so?\n It came without [" + things2 + "]! It came without tags!\n It came without packages, boxes, or [" + things3 + "]!\n\n"
storyText += "And he puzzled three hours, till his [" + bodyPart3 + "] was sore.\n Then the Grinch thought of something he hadn't before!\n"
storyText += "Maybe Christmas, he thought, doesn't come from a [" + place + "].\n Maybe Christmas...perhaps...means a little bit more!\n\n"
storyText += "And what happened then? Well...in Whoville they say,\n That the Grinch's small heart Grew [" + number + "] sizes that day!\n"
storyText += "And the minute his heart didn't feel quite so tight,\n He whizzed with his [" + noun + "] through the bright morning light,\n"
storyText += "And he brought back the toys! And the [" + noun2 +"] for the [" + noun3 + "]!\n And he, HE HIMSELF!\n The Grinch carved the roast [" + food +"]!"
storyText += "\n\n*************************************"

# output the story title and text
print(storyTitle)
print(storyText)