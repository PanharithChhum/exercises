MAX = 100
total = 10 #algorithm skips 2, 3, and 5 on line13
prime_numbers = []


def isprime(num):
	for m in prime_numbers:
		if(num % m == 0 and m != 1 and num != m):
			return False
	return True

for x in xrange(2, MAX):
	if( x % 2 == 0 or x % 3 == 0 or x % 5 == 0):
		continue
	if isprime(x) == True:
		prime_numbers.append(x)
		total = total + x
		print x

print total