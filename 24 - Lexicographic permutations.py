from math import *
from time import *
from prime import *
from factors import *


start = clock()

n = 9
count = 0
flag = 0
max1 = 999999

x = []


while True:
	diff = max1 - factorial(n)
	if diff > 0:
		max1 = diff
		count += 1
		while True:
			if count in x:
				count += 1
			else:
				break
	elif diff == 0:
		count += 1
		while True:
			if count in x:
				count += 1
			else:
				break
		x.append(count)
		break
	else:
		n -= 1
		x.append(count)
		count = 0

for i in range(10):
	if i not in x:
		x.append(i)

print x
y = [str(z) for z in x]
print "".join(y)

print clock() - start
