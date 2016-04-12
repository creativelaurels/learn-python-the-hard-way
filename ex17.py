# module <from> called on module <sys>
# to <import> the module <argv> (argument)

# module <from> called on <os.path> module
# to import the function <exists> 

from sys import argv
from os.path import exists

script, from_file, to_file = argv 
# ^ user needs to enter the script to run (this file)
# followed by the name of the file you want as file A to copy
# followed by the name of the file you want as file B to add file A to

print "Copying from %s to %s" % (from_file, to_file)
# this tells the user, hey I'm going to copy this file A into this other file B

# we could do these two on one line, how?
in_file = open(from_file) ; indata = in_file.read()
# this sets the variable "in_file" equal to opening the file A
# this sets the variable "indata" equal to reading File A

print "The input file is %d bytes long" % len(indata)
# this alerts the user to how many charcters (aka length) are in File A

print "Does the output file exist? %r" % exists(to_file)
# This will check if File B exists - it will return True or False
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input() #this asks for user to continue with this script

out_file = open(to_file, 'w') #variable "out_file" will open up File B in write mode ('w)
out_file.write(indata)
# the write function is called on the variable out_file
# so outfile (aka file B) will have indata(aka file A (read out above)) written on it
# This will OVERWRITE File B. Not append to.

print "Alright, all done."

out_file.close()
in_file.close()