from funções import *

def Riemann(fc, a, b, n):
    soma, i = 0, 0
    listax = lst_x(a, b, n)
    while i < n:
        soma = soma + (resolva(fc, listax[i])*(listax[i+1]-listax[i]))
        i+=1
    return soma

fc = input('função> ')
a, b = float(input('limite inferior> ')), float(input('limite superior> '))
n = int(input('partições> '))

print(Riemann(fc, a, b, n))
