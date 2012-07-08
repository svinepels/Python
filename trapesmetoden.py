# Trapes-metoden

def square(x):
    return x ** 2

def trapes(function, a, b, n):
    h = float(b - a) / n
    summen = 0
    for x in range(a + h, b, h):
        summen += function(x)
    return h / 2 * ( function(a) + function(b) + 2 *  summen )

print trapes(square, 0, 1, 8)
