import numpy as np
import matplotlib.pyplot as plt
import os
import matplotlib.ticker as ticker


plt.style.use("bmh")
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.titlesize": 12,
    "axes.labelsize":12,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": "#ffffff",
    "figure.autolayout": True,
    })









def name_gen(N,types,rho):
    return 'RP_N{:},{:}_T1.0_rho{:}_cluster_rc0.7_types_{:}.dat'.format(N[0],N[1],rho,types)



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



data_dir = 'data/'
export_dir = 'export'
Ns = [[128,256],[256,128],[256,256,256]]
rhos = [0.01875,0.01875,0.025]
types = ['00','11','all']
for ty in types:
    fig,axs = plt.subplots(1,len(Ns), figsize = (4*len(Ns),3))
    for nind,N in enumerate(Ns):
        if os.path.exists(data_dir + name_gen(N,ty,rhos[nind])):
            r0 = return_concentration(N[0])/return_overlap(50,Rgs["50"]["00.0"])
            r1 = return_concentration(N[1])/return_overlap(50,Rgs["50"]["30.0"])
            data = np.loadtxt(data_dir + name_gen(N,ty,rhos[nind]),delimiter = ';')
            print(data)
            axs[nind].bar(data[:,0],data[:,1],yerr = data[:,2], width = 0.5)
            #axs[nind].set_yscale('log')
            #axs[nind].set_yticks([10**(-4),10**(-3),10**(-2),10**(-1),10**0])
            axs[nind].set_xticks(data[:,0])
            axs[nind].set_title('$\\rho_0/\\rho_0^* = {:.4f}; \\rho_1/\\rho_1^* = {:.4f}; N_0 = {:}; N_1 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
            axs[nind].set_xlabel('cluster size',fontsize = 10.0)
            axs[nind].set_ylabel('clustering probability',fontsize = 10.0)
    fig.suptitle('clustering for type: {:}; $r_c = 0.7$'.format(ty),fontsize = 10)
    fig.savefig(export_dir + '/cluster_type_nonlog{:}.pdf'.format(ty))
    fig.clf()
 





