# Numerisk derivasjon

import math

def numdev(function, point, precision):
    if isinstance(function, str):
        function_formula = function
        def function(x):
            return eval(function_formula)

    return (function(point + 1.0 / (10 ** precision)) - function(point)) / (1.0 / (10 ** precision))
