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
        self.sxlny = sum(self.xlny)
        self.lnxlny = [self.lnx[i]*self.lny[i] for i in range(self.n)]
        self.slnxlny = sum(self.lnxlny)
    def lin(self):
        a = ((self.n*self.sxy)-(self.sx*self.sy))/((self.n*self.sx2)-(self.sx)**2)
        b = ((self.sxy*self.sx)-(self.sy*self.sx2))/((self.sx**2)-(self.n*self.sx2))
        return f'{a}*x {"+" if b >= 0 else "-"} {abs(b)}'
    def graf_lin(self):
        ypnt = [resolva(self.lin(), i) for i in self.x]
        plt.plot(self.x, ypnt)
        #plt.title(self.lin())
        plt.ylabel('concentração de CO2 em ppm'); plt.xlabel('ano')
        plt.grid(); plt.show()
    def log(self):
        a = ((self.n*self.sylnx)-(self.slnx*self.sy))/((self.n*self.sln2x)-(self.slnx)**2)
        b = ((self.sylnx*self.slnx)-(self.sy*self.sln2x))/((self.slnx**2)-(self.n*self.sln2x))
        return f'{a}*ln(x) {"+" if b >= 0 else "-"} {abs(b)}'
    def graf_log(self):
        ypnt = [resolva(self.log(), i) for i in self.x]
        plt.plot(self.x, ypnt)
        #plt.title(self.log())
        plt.ylabel('concentração de CO2 em ppm'); plt.xlabel('ano')
        plt.grid(); plt.show()
    def exp(self):
        a = ((self.n*self.sxlny) - (self.sx*self.slny))/(self.n*self.sx2-(self.sx**2))
        b = ((self.sxlny*self.sx) - (self.slny*self.sx2))/((self.sx**2)-self.n*self.sx2)
        eb = exp(b)
        return f'{eb}*exp({a}*x)'
    def graf_exp(self):
        ypnt = [resolva(self.exp(), i) for i in self.x]
        plt.plot(self.x, ypnt)
        #plt.title(self.exp())
        plt.ylabel('concentração de CO2 em ppm'); plt.xlabel('ano')
        plt.grid(); plt.show()
    def pot(self):
        a = ((self.n*self.slnxlny)-(self.slnx*self.slny))/((self.n*self.sln2x)-(self.slnx**2))
        b = ((self.slnx*self.slnxlny)-(self.slny*self.sln2x))/((self.slnx**2)-self.n*self.sln2x)
        eb = exp(b)
        return f'{eb}*x^{a}'
    def graf_pot(self):
        ypnt = [resolva(self.pot(), i) for i in self.x]
        plt.plot(self.x, ypnt)
        #plt.title(self.pot())
        plt.ylabel('concentração de CO2 em ppm'); plt.xlabel('ano')
        plt.grid(); plt.show()
    def R2(self, função):
        gx = função()
        SQReg = 0
        SQTot = 0
        for i in range(self.n):
            SQReg += ((resolva(gx, self.x[i])-self.medy)**2)
            SQTot += ((self.y[i]-self.medy)**2)
        return float(SQReg/SQTot)
