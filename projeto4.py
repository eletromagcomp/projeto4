#%% Importando
import numpy as np
import matplotlib.pyplot as plt
import time
#%% Variáveis

def R():
    return 10

def z_0():
    return 2


#%% Campo Magnético

def funcao_espira(phi,x):
    
    a = [np.sin(phi)]
    b = [x-R*np.cos(phi),0,z_0]
    
    return R*np.cross(a,b)/(np.sqrt(b.dot(b)))**3
