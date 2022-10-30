import matplotlib.pyplot as plt
import numpy as np

mT1_4_dens04 = np.loadtxt('mineT1.4_dens_0.4.dat', delimiter = ';')

mT1_8_dens04 = np.loadtxt('mineT1.8_dens_0.4.dat', delimiter = ';')

mT1_4_dens07 = np.loadtxt('mineT1.4_dens_0.7.dat', delimiter = ';')

mT1_8_dens07 = np.loadtxt('mineT1.8_dens_0.7.dat', delimiter = ';')

roT1_4_dens04 = np.loadtxt('RDF_T1.4_dens_0.4.dat', skiprows = 1)

roT1_8_dens04 = np.loadtxt('RDF_T1.8_dens_0.4.dat', skiprows = 1)

roT1_4_dens07 = np.loadtxt('RDF_T1.4_dens_0.7.dat', skiprows = 1)

roT1_8_dens07 = np.loadtxt('RDF_T1.8_dens_0.7.dat', skiprows = 1)

fig,axs = plt.subplots(2,1)
axs[0].plot(mT1_4_dens04[:,0],mT1_4_dens04[:,1],'ko', markersize = 2, label = 'm_dens 0.4',markerfacecolor = 'none')
axs[0].plot(mT1_4_dens07[:,0],mT1_4_dens07[:,1],'k+', markersize = 2.5,label = 'm_dens 0.7',markerfacecolor = 'none')
axs[0].plot(roT1_4_dens04[:,0],roT1_4_dens04[:,1], 'b--',label = 'Ro_dens 0.4',linewidth = 0.7)
axs[0].plot(roT1_4_dens07[:,0],roT1_4_dens07[:,1], 'r--',label = 'Ro_dens 0.7',linewidth = 0.7)
axs[0].title.set_text('T = 1.4')
axs[0].legend()

axs[1].title.set_text('T = 1.8')
axs[1].plot(mT1_8_dens04[:,0],mT1_8_dens04[:,1], 'ko',markersize = 2,label = 'm_dens 0.4',markerfacecolor = 'none')
axs[1].plot(mT1_8_dens07[:,0],mT1_8_dens07[:,1], 'k+',markersize = 2.5, label = 'm_dens 0.7',markerfacecolor = 'none')
axs[1].plot(roT1_8_dens04[:,0],roT1_8_dens04[:,1], 'b--',label = 'Ro_dens 0.4',linewidth = 0.7)
axs[1].plot(roT1_8_dens07[:,0],roT1_8_dens07[:,1], 'r--',label = 'Ro_dens 0.7', linewidth = 0.7)
plt.show()
