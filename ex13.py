from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

any_word = raw_input("Now you say anyword you would like to add: ")
another_word = raw_input("Now give me another word: ")

print "And I will cheer one more time:"

print "You went with", first
print "and also", second
print "but the best is", third
