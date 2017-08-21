from math import *

def largest_palindrome():
	for i in range(999,100,-1):
		for j in range(999,100,-1):
			if (list(str(j*i)) == list(str(j*i))[::-1]):
				print i*j
				break
		


largest_palindrome()