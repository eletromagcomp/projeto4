import numpy as np
from scipy.integrate import simps

class Simpson:    
    
    def __init__(self, Funcao, Discretizacao, Intervalo):
        self.n = self.Aviso(Discretizacao) if Discretizacao%2 else Discretizacao
        self.Intervalo = Intervalo
        self.h = (Intervalo[-1]-Intervalo[0])/self.n
        self.Coeficientes = np.ones(self.n)
        self.Funcao = Funcao
        self.Resultado = None
        self.Scipy = None
        
    def Aviso(self, Discretizacao):
        print('##### Você escolheu um número ímpar de intervalos (n).')
        print('##### O número n será modificado para n-1.')
        return Discretizacao-1
    
    def Integrar_Scipy(self):
        x = np.linspace(self.Intervalo[0],self.Intervalo[-1],self.n+1)
        self.Scipy = simps(self.Funcao(x), x, dx=self.h)
    
    def Criar_Coeficientes(self):
        self.Coeficientes = np.ones(self.n+1)*4
        self.Coeficientes[::2] = np.ones(int(self.n/2)+1)*2
        self.Coeficientes[0] = 1
        self.Coeficientes[-1] = 1
        
    def Integrar(self):
        self.Criar_Coeficientes()
        x = np.linspace(self.Intervalo[0],self.Intervalo[-1],self.n+1)
        self.Resultado = (self.h/3)*np.sum(self.Funcao(x)*self.Coeficientes)

# Teste
if 1:
    def func(x):
        return x**2
            
    S = Simpson(func, 101, (2,10))
    S.Integrar()
    S.Integrar_Scipy()
    print(S.Resultado)
    print(S.Scipy)