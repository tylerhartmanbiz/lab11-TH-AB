# https://github.com/TheShmill/lab11-TH-AB
# Partner 1: Tyler Hartman
# Partner 2: Aiden Bascelli


import math

def add(a, b): return a + b

def subtract(a, b): return a - b

def multiply(a, b): return a * b

def divide(a, b): 
    if a == 0: 
        raise ZeroDivisionError
    return b / a   # raise ZeroDivisionError if a == 0 

def logarithm(a, b): 
    if a <= 0 or b <= 0 or b == 1: raise ValueError
    return math.log(b, a)
    
def exponent(a, b): return a**b


