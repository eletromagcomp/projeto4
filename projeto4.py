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

#print(sym.simpson_malha.__doc__)

#x = np.arange(0,600, 1)
#z = np.arange(0,1000, 1)

Campo = sym.simpson_malha(N(),L(),R())

#%% Result
np.savetxt('campox.dat',Campo[:,:,0])
np.savetxt('campoy.dat',Campo[:,:,1])
np.savetxt('campoz.dat',Campo[:,:,2])

Teste = np.genfromtxt('campox.dat')

print(Teste[0,0])

#%% Plot

fig, ax = plt.subplots()

x = np.arange(-500,500)
z = np.arange(-200,400)

Campo_x = np.transpose(Campo[:,:,0])
Campo_z = np.transpose(Campo[:,:,2])

modulo = (Campo_x**2+Campo_z**2)**(1/2)


fig, ax = plt.subplots()
ax.streamplot(x,z,Campo_x, Campo_z, color=modulo, linewidth=2, cmap='autumn')
plt.grid()
#ax.set_aspect('equal')
plt.title('How to plot a vector in matplotlib ?',fontsize=10)
plt.savefig('how_to_plot_a_vector_in_matplotlib_fig3.png', bbox_inches='tight')
plt.show()
#plt.close()

#x = np.arange(-n_malha()/2, n_malha()/2)
#z = np.arange(-n_malha()/2, n_malha()/2)
X, Z = np.meshgrid(x, z)

fig_quiver, ax_quiver = plt.subplots()
U = 10*Campo_z / np.sqrt(Campo_z**2 + Campo_x**2)
V = 10*Campo_x / np.sqrt(Campo_z**2 + Campo_x**2)
ax_quiver.quiver(X[::40,::40], Z[::40,::40], V[::40,::40], U[::40,::40], pivot='mid', color='r', units='inches')
plt.show()