from sys import argv

script, input_file = argv 
#asking user to enter the script (this file) and input file into the cmd line

def print_all(f):  # we are defining a function we call print_all that takes the parameter 'f'
	print f.read() # In this case, 'f' is a file. print_all will read all of the file

def rewind(f): # we have made a function called rewind with the parameter 'f'
	f.seek(0)  # seek - moves the "read head" (like on a dvd) to the start of the file ('0 bytes')
	# seek deals in bytes, not lines

def print_a_line(line_count, f): #creating a function print_a_line that takes two parameters
	print line_count, f.readline() #line_count and read the line on the file
						# readline - reading a line from a file and moving the
						# readhead to the right after the \n that ends that line

current_file = open(input_file) # defines current_file as opening the input file

print "First let's print the whole file:\n"

print_all(current_file) # this will print all of the opened input_file

print "Now let's rewind, kind of like a tape."

rewind(current_file) # this will move the readhead from the end of the line to the start of text(0)

print "Let's print three lines:"

current_line = 1						 # variable current_line is equal to 1
print_a_line(current_line, current_file) # this will call on the function defined above
# and move the read head to line '1', and print it from the opened input file

current_line = current_line + 1 # current line is redefined as 1 + 1
print_a_line(current_line, current_file) # will move readhead to line 2, and print

current_line = current_line + 1 # current line is redefined as the last varaible + 1 (so 3)
print_a_line(current_line, current_file)