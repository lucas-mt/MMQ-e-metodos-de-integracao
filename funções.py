from sympy import *

x = symbols("x")

def f(função):
    return expand(função)

def resolva(função, num):
    return float(f(função).subs(x, num))

def mult(n):
    ask = int(input(f'partição: '))
    while ask%n!=0:
        ask = int(input(f'deve ser um valor múltiplo de {n}: '))
    return ask
    