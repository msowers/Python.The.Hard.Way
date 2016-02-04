# setup argv
# from sys import argv
# setup argv
# script, filename = argv
# open file and give variable
# txt = open(filename)
# display name of file given
# print "Here's your file %r:" % filename
# display file contents
# print txt.read()
# display request for file name again
print "Type the filename :"
# display the desired prompt
file_again = raw_input("> ")
# variable name for file name
txt_again = open(file_again)
# display file contents again
print txt_again.read()
