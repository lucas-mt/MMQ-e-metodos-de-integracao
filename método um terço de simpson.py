from funções import *

def It(função, lim_inf, lim_sup, pts):
    h = (lim_sup-lim_inf)/pts
    x = [lim_inf+(h*i) for i in range(pts+1)]
    y = [resolva(função, i) for i in x]
    aux1, aux2 = 0, 0
    for i in range(1, len(y)-1):
        if i%2==0:
            aux1+=y[i]
        else:
            aux2+=y[i]
    return (h/3)*(y[0] + 2*aux1 + 4*aux2 + y[-1])

fc = input('função: ')
linf = float(input('limite inferior: '))
lsup = float(input('limite superior: '))
n = mult(3)

print(It(fc, linf, lsup, n))
