# Newtons metode

import math
import numerisk_derivasjon

def newton(function, derivative, n, init):
    if isinstance(function, str):
        function_formula = function
        def function(x):
            return eval(function_formula)
    if isinstance(derivative, str):
        derivative_formula = derivative
        def derivative(x):
            return eval(derivative_formula)

    for k in range(1, n+1):
        init = init - float(function(init)) / derivative(init)

    return init

def newton2(function, derivative, precision, init):
    if isinstance(function, str):
        function_formula = function
        def function(x):
            return eval(function_formula)
    if isinstance(derivative, str):
        derivative_formula = derivative
        def derivative(x):
            return eval(derivative_formula)

    while True:
        init1 = init - float(function(init)) / derivative(init)
        if abs(init - init1) < 1.0 / (10 ** precision):
            break
        init = init1

    return round(init * (10 ** precision))/(10 ** precision)

numdev_precision = 5

def newton3(function, precision, init):
    def derivative(x):
        return numerisk_derivasjon.numdev(function, x, numdev_precision)
    return newton2(function, derivative, precision, init)

print newton('math.cos(x)-x', '-1 * math.sin(x) - 1', 10, 0.8)
print newton('x ** 2 - 2', '2 * x', 10, 1.5)

print newton2('math.cos(x)-x', '-1 * math.sin(x) - 1', 5, 0.8)
print newton2('x ** 2 - 2', '2 * x', 5, 1.5)

print newton3('math.cos(x)-x', 5, 0.8)
print newton3('x ** 2 - 2', 5, 1.5)
