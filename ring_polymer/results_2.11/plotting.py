import numpy as np
import matplotlib.pyplot as plt


narros = [np.loadtxt('dens_0.85.csv',delimiter = ',',skiprows = 1),np.loadtxt('dens_2.10.csv',delimiter = ',',skiprows = 1),np.loadtxt('dens_3.40.csv',delimiter = ',', skiprows = 1),np.loadtxt('dens_4.55.csv',delimiter = ',',skiprows = 1)]
me = [np.loadtxt('g_r[0, 0]_0.02125.dat',delimiter = ';')[:,:2],np.loadtxt('g_r[0, 0]_0.0525.dat',delimiter = ';')[:,:2],np.loadtxt('g_r[0, 0]_0.085.dat',delimiter = ';')[:,:2],np.loadtxt('g_r[0, 0]_0.11375.dat',delimiter = ';')[:,:2]]

label = [0.85,2.10,3.40,4.55]
color = ['r','b','g', 'c']
for i in range(4):
    print(narros[i][:,0])
    plt.plot(narros[i][:,0],narros[i][:,1], color[i] +'.', label = f' narros: {label[i]}')
    plt.plot(3.558*me[i][:,0],me[i][:,1],color[i] + '-', label = f' konsti: {label[i]}')

plt.xlabel('R/sig')
plt.ylabel('g(r)')
plt.legend()
plt.show()

















