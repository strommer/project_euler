from time import *
from math import *





def factors(num):
	factors_array = [1,]

	n = num
	for k in range(2,int(ceil(sqrt(num)))):
		if(n%k == 0):
			if(k not in factors_array):
				factors_array.append(k)
				factors_array.append(n/k)
			
	factors_array.append(num)
	return factors_array

print factors(28)
