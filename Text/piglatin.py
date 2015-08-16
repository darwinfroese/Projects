# Take a string and apply "pig latin" to it

# Pig Latin Rules
# 	1. Beginning with a consonant: move the cluster to the end and add "ay"
#	2. Beginning with a vowel: add "yay" to the end

vowels = ['a','e','i','o','u']

def consonant(str):
	for i in range(0,len(str)):
		if str[i].lower() in vowels:
			cluster = str[0:i]
			base = str[i:]
			print base + cluster + "ay"	
			break

def vowel(str):
	print str + "yay"


def main():
	str = raw_input("Please enter a string: ")
	while str != "exit":
		if str[0].lower() in vowels:
			vowel(str)
		else:
			consonant(str)
		str = raw_input("Please enter a string: ")


if __name__ == "__main__":
	main()