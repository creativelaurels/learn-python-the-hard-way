print "Please enter the file name so we may open it..."

filename = raw_input()

print "Here is the contents of the file:"

x = open(filename)

print x.read()

print "Now I will close the file called %s" % filename
x.close()