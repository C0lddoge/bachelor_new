import numpy as np
import matplotlib.pyplot as plt
import codemodule as cm

plt.style.use('bmh')
plt.rcParams.update({
       "text.usetex": True,
       "font.family": "sans-serif",
       "font.size": 15,
       "axes.titlesize": 15,
       "axes.labelsize": 15,
       "font.sans-serif": ["Helvetica"],
       "axes.facecolor": '#ffffff',
       "figure.autolayout": True,
  })  



data = np.loadtxt('ener.dat',delimiter = ';')
data = cm.equilibrate(data,0.022)
print(len(data))
ks = np.arange(2,100)
plot = []
N = len(data[:,1])
for i in ks:
    Nb = int(N/i)
    plot.append(cm.bin_ana(data,Nb))
plt.plot(ks,np.array(plot),'.',markersize = 3.0)
plt.xlabel('$k$')
plt.ylabel('$ \\sigma^2$')
plt.savefig('bin_ana.pdf')



