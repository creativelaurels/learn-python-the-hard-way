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

snacks = ['peanuts', 'cheetos', 'grapes']

print "\t", snacks

print "\n\tWhat snack would you like?\n\n"

snack = raw_input("\t>>> ")

if "peanuts" in snack:
	print "\nA great source of protein and fat."
elif "cheetos" in snack:
	print "\nYou're not worried about getting orange cheese dust on you, right?"
elif "apple" in snack:
	print "\nYou're a healthy one!"
else:
	print "\nThat's not an option, pay attention!"
	
print "Brilliant, %s! \nWith a %s in one hand and %s in the other, you'll be a great success!" % (name, weapon, snack)

print "You're now being transported to the appropriate location based on your choices..."

print "... One moment please..."

if weapon == "laser pointer":
	print "\n\t GROUND FLOOR - BANK OF AMERICA TOWER"
elif weapon == "sword":
	print "\n\t THE VALLEY OF RATHER LARGE TREES"
elif snack == "cheetos":
	print "\n\t YOU'RE HIGH SCHOOL FRIEND'S BASEMENT"
else:
	print "\n\t THE SURFACE OF THE MOON"



