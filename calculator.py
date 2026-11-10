# https://github.com/TheShmill/lab11-TH-AB
# Partner 1: Tyler Hartman
# Partner 2: Aiden Bascelli


import math

def square_root(a):
    if a < 0:
        raise ValueError("Cannot take square root of negative number")
    return math.sqrt(a)


def hypotenuse(a, b):
    return math.hypot(a, b)

def add(a, b): 
    return a + b
def subtract(a, b): 
    return a - b
def mul(a, b): 
    return a * b
def div(a, b): 
    if a == 0: 
        raise ZeroDivisionError
    return b / a  
def logarithm(a, b): 
    if a <= 0 or b <= 0 or b == 1: 
        raise ValueError
    return math.log(b, a)
    
def exp(a, b): 
    return a**b


