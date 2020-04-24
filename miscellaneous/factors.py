from time import *
from math import *
from prime import *

def factors(num):
	factors_array = [1,]

	n = num
	for k in range(2,int(ceil(sqrt(num)))+1):
		if(n%k == 0):
			if(k not in factors_array):
				factors_array.append(k)
			if(n/k not in factors_array):
				factors_array.append(n/k)
			
	return factors_array

def prime_factors(num):
	'''Does not include 1 in the start'''
	prime_factors_array = [1,]

	n = num
	for k in range(2,int(ceil(sqrt(num)))+1):
		if(n%k == 0):
			if(k not in prime_factors_array and isPrime(k)):
				prime_factors_array.append(k)
			if(n/k not in prime_factors_array and isPrime(n/k)):
				prime_factors_array.append(n/k)
			
	return prime_factors_array[1:]

def sum_of_factors(num):
	return sum(factors(num))
