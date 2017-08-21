from math import *
from time import *
 
def small_mul():
	i = 323
	flag = 0
	num = [5,7,9,11,13,16,17,19]

	while True:
		i += 323
		for j in num:
			if (i%j == 0):
				flag += 1
				if (flag == len(num)):
					print i
					break
			else:
				break
		if (flag == len(num)):
			break
		else:
			flag = 0

start = clock()
small_mul()
end = clock() - start
print end