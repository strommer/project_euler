from math import *
from time import *
from prime import *



def collatz_chain(num):
	chain = [num]
	while (num != 1):
		if (num%2 == 0):
			num = num/2
			chain.append(num)
		else:
			num = 3*num +1
			chain.append(num)
	return len(chain)

large = 0
number = 0

for i in range(2,1000000):
	x = collatz_chain(i)
 	if (x > large):
 		large = x
 		number =i

print large , number
