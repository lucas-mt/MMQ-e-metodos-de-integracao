from MMQ import *
from funções import *
from R2 import *

xsep, x = [], []
ysep, y = [], []

with open('dados.txt', 'r', encoding='utf-8') as arq:
    for i in arq.readlines():
        for j in range(len(i)):
            if 10 <= j <= 18:
                xsep.append(f'{i[j]}')
            if j>= 21 and i[j]!='\n':
                ysep.append(f'{i[j]}')
        x.append(float(''.join(xsep))); y.append(float(''.join(ysep)))
        xsep.clear(); ysep.clear()

print(MMQpot(x, y), '\n', R2(x, y, MMQpot))
