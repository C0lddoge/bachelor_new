import numpy as np
import matplotlib.pyplot as plt


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


data_dir = './data_lj/'
export_dir = './export_lj/'


def name_me(dens,T):
    return 'LJ_N216_types_1_dens{:.2e}_T{:.2e}_prope_rdf_00.dat'.format(float(dens),float(T))

def name_ro(dens,T):
    return 'RDF_T{:}_dens_{:}.dat'.format(T,dens)


rhos = ['0.4','0.7']
Ts = ['1.4','1.8']


colors = ['indianred','gold','darkgreen','slateblue']
labels = ['$T^* = 1.4$ ; $ \\rho = 0.4 \ \\sigma^{-3}$', '$T^* = 1.8$ ; $ \\rho = 0.4 \ \\sigma^{-3}$','$T^* = 1.4$ ; $ \\rho = 0.7 \ \\sigma^{-3}$','$T^* = 1.8$ ; $ \\rho = 0.7 \ \\sigma^{-3}$']

#fig,axs = plt.subplots(2,figsize = (10,15))
counter = 0
for ind,t in enumerate(Ts):
    for rho in rhos:
        data = np.loadtxt(data_dir + name_me(rho,t),delimiter=';')
        plt.errorbar(data[:,0],data[:,1], yerr = data[:,2], marker = 'x', markersize = 3.0, linewidth = 0.0, elinewidth = 1.0,color = colors[counter])
        data = np.loadtxt(data_dir + name_ro(rho,t))
        plt.plot(data[:,0],data[:,1],alpha = 0.7,linewidth = 1.0, color = colors[counter],label = labels[counter])
        counter += 1
#    axs[ind].set_xlabel('$r[\\sigma]$')
 #   axs[ind].set_ylabel('$g(r)$')
  #  axs[ind].set_title('$T={:}$'.format(t))
   # axs[ind].legend(loc = 'upper right', fontsize = 17,handlelength = 0.8)
plt.xlabel('$r \ [\\sigma]$')
plt.ylabel('$g(r)$')
plt.legend(fontsize = 13)



plt.savefig(export_dir + 'lj_gr_comp.pdf')

