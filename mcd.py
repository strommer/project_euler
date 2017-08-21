from math import *
from time import *
from prime import *
from factors import *
import re

start = clock()
nuggets = (6,9,20)


def ways (target , coin ):
	if coin <= 1:
		return 1
	res = 0
	while target >= 0:
		res = res + ways ( target , coin -1 )
		target = target - nuggets [coin -1]
	return res

print ways (9,3)


print clock() - start
