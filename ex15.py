
# module from called on variable sys to module import the variable argument
from sys import argv
# this identifies what the user needs to input into the command line
# in this case it is the name of the python script to run (this file)
# followed by the input of the file name, which is the text file ex15_sample we just created
script, filename = argv

# this is assigning the variable txt to the function open
# open will execute on the filename given by user in the command line above ^
txt = open(filename)

# this will print the name of the file
print "Here's your file %r:" % filename
# this will call the function read() on the variable txt (aka the file you just opened)
# it will display the text in the file we made
print txt.read()

# this will as you to enter the name of the file again via your input
# compared to above which was done through the command line using argv
print "Type the filename again:"
# asking you to enter the name of the file >Enter after that symbol
file_again = raw_input(">")
# assigning the variable text again to the function open
# open with the paramters of whatever file name user just input
txt_again = open(file_again)
# will print out whatever file was just name above
print txt_again.read()