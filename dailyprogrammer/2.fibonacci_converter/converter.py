import sys
fibarr = []

def fib(num):
	a, b = 0, 1
	fibarr.append(b)
	while True:
		a,b = b, a + b
		if b < num:
			fibarr.append(b)
		else:
			break

def nthfib(num):
	a, b = 0, 1
	fibarr.append(b)
	length = 1
	while True:
		a,b = b, a + b
		if length == num:
			break
		else:
			fibarr.append(b)
			length = length + 1

def num_to_fib(num):
	total = 0
	fib(num)
	for fib_num in reversed(fibarr):
		if fib_num + total <= num:
			total = total + fib_num
			sys.stdout.write('1')
		else:
			sys.stdout.write('0')
	print '\n'

def fib_to_num(num):
	total = 0
	nthfib(len(str(num)))
	num_arr = map(int, str(num))
	for idx, val in enumerate(num_arr):
		if val == 1:
			total = total + fibarr[-(idx+1)]
	print total


def convert(base, num):
	if base == 10:
		num_to_fib(num)
	else:
		fib_to_num(num)

# convert(10,16)
# convert(10,32)
# convert(10,9024720)
convert(1,10)
convert(1,1)
convert(1,111111)
convert(1,100000)
convert(1,10110110100111001)