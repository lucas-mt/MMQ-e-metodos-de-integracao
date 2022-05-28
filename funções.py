from sympy import *

x = symbols("x")

def f(função):
    return expand(função)

def resolva(função, num):
    return f(função).subs(x, num)

def lst_x(a, b, n):
    i = a
    h = (b-a)/n
    pnt_x = []
    while i <= b:
        pnt_x.append(i)
        i += h
    return pnt_x

def lst_y(a, b, n, função):
    pnt_y = []
    lista_x = lst_x(a, b, n)
    for i in lista_x:
        pnt_y.append(resolva(função, i))
    return pnt_y
