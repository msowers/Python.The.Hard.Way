def number_of_games(games_installed, games_not_installed):
    print " I have %d games installed" % games_installed
    print "I have %d games not installed" % games_not_installed
    print " I have %d total games" % (games_installed + games_not_installed)

print "Giving numbers directly"
number_of_games(112, 108)

print "Giving variables from a script"
amount_installed = 112
amount_not_installed = 108

number_of_games(amount_installed, amount_not_installed)

print "Math inside!"
number_of_games(100 + 12, 100 + 8)

print "Or with variables and math"
number_of_games(amount_installed - 10 + 10, amount_not_installed - 10 + 10)
