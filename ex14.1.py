from sys import argv

script, first_name, last_name = argv
input = '> '

print "Hi, %s %s, I'm the %s script." %(first_name, last_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % first_name
likes = raw_input(input)

print "Where do you live Mr. %s?" % last_name
lives = raw_input(input)

print "What kind of computer do you have?"
computer = raw_input(input)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)
