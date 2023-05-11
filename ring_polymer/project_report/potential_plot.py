import matplotlib.pyplot as plt
import numpy as np


plt.style.use('bmh')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 20,
    "axes.titlesize": 20,
    "axes.labelsize": 10,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
        })

def name_gen(K1,K2):
    return 'vEff_M1-50_M2-50_K1-{:}_K2-{:}.dat'.format(K1,K2)


type_dict = {'11': ['00','00'],'21':['00','30'],'22':['30','30']}
colors = ['blue','darkmagenta','red']
keys = ['11','21','22']
labels = ['flexible-flexible','flexible-semiflexible','semiflexible-semiflexible']
direc = 'potentials/'
export_dir = 'export_rp/'
for ind,key in enumerate(keys):
    data = np.loadtxt(direc + name_gen(type_dict[key][0],type_dict[key][1]))
    plt.errorbar(data[:,0],data[:,1],yerr = data[:,2],marker = 'x',markersize = 2.0, linewidth = 1.0, elinewidth = 1.0,label = labels[ind],color =colors[ind])

plt.xlabel('$r/R_f^0$',fontsize = 25)
plt.ylabel('$U_{ij}(r) \ [k_b T]$',fontsize = 25)
plt.legend()
plt.savefig(export_dir + 'potentials2.pdf')



