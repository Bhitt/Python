# import the library numpy for randomly generating numbers
import numpy

# initialize variables for monster health and hero health
monsterHealth = 100
heroHealth = 100
print("***************************")

# loop while the monster health and hero health are above 0
while (monsterHealth > 0 and heroHealth > 0):
    # get a random amount of damage from 5 to 12
    damage = numpy.random.randint(5,13)
    # get a random number 0 or 1 to determine who is hit
    hitHero = numpy.random.randint(0,2)
    
    # hit the hero if the value is 0, otherwise hit the monster
    if (hitHero == 0):
        print("The Monster takes " + str(damage) + " damage!")
        monsterHealth -= damage # subtract the damage from the health
        print("Monster Health: "+str(monsterHealth))
    else:
        print("The Hero takes " + str(damage) + " damage!")
        heroHealth -= damage # subtract the damage from the health
        print("Hero Health: "+str(heroHealth))

# looping is over, output the results
print("***************************")
print("The battle is over...")
print("Monster Health: "+str(monsterHealth))
print("Hero Health: "+str(heroHealth))
if (heroHealth > monsterHealth):
    print("The Hero Wins!!!!")
else:
    print("The Monster Wins!!!")