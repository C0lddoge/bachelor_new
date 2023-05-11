import numpy as np 
import matplotlib.pyplot as plt

plt.figure(figsize = (6.4,6.4))
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
   

data_me = np.loadtxt('data_lj/energies.dat',delimiter = ';')
data_lit = np.loadtxt('data_lj/enerlit.dat',delimiter = ';')

E_me = data_me[:,2]
err_me = data_me[:,3]
print(err_me)

E_lit = data_lit[:,2]
err_lit = data_lit[:,3]


plt.plot(np.linspace(-2.5,0.2),np.linspace(-2.5,0.2), '--',color = 'black',linewidth = 1.5, label = "control line")

colors = ['indianred','gold','darkgreen','slateblue']
labels = ['$T^* = 1.4$ ; $ \\rho = 0.4 \ \\sigma^{-3}$', '$T^* = 1.8$ ; $ \\rho = 0.4 \ \\sigma^{-3}$','$T^* = 1.4$ ; $ \\rho = 0.7 \ \\sigma^{-3}$','$T^* = 1.8$ ; $ \\rho = 0.7 \ \\sigma^{-3}$']

for i in range(4):
    plt.errorbar(E_me[i],E_lit[i],marker = 'x', markersize = 10.0,linewidth = 0.0,xerr = err_me[i], yerr= err_lit[i], elinewidth = 1.3 , color = colors[i],label = labels[i])


plt.legend()
#plt.errorbar(E_me,E_lit,marker = 'x',markersize = 2.5,linewidth = 0.0,xerr = err_me, yerr= err_lit, elinewidth = 1.0)
plt.xlabel('$E_{MC} \ [\\epsilon]$')
plt.ylabel('$E_{MD} \ [\\epsilon]$')
plt.savefig('comp.pdf')





