#%% Importando
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import simps

import time
import util4 as u4

#%% Variáveis
def R():
    return 35.5

def L():
    return 40

def n_malha():
    return 100


#%% Campo Magnético

n = 100
phi = np.linspace(0,2*np.pi,n+1)
h = (2*np.pi-0)/n

def funcao_espira(phi,x=0,z=0,z_0=40):
    l = len(phi) if isinstance(phi, (list, tuple, np.ndarray)) else 1
    
    campo = np.zeros((3,l))
    
    x_c = (z-z_0)*np.cos(phi)
    y_c = (z-z_0)*np.sin(phi)
    z_c = R() + x*np.cos(phi)
    
    div = np.sqrt((x-R()*np.cos(phi))**2 + (-R()*np.sin(phi))**2 + (z-z_0)**2)**(3)
    
    campo[0,:] = x_c/div
    campo[1,:] = y_c/div
    campo[2,:] = z_c/div
         
    return campo
    
espiras = np.arange(-L()/2,L()/2+10,10)
campo = np.zeros((3, n_malha(), n_malha()))

x = np.arange(-n_malha()/2, n_malha()/2)
y = 0
z = np.arange(-n_malha()/2, n_malha()/2)

for i in range(n_malha()):
    for j in range(n_malha()):
        for k in range(len(espiras)):
            campo[:,i,j] += simps(funcao_espira(phi,x=x[i],z=z[i],z_0=espiras[k]), phi, dx=h)


#%%Plot
figure_stream, ax_stream = plt.subplots()
figure_stream.set_size_inches((7,7))
ax_stream.streamplot(z, x, campo[2,:,:], campo[0,:,:], color = 'black', arrowstyle='-', density = 1.5)
plt.show()
