# Summering av en foelge over en liste indekser

import math

def summation(function, indices): #Summerer function over alle tall i indices
    if isinstance(function, str):
        function_formula = function
        def function(x):
            return eval(function_formula)
    result = 0
    for n in indices:
        result += function(n)
    return result

def primetest(k): #Avgjoer om k er et primtall eller ikke
    if k == 1:
        return False
    i = 2
    sqk = math.sqrt(k)
    while True:
        if i > sqk:
            return True
        if k % i == 0:
            return False
        i += 1

def primes(n): #Returnerer liste med alle primtall mindre enn eller lik n
    primelist = []
    for m in range(1, n+1):
        if primetest(m):
            primelist.append(m)
    return primelist
print primes(50)

def square(x):
    return x ** 2

def reciprocal(x):
    return 1.0 / x

##print summation(reciprocal, primes(10))
##print summation(reciprocal, primes(100))
##print summation(reciprocal, primes(1000))
##print summation(reciprocal, primes(10000))
##print summation(reciprocal, primes(100000))
##print summation(reciprocal, primes(1000000))
##print summation(reciprocal, primes(10000000))
##print summation(reciprocal, primes(100000000))
