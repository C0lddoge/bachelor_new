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
    return 'RP_N{:},{:}_L{:}_clust_rc{:}.dat'.format(N[0],N[1],L,rc)

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



data_dir = 'cluster_data/'
export_dir = 'export_rp/'
Ns = [[256,256]]
Ls = [108.6,97.21,80.0,63.5,55.47,50.4,46.78,44.03]
Ls2 = ['108.60','097.21','080.00','063.50','055.47','050.40','046.78','044.03']
#xlim = [10,10,10,512,512,512,512,512]
rcs = [4.0,4.5,5.0,5.5,6.0,6.5,7.0]
widths = 0.3
fig,axs = plt.subplots(len(Ls),len(rcs), figsize = (500,250),squeeze = False)
#axs[1][1].set_visible(False)
for nind,N in enumerate(Ns):
    for lind,L in enumerate(Ls):
        fig,axs = plt.subplots(4,2,figsize = (10,15),squeeze = False)
        axs[3,1].set_visible(False)
        for rcind,rc in enumerate(rcs):
            x,y = np.unravel_index(rcind,(4,2))
            print(data_dir + name_gen(N,L,rc))
            if os.path.exists(data_dir + name_gen(N,L,rc)): 
            #r0 = return_concentration(N[0])/return_overlap(50,Rgs["50"]["00.0"])
            #r1 = return_concentration(N[1])/return_overlap(50,Rgs["50"]["30.0"])
                data = np.loadtxt(data_dir + name_gen(N,L,rc))
                data_mr = np.loadtxt(data_dir + name_gen_mr(N,Ls2[lind],rc))

                #x,y = np.unravel_index(nind,(2,2))
            #if ty == 'all':
             #   axs[x][y].bar(data[:,0]-widths/2,data[:,1],capsize = 1.5,width = widths, label = 'total cluster distribution')
              #  print(data[:,2])
               # axs[x][y].errorbar(data[:,0]-widths/2,data[:,1], yerr = data[:,2],linewidth = 0.0, elinewidth = 1.0, capsize = 0.0, color = 'black')
            #else:
             #   axs[x][y].bar(data[:,0]+widths/2,data[:,1],capsize = 1.5,width = widths, label = 'semiflexible cluster distribution')
              #  axs[x][y].errorbar(data[:,0]+widths/2,data[:,1], yerr = data[:,2],linewidth = 0.0, elinewidth = 1.0, capsize = 0.0, color = 'black')
                axs[x][y].plot(data[:,0],data[:,1],label = 'CG')
                axs[x][y].plot(data_mr[:,0],data_mr[:,1], label = 'MR')
                #axs[x][y].set_xlim(0,xlim[lind])
                axs[x][y].set_xscale('log')
                #axs[x][y].set_yscale('log')
            #axs[nind].set_yscale('log')
            #axs[nind].set_yticks([10**(-4),10**(-3),10**(-2),10**(-1),10**0])
            
            #axs[lind][rcind].set_xticks(data[:,0])
            #locmin = LogLocator(numticks =999, subs="auto")
            #axs[x][y].yaxis.set_minor_locator(locmin)
            #axs[x][y].set_ylim(10**(-3),10**0)
           # axs[x][y].yaxis.set_minor_formatter(NullFormatter())
            #axs[x][y].set_yticks([0.0,0.1,0.2,0.3,])
            axs[x][y].set_title('$r_c = {:} \ \\sigma$'.format(rc))
            axs[x][y].set_xlabel('clustersize',fontsize = 20)
            axs[x][y].set_ylabel('weight fraction',fontsize = 20)
            axs[x][y].legend()
 #           axs[lind][rcind].legend(fontsize = 15)
#            axs[lind][rcind].set_ylim(10**(-5),1.1*10**0)
        fig.suptitle('$L = {:} \ \\sigma$ ; $\\rho = {:1.5f} \ \\sigma^{{-3}}$'.format(L,(N[0]+N[1])/L**3))
        fig.savefig(f'export_cluster/ratio_L{L}.pdf')
        fig.clf()
 





