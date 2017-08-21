from math import *
from time import *

def isPrime(num):
    if num<2:
            return False
    i = 0
    for factor in range(2, int(floor(sqrt(num)))+1):
        if num%factor == 0:
            return False  
    return True

def nthPrime(n):
    found = 0
    guess = 1
    while found < n:
        guess += 1
        if isPrime(guess):
            found += 1
    return guess
