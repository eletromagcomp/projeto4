#%% Importando
import numpy as np
import matplotlib.pyplot as plt
import time
import sym

#%% Variáveis
def N(x=4):
    return x

def L(x=0.5):
    return x

def R(x=1):
    return x

#%% Integração
Campo = sym.simpson_malha(N(),L(),R())
Campo_hor = sym.simpson_malha_hor(N(),L(),R())

#%% Save Results
np.savetxt('campox.dat',Campo[:,:,0])
np.savetxt('campoy.dat',Campo[:,:,1])
np.savetxt('campoz.dat',Campo[:,:,2])

np.savetxt('campox_hor.dat',Campo[:,:,0])
np.savetxt('campoy_hor.dat',Campo[:,:,1])
np.savetxt('campoz_hor.dat',Campo[:,:,2])

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
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_streamplot.png', bbox_inches='tight')
plt.show()


fig_quiver, ax_quiver = plt.subplots()
fig_quiver.set_size_inches((10,10))
U = 10*Campo_z / np.sqrt(Campo_z**2 + Campo_x**2)
V = 10*Campo_x / np.sqrt(Campo_z**2 + Campo_x**2)
ax_quiver.quiver(X[::20,::20], Z[::20,::20], V[::20,::20], U[::20,::20], units='inches')
for n in range(0,limite_espiras):
    plt.plot(25, n*50/N(), 'bo')
    plt.plot(-25, n*50/N(), 'bo')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R'+str(R())+'_quiver.png', color='r', bbox_inches='tight')
plt.show()

#%% Plot
x = np.arange(-125,125)
y = np.arange(-125,125)

X, Y = np.meshgrid(x, y)

Campo_hor_x = np.transpose(Campo_hor[:,:,0])
Campo_hor_y = np.transpose(Campo_hor[:,:,1])

# if momentâneo só pro Kirby plotar os troços dele (N = 1)
limite_espiras = 1 if N()==1 else int(N()+1)

fig, ax = plt.subplots()
fig.set_size_inches((10,10))
strm = ax.streamplot(x, y, Campo_hor_x, Campo_hor_y, color='r', linewidth=2, cmap='autumn')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_streamplot_hor.png', bbox_inches='tight')
plt.show()


fig_quiver, ax_quiver = plt.subplots()
fig_quiver.set_size_inches((10,10))
U = Campo_hor_y
V = Campo_hor_x
ax_quiver.quiver(X[::20,::20], Y[::20,::20], V[::20,::20], U[::20,::20], units='inches')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_quiver_hor.png', color='r', bbox_inches='tight')
plt.show()