from funções import *

def I(função, lim_inf, lim_sup, pts):
    h = (lim_sup-lim_inf)/pts
    x = [lim_inf+(h*i) for i in range(pts+1)]
    y = [resolva(função, i) for i in x]
    aux1, aux2 = 0, 0
    for i in range(1, len(y)-1):
        if i%3!=0:
            aux1 += y[i]
        else:
            aux2 += y[i]
    return (h*(3/8))*(y[0] + 3*aux1 + 2*aux2 + y[-1])

fc = input('função: ')
linf = float(input('limite inferior: '))
lsup = float(input('limite superior: '))
n = mult(3)

print(I(fc, linf, lsup, n))
