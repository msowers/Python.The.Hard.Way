# Variables

name = 'Matthew Sowers'
age = 37 # not a lie
height = (5 * 12 + 11) * 2.54 # centimeters
weight = 420 * 2.20462262 # kilograms
eyes = 'Green'
teeth = 'White'
hair = 'Brown'

# Output
print "Let's talk about %s." % name
print "He's %d centimeters tall." % height
print "He's %d kilograms heavy." % weight
print "Actually that's pretty heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d, I get %d." % (age, height, weight, age + height + weight)
