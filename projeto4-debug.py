#%% Importando
import numpy as np
import matplotlib.pyplot as plt
import time
import sym

#%% Variáveis
def N(x=4):
    return x

def L(x=1):
    return x

def R(x=1):
    return x

#%% Integração   
start = time.time()
print(sym.simpson_malha.__doc__)
Campo = sym.simpson_malha(N(),L(),R())

print(sym.simpson_malha_hor.__doc__)
Campo_hor = sym.simpson_malha_hor(N(),L(),R())
end_integrar = time.time()

#%% Plot
x = np.arange(-125,125)
z = np.arange(-50,100)
X, Z = np.meshgrid(x, z)
limite_espiras = 1 if N()==1 else int(N()+1)

fig, ax = plt.subplots()
fig.set_size_inches((10,10))
strm = ax.streamplot(x,z,np.transpose(Campo[:,:,0]), np.transpose(Campo[:,:,2]), color='r', linewidth=2, cmap='autumn')
for n in range(0,limite_espiras):
    plt.plot(25, n*50/N(), 'bo')
    plt.plot(-25, n*50/N(), 'bo')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_streamplot.png', bbox_inches='tight')
plt.show()
    
fig_quiver, ax_quiver = plt.subplots()
fig_quiver.set_size_inches((10,10))
#Plot do quiver normalizado
U = 10*np.transpose(Campo[:,:,2]) / np.sqrt(np.transpose(Campo[:,:,2])**2 + np.transpose(Campo[:,:,0])**2)
V = 10*np.transpose(Campo[:,:,0]) / np.sqrt(np.transpose(Campo[:,:,2])**2 + np.transpose(Campo[:,:,0])**2)
ax_quiver.quiver(X[::20,::20], Z[::20,::20], V[::20,::20], U[::20,::20], units='inches')
for n in range(0,limite_espiras):
    plt.plot(25, n*50/N(), 'bo')
    plt.plot(-25, n*50/N(), 'bo')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_quiver.png', color='r', bbox_inches='tight')
plt.show()

#%% Plot Horizontal
y = np.arange(-125,125)
X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()
fig.set_size_inches((10,10))
strm = ax.streamplot(x, y, np.transpose(Campo_hor[:,:,0]), np.transpose(Campo_hor[:,:,1]), color='r', linewidth=2, cmap='autumn')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_streamplot_hor.png', bbox_inches='tight')
plt.show()

fig_quiver, ax_quiver = plt.subplots()
fig_quiver.set_size_inches((10,10))
ax_quiver.quiver(X[::20,::20], Y[::20,::20], np.transpose(Campo_hor[:,:,0])[::20,::20], np.transpose(Campo_hor[:,:,1])[::20,::20], units='inches')
plt.savefig('N='+str(limite_espiras)+'_L='+str(L())+'_R='+str(R())+'_quiver_hor.png', color='r', bbox_inches='tight')
plt.show()

end_plot = time.time()

#%% Tempo
print('Tempo para integrar: '+str(end_integrar-start))
print('Tempo para plotar: '+str(end_plot-end_integrar))
print('Tempo total: '+str(end_plot-start))
