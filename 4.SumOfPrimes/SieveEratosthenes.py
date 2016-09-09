import math

def eratosthenes(num):
	sum = 0
	isComposite = []
	upperBoundSQRT = int(math.sqrt(num))
	for indx in range(0, num):
		isComposite.append(False)
	for x in range(2, upperBoundSQRT):
		if(isComposite[x] == False):
			for k in range(x*x, num, x):
				isComposite[k] = True;
	for x in range(2, num):
		if(isComposite[x] == False):
			sum = sum + x
	return sum

print eratosthenes(2000000)

