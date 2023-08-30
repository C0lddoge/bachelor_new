import numpy as np
import matplotlib.pyplot as plt
import os

rhos = np.array([0.02,0.05,0.1,0.3])
rhos2 = np.array([0.02,0.05,0.1,0.3])/2
lit = [0.161,0.162,0.156,0.138]
damps = [500,700,1000]

x = np.linspace(0.2,0.0,100)
for damp in damps:
    me = np.loadtxt(f'diff_coeff_damp{damp}dt.dat')
    plt.errorbar(rhos,me[:,1],yerr = me[:,2],marker = 'x',label = f'me; damp = {damp}dt',linestyle = 'none')
    plt.xlabel('rho')
    plt.ylabel('D')
#plt.ylim(0.0,1.0)

#plt.errorbar(0.02,np.loadtxt('diff_coeff_damp10.0.dat')[1],yerr = np.loadtxt('diff_coeff_damp10.0.dat')[2],marker = 'x',label = f'me; damp = 10.0',linestyle = 'none')
plt.errorbar(rhos,lit/rhos2,yerr = lit/rhos2*0.08 ,marker = 'o',linestyle = 'none',label = 'lit', markersize = 4.0)
plt.legend()
plt.show()
#plt.plot(rhos,lit, 'o')
#plt.savefig('diffs.pdf')

