# check if a string is a palindrome

def palindrome(str1, str2):

	print "Is %s a palindrome of %s? %r" % (str2[::-1], str1, str2[::-1] == str1)

def main():
	str1 = raw_input("Please enter a string: ")

	while str1 != "exit":
		str2 = raw_input("Please enter a second string: ")
		palindrome(str1, str2)
		str1 = raw_input("Please enter a string: ")

if __name__ == "__main__":
	main()