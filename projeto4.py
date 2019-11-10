#%% Importando
import numpy as np
import matplotlib.pyplot as plt
import time
import sym

#%% Variáveis
def N(x=1):
    return x

def L(x=10):
    return x

def R(x=5):
    return x

#%% Integração
Campo = sym.simpson_malha(N(),L(),R())

#%% Save Results
np.savetxt('campox.dat',Campo[:,:,0])
np.savetxt('campoy.dat',Campo[:,:,1])
np.savetxt('campoz.dat',Campo[:,:,2])

#Teste = np.genfromtxt('campox.dat')
#print(Teste[0,0])

#%% Plot

x = np.arange(-125,125)
z = np.arange(-50,100)

X, Z = np.meshgrid(x, z)

Campo_x = np.transpose(Campo[:,:,0])
Campo_z = np.transpose(Campo[:,:,2])

# if momentâneo só pro Kirby plotar os troços dele (N = 1)
limite_espiras = 1 if N()==1 else int(N()+1)

fig, ax = plt.subplots()
fig.set_size_inches((10,10))
strm = ax.streamplot(x,z,Campo_x, Campo_z, color='r', linewidth=2, cmap='autumn')
for n in range(0,limite_espiras):
    plt.plot(25, n*50/N(), 'bo')
    plt.plot(-25, n*50/N(), 'bo')
plt.savefig('N='+str(N())+'_L='+str(L())+'_R='+str(R())+'_streamplot.png', bbox_inches='tight')
plt.show()


fig_quiver, ax_quiver = plt.subplots()
fig_quiver.set_size_inches((10,10))
U = 10*Campo_z / np.sqrt(Campo_z**2 + Campo_x**2)
V = 10*Campo_x / np.sqrt(Campo_z**2 + Campo_x**2)
ax_quiver.quiver(X[::20,::20], Z[::20,::20], V[::20,::20], U[::20,::20], units='inches')
for n in range(0,limite_espiras):
    plt.plot(25, n*50/N(), 'bo')
    plt.plot(-25, n*50/N(), 'bo')
plt.savefig('N='+str(N())+'_L='+str(L())+'_R'+str(R())+'_quiver.png', color='r', bbox_inches='tight')
plt.show()