

highest_multiple = 1

numerator = 1536
denominator = 7836045

list_numerator = []
list_denominator = []

i = 1

while( i <= numerator):
	if numerator % i == 0:
		list_numerator.append(i)
	i = i + 1

j = 1

while ( j <= denominator):
	if denominator % j == 0:
		list_denominator.append(j)
	j = j + 1

for m in reversed(list_numerator):
	if m in list_denominator:
		numerator = numerator / m
		denominator = denominator / m
		break

print numerator
print denominator

