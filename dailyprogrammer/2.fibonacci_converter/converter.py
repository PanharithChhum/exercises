#challenge #282 found here 
# https://www.reddit.com/r/dailyprogrammer/comments/5196fi/20160905_challenge_282_easy_unusual_bases/

import sys
fibarr = []

#create list of fib numbers up to or equal to num
def fib(num):
	a, b = 0, 1
	fibarr.append(b)
	while True:
		a,b = b, a + b
		if b <= num:
			fibarr.append(b)
		else:
			break

#create list of fib numbers up to nth fib number
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

#conver num to base fibonacci
def num_to_fib(num):
	total = 0
	fib(num)
	result = ""
	for fib_num in reversed(fibarr):
		if fib_num + total <= num:
			total = total + fib_num
			result += '1'
		else:
			result += '0'
	print result

#convert base fibonacci to number
def fib_to_num(num):
	total = 0
	nthfib(len(str(num)))
	num_arr = map(int, str(num))
	for idx, val in enumerate(num_arr):
		if val == 1:
			total = total + fibarr[-(idx+1)]
	print total


num_to_fib(16)
num_to_fib(32)
num_to_fib(9024720)
fib_to_num(10)
fib_to_num(1)
fib_to_num(111111)
fib_to_num(100000)
fib_to_num(10110110100111001)