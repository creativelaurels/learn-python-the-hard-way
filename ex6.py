
# the code below assigns a value to the varaiable string x and assigns %d to the value of 10
x = "There are %d types of people." % 10
binary = "binary" # this assigns the variable binary equal to the string text binary
do_not = "don't" # this assigns the varaiable do_not equal to the string text don't
# the code below assigns the varaiable y equal to a string text that will display the varaiables defined above as binary and don't
y = "Those who know %s and those who %s" % (binary, do_not)

# the code below will print two varaibles, x and then y
print x
print y

#the code below will print a string and print the varaiable x no matter what
print "I said: %r" % x

# the code below will print a string and the varaiable y
print "I also said: '%s'." % y

#the code below assigns two variables, one a boolean and one a string 
hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

# the code below will print out a string with the boolean of hilarious
print joke_evaluation % hilarious

# the code below assigns two string varaiables
w = "This is the left side of..."
e = "a string with a right side."

# the code below will print the variable string w followed in line by the string varaible e
print w + e
