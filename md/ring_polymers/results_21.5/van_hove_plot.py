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









def name_gen(N,L,lag,types):
    return 'RP_N{:},{:}_L{:}_vh_lag{:}_type{:}.dat'.format(N[0],N[1],L,lag,types)
def name_gen_mr(N,L,lag,types):
    return 'RP_N{:},{:}_L{:}_vh_lag{:}_type{:}_MR.dat'.format(N[0],N[1],L,lag,types)



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



data_dir = 'vanhove_data/'
Ns = [[256,256]]
Ls = [108.6,97.21,80.0,63.5,55.47,50.4,46.78,44.03]
Ls2 = ['108.60','097.21','080.00','063.50','055.47','050.40','046.78','044.03']
#xlim = [10,10,10,512,512,512,512,512]
lags= [1,5,10,20,50,100,200]
types = ['1','2','all']
colors = {1:'red',2:'mediumvioletred',5:'magenta',10:'darkgreen',20:'lime',50:'olivedrab',100:'dodgerblue',200:'midnightblue'}
tau_frame = 5
#axs[1][1].set_visible(False)
for nind,N in enumerate(Ns):
    for lind,L in enumerate(Ls):
        fig,axs = plt.subplots(2,2,figsize = (15,10),squeeze = False)
        axs[1,1].set_visible(False)
        for tyind,ty in enumerate(types):
            x,y = np.unravel_index(tyind,(2,2))
            for lagind,lag in enumerate(lags):
                if os.path.exists(data_dir + name_gen(N,L,lag,ty)): 
            #r0 = return_concentration(N[0])/return_overlap(50,Rgs["50"]["00.0"])
            #r1 = return_concentration(N[1])/return_overlap(50,Rgs["50"]["30.0"])
                    data = np.loadtxt(data_dir + name_gen(N,L,lag,ty))
                    #data_mr = np.loadtxt(data_dir + name_gen_mr(N,Ls2[lind],lag,ty))

                    axs[x][y].plot(data[::2,0],data[::2,1],label = 'CG; $\\tau_l = {:}$'.format(lag), color = colors[lag], linewidth = 1.5)
                    #axs[x][y].plot(data_mr[::2,0],data_mr[::2,1], label = 'MR; $\\tau_l = {:}$'.format(lag),color = colors[lag], marker = 'x', linewidth = 0.0, markersize = 1.5)
                #axs[x][y].set_xscale('log')
               # axs[x][y].set_yscale('log')
                axs[x][y].set_title('type - {:}'.format(ty))
                axs[x][y].set_xlabel('$r \ [\\sigma]$',fontsize = 20)
                axs[x][y].set_ylabel('$G_s(r,t)$',fontsize = 20)
                axs[x][y].set_xlim(0,150)
                axs[x][y].legend()
        fig.suptitle('$L = {:} \ \\sigma$ ; $\\rho = {:1.5f} \ \\sigma^{{-3}}$'.format(L,(N[0]+N[1])/L**3))
        fig.savefig(f'export_vanhove/vanhove_L{L}.pdf')
        fig.clf()
 





