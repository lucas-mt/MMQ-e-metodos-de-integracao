from funções import *

def At(função, lim_inf, lim_sup, pts):
    h = (lim_sup-lim_inf)/pts
    x = [lim_inf+(h*i) for i in range(pts+1)]
    y = [resolva(função, i) for i in x]
    soma = 0
    for i in range(len(y)-1):
        soma += (y[i]+y[i+1])
    return (h/2)*soma

fc = input('função: ')
linf = float(input('limite inferior: '))
lsup = float(input('limite superior: '))
n = mult(2)

print(At(fc, linf, lsup, n))
