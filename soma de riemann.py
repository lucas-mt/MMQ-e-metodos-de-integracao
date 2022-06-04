from funções import *

def Sr(função, lim_inf, lim_sup, pts):
    h = (lim_sup-lim_inf)/pts
    x = [lim_inf+(h*i) for i in range(pts+1)]
    y = [resolva(função, i) for i in x]
    c = input('esquerda [e] ou direita[d]? ').strip().lower()
    if c=='e':
        soma = 0
        for i in range(len(y)-1):
            soma += y[i]
        return h*soma
    elif c=='d':
        soma = 0
        for i in range(1, len(y)):
            soma += y[i]
        return h*soma

fc = input('função: ')
linf = float(input('limite inferior: '))
lsup = float(input('limite superior: '))
n = int(input('partrição: '))

print(Sr(fc, linf, lsup, n))
