from MMQ import *
from funções import *

def R2(x, y, fc):
    n = len(x)
    g = fc(x, y)
    medy = sum(y)/len(y)
    SQReg = 0
    SQTot = 0
    for i in range(n):
        SQReg += ((resolva(g, x[i])-medy)**2)
        SQTot += ((y[i]-medy)**2)
    return float(SQReg/SQTot)
