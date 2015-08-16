# count the number of vowels in the text entered
# Bonus: Count the number of each vowel

vowels = ['a','e','i','o','u','y']
vowelcount = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0, 'y':0}

def print_count():
	total = 0
	for c in vowels:
		total += vowelcount[c]

	print "You have entered %d vowels." % total
	print """
	\ta: %d
	\te: %d
	\ti: %d
	\to: %d
	\tu: %d
	\ty: %d
	""" % (vowelcount['a'], vowelcount['e'], vowelcount['i'], vowelcount['o'], vowelcount['u'], vowelcount['y'])

def count_vowels(str):
	for c in str:
		if c in vowels:
			vowelcount[c] = vowelcount[c] + 1

def main():
	str = raw_input("Please enter a string: ")
	while str != "exit":
		count_vowels(str)
		print_count()
		str = raw_input("Please enter a string: ")


if __name__ == "__main__":
	main()