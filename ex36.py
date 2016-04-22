def moon2():
	print "Your ship is so awesome and shiny."
	print "You go to climb back in but a scary moon monster hops out from the cabin!"
	print "Its yelling at you with words you don't understand!"
	print "\nWhat do you do?"
	print "Your choice of a, b, or c: "
	print "\ta) Offer it some %s. \n\tb) Run away! \n\tc) Try to fight it!" % snack
	
	moon_choice2 = raw_input("\t>>> ")
	
	if moon_choice2 == "a":
		print "\nThe scary moon monster is overwhelemed by your generousity."
		print "You become best friends forever."
		winner()
	if moon_choice2 == "b":
		print "\nYou cowardly run, but trip and rip your space suit on a rock. You lose your oxygen supply."
		dead()
	if moon_choice2 == "c":
		print "The moon monster overpowers you like, crazy easy, and you get smushed under his big feet."
		dead()
def moon():
	print "\nIt is cold, quiet and dusty on this moon!"
	print "But you look soo good in your space suit."
	print "You hear a noise come from a crater near by."
	print "\nWhat do you do?"
	print "Your choice of a, b, or c: "
	print "\ta) Bravely go investigate the sound. \n\tb) Toss your %s into it. \n\tc) Eat some %s." % (weapon, snack)

	moon_choice = raw_input("\t>>> ")
	
	if moon_choice == "a":
		print "\nYou find a little moon critter. It is rabid and latches on to your throat."
		dead()
	elif moon_choice == "b":
		print "\nThe crater gets blown apart, saving you from a rabid moon critter. You head towards your ship."
		moon2()
	else:
		print "\nThe %s are delicious. But the smell attracted a rabid moon critter from the crater." % snack
		print "It latches on to your throat."
		dead()
def valley2():
	print "\nGeorge shows you the way to the scary forest caves."
	print "A forest monster jumps out from the cave!"
	print "The monster screams \'I\'m gonna eat your friend, George, and then you are next!\'"
	print "The monster is coming for you!"
	print "\nWhat do you do?"
	print "Your choice of a, b, or c: "
	print "\ta) Use your %s on the monster! \n\tb) Run away! \n\tc) Try to feed the monster some %s!" % (weapon, snack)
    
	valley_choice2 = raw_input("\t>>> ")
	
	if valley_choice2 == "a":
		print "\nYou bravely over take the monster, saving George and his friend!"
		winner()
	elif valley_choice2 == "b":
		print "\nYou chicken! Now George and his friend are doomed!"
		loser()
	else:
		print "\nThe monster hates %s! He eats you, George and his friend!" % snack
		dead()
def valley():
	print "\nYou are surrounded by rather large trees."
	print "It is beautiful!"
	print "A chipmunk hops out and asks you if you if you can help him."
	print "\nWhat do you do?"
	print "Your choice of a, b, or c: "
	print "\ta) Tell the little guy, of course you will help him. \n\tb) Give the chipmunk some %s. \n\tc) Tell the chipmunk to get away, you're busy!" % snack
    
	valley_choice = raw_input("\t>>> ")
    
	if valley_choice == "a":
		print "\nThe chipmunk says his name is George."
		print "He hops on your shoulder and you head into the forest to help him find his captured friend."
		valley2()
	elif valley_choice == "b":
		print "\nThe chipmunk says %s are his favorite. He says to call him George." % snack
		print "He hops on your shoulder and you head into the forest to help him find his captured friend."
		valley2()
	else:
		print "\nYou stomp away from the chipmunk but trip over a log and land on your %s." % weapon
		dead()
def boa_level_2():
	print "You mash the panel of floor numbers."
	print "The elevator is taking you up..."
	print "It stops on the top floor."
	print "You step out and walk into a board meeting."
	print "What do you do?"
	print "Your choice of a, b, or c: "
	print "\ta) Get back in the elevator and leave \n\tb) Get out your laser pointer and show them how to do a PowerPoint like a pro! \n\tc) Eat some %s..." % snack
    
	boa_choice2 = raw_input("\t>>> ")
    
	if boa_choice2 == "a":
		print "\nThat is a pretty weak choice."
		loser()
	elif boa_choice2 == "b":
		print "\nYou wow them all and they give you a big bag of money!"
		winner()
	elif boa_choice2 == "c":
		print "\nIt tasted good but everyone is pretty unimpressed."
		loser()
	else:
		print "That's not an option, pay attention!"
def boa_level():
	print "\nYou walk in, and things seem okay but we both know they're not."
	print "The gentleman at the help desks asks to see some ID."
	print "What do you do?"
	print "Your choice of a, b, or c: "
	print "\ta) Show him your ID \n\tb) Laser point 'em \n\tc) Eat your snack"
	
	boa_choice = raw_input("\t>>> ")
	
	if boa_choice == "a":
		print "\nHe checks your ID, and you get in the elevator."
		boa_level_2()
	elif boa_choice == "b":
		print "\nHe screams!! The light has blinded him! You make a dash to the elevator!"
		boa_level_2()
	elif boa_choice == "c":
		print "\nYou ignore him and munch on your %s, but it gets caught in your throat and you die." % snack
		dead()
	else:
		print "That's not an option, pay attention!"
def dead():
	print "End of game cause you dead, but great job, %s!" % name
def loser():
	print "You lose, %s! Game Over." % name
def winner():
	print "You've proven your skill, all hail The Great Adventurer %s! Game Over." % name

#Start of game
print "*~*~Welcome to your adventure~*~* \nMay we have your name please?\n"
name = raw_input("\t>>> ")
	
if "shit" in name or "ass" in name or "fuck" in name:
	print "I think not!"
	exit(0)
elif "Shit" in name or "Ass" in name or "Fuck" in name:
	print "I think not!"
	exit(0)
else:
	print "\n\tGreetings %s!" % name

print """
Before you take off you will need to make 
some decision on what to bring along with you...
"""
print "%s, the first item you need to select is a weapon.\n\nHere is what we have:\n\n" % name
	
# Selecting Weapon
weapons = ['sword', 'laser pointer', 'hand grenade']
print "\t", weapons
print "\n\tWhat weapon would you like?\n\n"
weapon = raw_input("\t>>> ")

if "sword" in weapon:
	print "\nYou're a very traditional adventurer."
elif "laser pointer" in weapon:
	print "\nAre you hoping to battle cats today?"
elif "hand grenade" in weapon:
	print "\nGo big or go home, right?"
else:
	print "\nThat's not an option, pay attention!"
	
print "\nNow you need to select a snack for the road:\n\n" 

#Selecting Snack
snacks = ['peanuts', 'cheetos', 'grapes']
print "\t", snacks
print "\n\tWhat snack would you like?\n\n"
snack = raw_input("\t>>> ")

if "peanuts" in snack:
	print "\nA great source of protein and fat."
elif "cheetos" in snack:
	print "\nYou're not worried about getting orange cheese dust on you, right?"
elif "grapes" in snack:
	print "\nYou're a healthy one!"
else:
	print "\nThat's not an option, pay attention!"
	exit(0)
	
print "Brilliant, %s! \nWith a %s in one hand and %s in the other, you'll be a great success!" % (name, weapon, snack)

#Transporting To defined function "locations"
print "\nYou're now being transported to the appropriate location based on your choices..."
print "\n... One moment please..."

if weapon == "laser pointer":
	print "\n\t GROUND FLOOR - BANK OF AMERICA TOWER"
	boa_level()
elif weapon == "sword":
	print "\n\t THE VALLEY OF RATHER LARGE TREES"
	valley()
else:
	print "\n\t THE SURFACE OF THE MOON"
	moon()
