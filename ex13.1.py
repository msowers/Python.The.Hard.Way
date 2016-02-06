from sys import argv

script, first, second, third = argv

<<<<<<< Updated upstream
print "Your script is called:" , script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

one = raw_input("How many examples? ")
two = raw_input("Which example are you on? ")
three = raw_input("How many more examples? ")

print "So you have completed %s examples, you on on the %s example, and you have %s examples left." % (one, two, three)
=======
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third
>>>>>>> Stashed changes
