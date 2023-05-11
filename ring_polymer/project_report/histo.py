import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import AutoMinorLocator


plt.style.use("bmh")
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 22,
    "axes.titlesize": 22,
    "axes.labelsize":22,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": "#ffffff",
    "figure.autolayout": True,
    })









def name_gen(N,types,rho):
    return 'RP_N{:},{:}_T1.0_rho{:}_cluster_rc2.0_types_{:}_v2.dat'.format(N[0],N[1],rho,types)



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



data_dir = 'data_rp/'
export_dir = 'export_rp/'
Ns = [[128,256],[256,128],[256,256,256]]
rhos = [0.01875,0.01875,0.025]
types = ['11','all']
widths = 0.3
fig,axs = plt.subplots(2,2, figsize = (15.5,10))
axs[1][1].set_visible(False)
for nind,N in enumerate(Ns):
    for ty in types:
        if os.path.exists(data_dir + name_gen(N,ty,rhos[nind])):
            r0 = return_concentration(N[0])/return_overlap(50,Rgs["50"]["00.0"])
            r1 = return_concentration(N[1])/return_overlap(50,Rgs["50"]["30.0"])
            data = np.loadtxt(data_dir + name_gen(N,ty,rhos[nind]),delimiter = ';')
            x,y = np.unravel_index(nind,(2,2))
            print(data)
            if ty == 'all':
                axs[x][y].bar(data[:,0]-widths/2,data[:,1],capsize = 1.5,width = widths, label = 'total cluster distribution')
                print(data[:,2])
                axs[x][y].errorbar(data[:,0]-widths/2,data[:,1], yerr = data[:,2],linewidth = 0.0, elinewidth = 1.0, capsize = 0.0, color = 'black')
            else:
                axs[x][y].bar(data[:,0]+widths/2,data[:,1],capsize = 1.5,width = widths, label = 'semiflexible cluster distribution')
                axs[x][y].errorbar(data[:,0]+widths/2,data[:,1], yerr = data[:,2],linewidth = 0.0, elinewidth = 1.0, capsize = 0.0, color = 'black')
            #axs[nind].set_yscale('log')
            #axs[nind].set_yticks([10**(-4),10**(-3),10**(-2),10**(-1),10**0])
            
    axs[x][y].set_xticks(data[:,0])
    #axs[x][y].set_yticks([10**(-4),10**(-3),10**(-2),10**(-1),10**(0)])
    axs[x][y].yaxis.set_minor_locator(AutoMinorLocator())
    axs[x][y].set_title('$\\rho_1/\\rho_1^* = {:.2f}; \\rho_2/\\rho_2^* = {:.2f}; N_1 = {:}; N_2 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
    axs[x][y].set_xlabel('rings per cluster',fontsize = 20)
    axs[x][y].set_ylabel('weight fraction',fontsize = 20)
    axs[x][y].legend(fontsize = 15)
    axs[x][y].set_ylim(10**(-5),1.1*10**0)
fig.savefig(export_dir + 'clusterhistslides.pdf'.format(ty))
fig.clf()
 





