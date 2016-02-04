from sys import argv

script, filename = argv

txt1 = open(filename)

print txt1.read()

txt = raw_input("Do you want to read anything else?")

new_text = open(txt)

print new_text.read()
