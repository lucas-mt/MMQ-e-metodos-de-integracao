from math import exp, log
from funções import *
import matplotlib.pyplot as plt

class MMQ:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(self.x)
        self.medy = sum(self.y)/len(self.y)
        self.xy = [self.x[i]*self.y[i] for i in range(len(self.x))]
        self.x2 = [i**2 for i in self.x]
        self.sx = sum(self.x)
        self.sy = sum(self.y)
        self.sxy = sum(self.xy)
        self.sx2 = sum(self.x2)
        self.lnx = [log(i) for i in self.x]
        self.slnx = sum(self.lnx)
        self.ylnx = [self.y[i]*self.lnx[i] for i in range(self.n)]
        self.sylnx = sum(self.ylnx)
        self.ln2x = [i**2 for i in self.lnx]
        self.sln2x = sum(self.ln2x)
        self.lny = [log(i) for i in self.y]
        self.xlny = [self.x[i]*self.lny[i] for i in range(self.n)]
        self.slny = sum(self.lny)
        self.medlny = self.slny/self.n
        self.sxlny = sum(self.xlny)
        self.lnxlny = [self.lnx[i]*self.lny[i] for i in range(self.n)]
        self.slnxlny = sum(self.lnxlny)
    def lin(self):
        a = float(((self.n*self.sxy)-(self.sx*self.sy))/((self.n*self.sx2)-(self.sx)**2))
        b = float(((self.sxy*self.sx)-(self.sy*self.sx2))/((self.sx**2)-(self.n*self.sx2)))
        g1 = f'{a}*x {"+" if b >= 0 else "-"} {abs(b)}'
        SQReg = 0
        SQTot = 0
        for i in range(self.n):
            SQReg += ((resolva(g1, self.x[i])-self.medy)**2)
            SQTot += ((self.y[i]-self.medy)**2)
        return g1, float(SQReg/SQTot)
    def log(self):
        a = float(((self.n*self.sylnx)-(self.slnx*self.sy))/((self.n*self.sln2x)-(self.slnx)**2))
        b = float(((self.sylnx*self.slnx)-(self.sy*self.sln2x))/((self.slnx**2)-(self.n*self.sln2x)))
        g1 = f'{a}*ln(x) {"+" if b >= 0 else "-"} {abs(b)}'
        SQReg = 0
        SQTot = 0
        for i in range(self.n):
            SQReg += ((resolva(g1, self.x[i])-self.medy)**2)
            SQTot += ((self.y[i]-self.medy)**2)
        return g1, float(SQReg/SQTot)
    def exp(self):
        a = float(((self.n*self.sxlny) - (self.sx*self.slny))/(self.n*self.sx2-(self.sx**2)))
        b = float(((self.sxlny*self.sx) - (self.slny*self.sx2))/((self.sx**2)-self.n*self.sx2))
        g1 = f'{a}*x {"+" if b >= 0 else "-"} {abs(b)}'
        SQReg = 0
        SQTot = 0
        for i in range(self.n):
            SQReg += ((resolva(g1, self.x[i])-self.medlny)**2)
            SQTot += ((self.lny[i]-self.medlny)**2)
        eb = float(exp(b))
        return f'{eb}*exp({a}*x)', float(SQReg/SQTot)
    def pot(self):
        a = float(((self.n*self.slnxlny)-(self.slnx*self.slny))/((self.n*self.sln2x)-(self.slnx**2)))
        b = float(((self.slnx*self.slnxlny)-(self.slny*self.sln2x))/((self.slnx**2)-self.n*self.sln2x))
        g1 = f'{b} + x*{a}'
        SQReg = 0
        SQTot = 0
        for i in range(self.n):
            SQReg += ((resolva(g1, log(self.x[i]))-self.medlny)**2)
            SQTot += ((self.lny[i]-self.medlny)**2)
        eb = float(exp(b))
        return f'{eb}*x^{a}', float(SQReg/SQTot)
    def graf(self, função):
        ypnt = [resolva(função()[0], i) for i in self.x]
        plt.plot(self.x, ypnt)
        #plt.title(self.função())
        plt.ylabel('concentração de CO2 em ppm'); plt.xlabel('ano')
        plt.grid(); plt.show()
        