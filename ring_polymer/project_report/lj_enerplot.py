import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import (MultipleLocator,AutoMinorLocator)


export_dir = 'export_lj/'
plt.rcParams.update({ 
       "text.usetex": True, 
       "font.family": "sans-serif", 
       "font.size": 15, 
       "axes.titlesize": 15, 
       "axes.labelsize":15, 
       "font.sans-serif": ["Helvetica"], 
       "axes.facecolor": "#ffffff", 
       "figure.autolayout": True, 
      })

data_me = np.loadtxt('data_lj/energies.dat',delimiter = ';')
todict = []
for i in range(np.shape(data_me)[0]):
    todict.append(('{:},{:}'.format(data_me[i,0],data_me[i,1]),[data_me[i,2],data_me[i,3]]))
data_dict_me = dict(todict)


data_lit = np.loadtxt('data_lj/energies.dat',delimiter = ';')
todict = []
for i in range(np.shape(data_me)[0]):
    todict.append(('{:},{:}'.format(data_me[i,0],data_me[i,1]),[data_me[i,2],data_me[i,3]]))
data_dict_lit = dict(todict)


data = {'MC-code': data_dict_me, 'MD': data_dict_lit}

params = ['0.4,1.4','0.4,1.8','0.7,1.4','0.7,1.8']
methods = ['MC-code','MD']

fig,axs = plt.subplots(2,2,figsize = (8,8))

for ind,param in enumerate(params):
    xind,yind= np.unravel_index(ind,(2,2))
    toplot = []
    toerr = []
    x = [2,4]
    for method in methods:
        toplot.append(data[method][param][0])
        toerr.append(data[method][param][1])
    axs[xind][yind].set_xticks(x,methods)
    if toplot[0] < 0:
        axs[xind][yind].invert_yaxis()
        #axs[xind][yind].set_ylim(toplot[0]+0.1,toplot[0]-0.1)
        axs[xind][yind].bar(x,toplot[0],yerr = toerr , capsize = 2.5,width = 1.0, color = ['royalblue','crimson'])
    else:
        axs[xind][yind].bar(x,toplot[0],yerr = toerr , capsize = 2.5,width = 1.0, color = ['royalblue','crimson'])
        #axs[xind][yind].set_ylim(toplot[0]-0.1,toplot[0]+0.1)

    axs[xind][yind].set_title('$ \\rho = {:} ; T^* = {:}$'.format(param.split(',')[0],param.split(',')[1]))
    axs[xind][yind].set_xlim(0,6)
    axs[xind][yind].yaxis.set_minor_locator(AutoMinorLocator())
fig.tight_layout()
plt.savefig(export_dir+'energies.pdf')



