import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import AutoMinorLocator,LogLocator,NullFormatter


plt.style.use("bmh")
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 13,
    "axes.titlesize": 13,
    "axes.labelsize":13,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": "#ffffff",
    "figure.autolayout": True,
    })









def name_gen(N,L,rc):
    return 'RP_N{:},{:}_L{:}_M100,25_k0,30_clust_rc{:}_CG.dat'.format(N[0],N[1],L,rc)

def name_gen_mr(N,L,rc):
    return 'RP_N{:},{:}_L{:}_clust_rc{:}_MR.dat'.format(N[0],N[1],L,rc)


Rgs = {
        '50': {
                '00.0':3.55323,
                '30.0':6.5076,

            }

        }

def return_overlap(M ,Rg):
    return int(50)/(2*float(Rg))**3

def return_concentration(N, L = '097.21'):
    return int(N)*50/float(L)**3



data_dir = 'cluster_data_M100,25_k0,30/'
export_dir = 'export_rp_newpot/'
Ns = [[500,500],[666,666],[864,864]]
Ls = [99.99,58.48,43.68,41.98,41.61]
#Ls2 = ['108.60','097.21','080.00','063.50','055.47','050.40','046.78','044.03']
#xlim = [10,10,10,512,512,512,512,512]
rcs = [4.5]
widths = 0.3
#fig,axs = plt.subplots(len(Ls),len(rcs), figsize = (500,250),squeeze = False)
#axs[1][1].set_visible(False)
for nind,N in enumerate(Ns):
    for lind,L in enumerate(Ls):
        for rcind,rc in enumerate(rcs):
            print(data_dir + name_gen(N,L,rc))
            if os.path.exists(data_dir + name_gen(N,L,rc)): 
                fig,axs = plt.subplots(figsize = (10,15))
                x,y = np.unravel_index(rcind,(4,2))
                print(data_dir + name_gen(N,L,rc))
                data = np.loadtxt(data_dir + name_gen(N,L,rc))
                axs.plot(data[:,0],data[:,1],label = 'CG')
                axs.set_xscale('log')
                axs.set_xlabel('clustersize',fontsize = 20)
                axs.set_ylabel('weight fraction',fontsize = 20)
                axs.legend()
                fig.suptitle('$N_1 = {:}; N_2 = {:} ; L = {:} \ \\sigma$ ; $\\rho = {:1.5f} \ \\sigma^{{-3}}$'.format(N[0],N[1],L,(N[0]+N[1])/L**3))
                fig.savefig(f'export_cluster_M100,25_k0,30/ratio_L{L}_N{N[0]},{N[1]}.pdf')
                fig.clf()
 





