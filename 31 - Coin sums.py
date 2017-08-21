from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()
coins = (1, 2, 5, 10, 20, 50, 100, 200)


def ways (target , coin ):
	if coin <= 1:
		return 1
	res = 0
	while target >= 0:
		res = res + ways ( target , coin -1 )
		target = target - coins [coin -1]
	return res

print ways (5000,8)


print clock() - start
