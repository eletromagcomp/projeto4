#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 14:07:26 2019

@author: hiro
"""

#%% Importando
import numpy as np
import matplotlib.pyplot as plt
import time
#%% Variáveis
def R_sole():
    return 100

def L_sole():
    return 200

def malha_x():
    return 10*R_sole()

def malha_z():
    return 3*L_sole()

def n_sole():
    return 10

def N_sole():
    return n_sole()*L_sole()
#%%
    
R = R_sole() + 0.5
L = L_sole()
N = N_sole()

magnetic = np.zeros(malha_x, malha_z)

for i in range(malha_x()):
    for j in range(malha_z()):
        '''
        Simpson
        '''

        
