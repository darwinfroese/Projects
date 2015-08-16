# Reverse a string entered

str = raw_input("Please enter a string to reverse: ")

while str != "exit":
	print str[::-1]
	str = raw_input("Please enter a string to reverse: ")