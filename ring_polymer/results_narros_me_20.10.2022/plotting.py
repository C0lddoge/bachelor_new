import numpy as np
import matplotlib.pyplot as plt


narros = [np.loadtxt('dens_0.85.csv',delimiter = ',',skiprows = 1),np.loadtxt('dens_2.10.csv',delimiter = ',',skiprows = 1),np.loadtxt('dens_3.40.csv',delimiter = ',', skiprows = 1),np.loadtxt('dens_4.55.csv',delimiter = ',',skiprows = 1)]
me = [np.loadtxt('g_r[0, 0]_dens2.95e-04.dat',delimiter = ';')[:,:2],np.loadtxt('g_r[0, 0]_dens7.28e-04.dat',delimiter = ';')[:,:2],np.loadtxt('g_r[0, 0]_dens1.18e-03.dat',delimiter = ';')[:,:2],np.loadtxt('g_r[0, 0]_dens1.58e-03.dat',delimiter = ';')[:,:2]]

label = [0.85,2.10,3.40,4.55]
for i in range(4):
    print(narros[i][:,0])
    plt.plot(narros[i][:,0],narros[i][:,1], '.', label = f' narros: {label[i]}')
    plt.plot(me[i][:,0],me[i][:,1], label = f' konsti: {label[i]}')

plt.xlim(0,13)
plt.legend()
plt.show()

















