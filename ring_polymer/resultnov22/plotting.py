import numpy as np
import matplotlib.pyplot as plt

mix00 = np.loadtxt('g_r[0, 0]_0.025_mix_0.5.dat',delimiter = ';')[:,:2]
mix10 = np.loadtxt('g_r[1, 0]_0.025_mix_0.5.dat',delimiter = ';')[:,:2]
mix11 = np.loadtxt('g_r[1, 1]_0.025_mix_0.5.dat',delimiter = ';')[:,:2]

flexi = np.loadtxt('g_r[0,0]_flexible.dat',delimiter = ';')[:,:2]
stiff = np.loadtxt('g_r_1.0stiff.dat',delimiter = ';')[:,:2]


fig,ax = plt.subplots(3)

ax[0].plot(mix00[:,0],mix00[:,1],'.',markersize = 3.0)
ax[0].set(xlabel = 'r[R0]', ylabel = 'g(r)00')
ax[1].plot(mix10[:,0],mix10[:,1],'.',markersize = 3.0)
ax[1].set(xlabel = 'r[R0]', ylabel = 'g(r)10')
ax[2].plot(mix11[:,0],mix11[:,1],'.',markersize = 3.0)

ax[2].set(xlabel = 'r[R0]', ylabel = 'g(r)11')

#plt.plot(mix00[:,0],mix00[:,1])
plt.savefig('mixture.pdf')
plt.clf()
plt.plot(flexi[:,0],flexi[:,1], '+', markersize = 3.0)
plt.savefig('flexi.pdf')
plt.clf()
plt.plot(stiff[:,0],stiff[:,1], '+', markersize = 3.0)
plt.savefig('stiff.pdf')
plt.clf()






