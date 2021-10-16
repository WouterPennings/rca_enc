from math import sqrt
from itertools import count, islice

def isCoprime(x, y):
    return gcd(x, y) == 1

# Credit: https://www.w3resource.com/python-exercises/basic/python-basic-1-exercise-119.php
def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p

# Credit: https://stackoverflow.com/a/27946768
def isPrime(n):
    return n > 1 and all(n % i for i in islice(count(2), int(sqrt(n) - 1)))

# ToDO: Do not want to implement power functions, but math does some stupid rounding or something
def pow(number, n):
    result = number
    for _ in range(n - 1):
        result = result * number
    return result
