from funções import *

class MetInt:
    def __init__(self, função, lim_inf, lim_sup, pts):
        self.fc = função
        self.linf = lim_inf
        self.lsup = lim_sup
        self.n = pts
        self.h = (self.lsup-self.linf)/self.n
        self.x = [self.linf+(self.h*i) for i in range(self.n+1)]
        self.y = [resolva(self.fc, i) for i in self.x]
    def trap(self):
        sm = 0
        for i in range(len(self.y)-1):
            sm += (self.y[i]+self.y[i+1])
        return (self.h/2)*sm
    def s13(self):
        #n deve ser divisível por 2
        aux1, aux2 = 0, 0
        for i in range(1, len(self.y)-1):
            if i%2==0:
                aux1+=self.y[i]
            else:
                aux2+=self.y[i]
        return (self.h/3)*(self.y[0] + 2*aux1 + 4*aux2 + self.y[-1])
    def s38(self):
        #n deve ser divisível por 3
        aux1, aux2 = 0, 0
        for i in range(1, len(self.y)-1):
            if i%3!=0:
                aux1 += self.y[i]
            else:
                aux2 += self.y[i]
        return (self.h*(3/8))*(self.y[0] + 3*aux1 + 2*aux2 + self.y[-1])
    def rmn(self):
        c = input('esquerda [e] ou direita[d]? ').strip().lower()
        if c=='e':
            sm = 0
            for i in range(len(self.y)-1):
                sm += self.y[i]
            return self.h*sm
        elif c=='d':
            sm = 0
            for i in range(1, len(self.y)):
                sm += self.y[i]
            return self.h*sm
