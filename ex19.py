# defines function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
# print amount of cheeses, depending on the values given
    print "You have %d cheeses!" % cheese_count
# print amount of cracked depending on the values given
    print "You have %d boxes of crackers!" % boxes_of_crackers
# print
    print "Man that's enough for a party"
# print
    print "Get a blanket.\n"
#print given values given in numbers
print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)
# print given in numbers from variables
print "OR, we can use variable from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)
# print given by may for function
print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)
# print given by both variables and math 
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
