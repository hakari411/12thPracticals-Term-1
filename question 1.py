#Factorial of a number
from functools import lru_cache

@lru_cache(maxsize=300)
def factorial(n):
    if n == 0:
        return 1
    return n* factorial(n-1)

#Sum of the first n even numbers
def sum_first_even(n):
    return (n*(n+1))
