from integrações import *

fc = input('função: ')
linf = float(input('limite inferior: '))
lsup = float(input('limite superior: '))
n = mult(1)

itg = MetInt(fc, linf, lsup, n)
