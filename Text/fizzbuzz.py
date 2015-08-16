# Write a program that prints the numbers from 1 to 100 with the following exceptions:
#		* For multiples of 3 print "fizz"
# 		* For multiples of 5 print "buzz"
# 		* For multiples of 3 and 5 print "fizzbuzz"

def fizz():
	print "fizz"

def buzz():
	print "buzz"

def fizzbuzz():
	print "fizzbuzz"

for i in range(1,101):
	if i % 3 == 0 and i % 5 == 0:
		fizzbuzz()
	elif i % 3 == 0:
		fizz()
	elif i % 5 == 0:
		buzz()
	else:
		print i