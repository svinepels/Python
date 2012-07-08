# Trapes-metoden

import math

def floatrange(start, end, number_of_steps):
    # liste = []
    step = float(end - start) / number_of_steps
    k = 0
    while k <= number_of_steps:
        # liste.append(float(start + k * step))
        yield float(start + k * step)
        k += 1
    # return liste


def trapes(function_formula, a, b, n):
    def function(x):
        return eval(function_formula)
    h = float(b - a) / n
    summen = 0
    for x in floatrange(a + h, b - h, n - 2):
        summen += function(x)
    return h / 2 * ( function(a) + function(b) + 2 * summen )

##def midtpunkt(function_formula, a, b, n):
##    def function(x):
##        return eval(function_formula)
##    h =  float(b - a) / n
##    summen = 0
##    for x in floatrange(a, b, n):
##        summen +=
