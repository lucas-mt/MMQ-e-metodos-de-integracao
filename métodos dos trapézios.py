from funções import *

def At(função, a, b, n):
    soma, i = 0, 0
    listay = lst_y(a, b, n, função)
    h = (b-a)/n
    while i < n:
        soma = soma + (listay[i]+listay[i+1])
        i+=1
    return (h/2)*soma

fc = input('função> ')
a = float(input('limite inferior> '))
b = float(input('limite superior> '))
n = int(input('partições> '))

print(At(fc, a, b, n))
