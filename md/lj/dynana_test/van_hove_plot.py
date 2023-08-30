import numpy as np
import matplotlib.pyplot as plt
import os
from matplotlib.ticker import AutoMinorLocator,LogLocator,NullFormatter
import codemodule as cm


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









def name_gen(rho,lag,damp):
    return 'LJ_N500_rho{:}_vh_lag{:}_type1_damp{:}dt.dat'.format(rho,lag,damp)



Rgs = {
        '50': {
                '00.0':3.55323,
                '30.0':6.5076,

            }

        }





data_dir = 'vanhove_data/'
rhos = [0.02,0.05,0.1,0.3]
damps = [500,700,1000]
lags= [1,5,10,50,100,200]
times = np.array([1,5,10,50,100,200])*0.005*1000
colors = {1:'red',2:'magenta',3:'blue'}
tau_frame = 5
rs = np.linspace(0,150,500)
xlims = np.array([40,60,80,100,120,140])+20
#axs[1][1].set_visible(False)
for rhoind,rho in enumerate(rhos):
    fig,axs = plt.subplots(3,2,figsize = (10,20))
    for lagind,lag in enumerate(lags):
        x,y = np.unravel_index(lagind,(3,2))
        gauss = lambda r,D: np.exp(-r**2/(4*D*times[lagind]))/np.sqrt(4*np.pi*D*times[lagind])**3
        for dampind,damp in enumerate(damps):
            print(data_dir + name_gen(rho,lag,damp))
            if os.path.exists(data_dir + name_gen(rho,lag,damp)):
                data = np.loadtxt(data_dir + name_gen(rho,lag,damp))
                data[:,1] = data[:,1]/(4*np.pi*data[:,0]**2)
                popt,pcov = cm.gauss_fit(data,times[lagind])
                print(popt)
                #data[:,1] = data[:,1]/(4*np.pi*data[:,0]**2)
                axs[x][y].plot(data[::10,0],data[::10,1],marker = 'x',linestyle = 'none' , color = colors[dampind+1],label = '$d = {:} dt$'.format(damp), markersize = 2.0,alpha = 0.5)
                axs[x][y].plot(rs,gauss(rs,*popt),color = colors[dampind+1],label = '$D = {:.2f}$'.format(popt[0]),linewidth = 1.0)
                axs[x][y].set_yscale('log')
                axs[x][y].set_xlabel('$r \ [\\sigma]$',fontsize = 20)
                axs[x][y].set_ylabel('$G_s(r,t)$',fontsize = 20)
                axs[x][y].set_title('lag = {:}'.format(lag))
                axs[x][y].set_xlim(0,xlims[lagind])
            #    plt.xlim(0,3)
                axs[x][y].legend()
    fig.suptitle('$\\rho = {:} \ \\sigma^{{-3}}$'.format(rho))
    fig.savefig(f'export_vanhove/vanhove4pi_rho{rho}.pdf')
    plt.clf()
 





