from __future__ import print_function

def fib2(n): # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)    # see below
        a, b = b, a+b
    return result

fibresultFromFile = fib2(fib)
print(fibresultFromFile)
print('')

#this is to make it dirrty
