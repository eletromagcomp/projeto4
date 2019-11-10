import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import time

from mpl_toolkits.mplot3d import axes3d, Axes3D #<-- Note the capitalization! 

fig = plt.figure()

ax = Axes3D(fig)

def R():
    return 10
def L():
    return 10


#%% Plotagem 3D com o quiver
    
# Make the grid
x, y, z = np.meshgrid(np.arange(-5*R(), 5*R(), 2),
                      np.arange(-5*R(), 5*R(), 2),
                      np.arange(-L(), 2*L(), 2))

# Make the direction data for the arrows
u = np.sin(np.pi * x) * np.cos(np.pi * y) * np.cos(np.pi * z)
v = -np.cos(np.pi * x) * np.sin(np.pi * y) * np.cos(np.pi * z)
w = (np.sqrt(2.0 / 3.0) * np.cos(np.pi * x) * np.cos(np.pi * y) *
     np.sin(np.pi * z))

M = (u**2+v**2+w**2)**(1/2)

# Color by Módulo :)
c = (u**2+v**2+w**2)**(1/2)
# Flatten and normalize
c = (c.ravel() - c.min()) / c.ptp()
# Repeat for each body line and two head lines
c = np.concatenate((c, np.repeat(c, 2)))
# Colormap
c = plt.cm.hsv(c)

start = time.time()
ax.quiver(x, y, z, u, v, w, colors=c, length=0.2, normalize=True)
end = time.time()
plt.show()

tempo = end - start
print(tempo)

#%% Plotagem 2D lateral

#Precisa ser a mesma quantidade

fig, ax = plt.subplots()

Y, X = np.mgrid[-5*R():5*R():100j, -L():2*L():100j]

U = -2*np.sin(X)
V = 5*np.cos(X)

modulo = (U**2+V**2)**(1/2)

# Varying color along a streamline

strm = ax.streamplot(X, Y, U, V, color=modulo, linewidth=2, cmap='autumn')
fig.colorbar(strm.lines)
ax.set_title('Varying Color')
plt.show()

#%% Plotagem 2D superior

