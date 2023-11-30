#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os

# plt settings
plt.style.use('bmh')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 20,
    "axes.titlesize": 20,
    "axes.labelsize": 20,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
	})

# paths
data_dir = './data/'
expo_dir = './export/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name_mc(N1,N2,dens,types):
    return 'RP_N{:},{:}_rho{:}_rdf_{:}{:}_mc.dat'.format(N1,N2,dens,*types)

def return_name_md(N1, N2, L,types):
    return 'SP_N{:},{:}_L{:}_newpot_rdf_{:}{:}.dat'.format(N1,N2,L,*types)
def return_name_mr(N1,N2,L,types):
    return 'MIXTURE_N1-{:}_N2-{:}_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-{:}-rdf_{:}{:}.dat'.format(N1,N2,L,*types)



# plotting


default_style2 = {
  'marker': 'x',
  'markersize': 2.0,
  'alpha': 0.80,
}


colors2 = {
   '0': 'darkred',
   '1': 'steelblue',
  '00': 'darkred',
  '10': 'rebeccapurple',
  '11': 'steelblue',
}

# plotting


Ls = [12.69,12.38,11.95,11.69,11.35,10.86]
N = [400,112]
fig,axs = plt.subplots(1,1,figsize = (10,5))
for nind,L in enumerate(Ls):
  x,y = np.unravel_index(nind,(2,3))
  for c, comb in enumerate([[0,0]]):
      print(data_dir + return_name_md(N[0],N[1],L,comb))
      if os.path.exists(data_dir + return_name_md(N[0],N[1],L,comb)):
        print('test')
        rho = np.sum(N)/L**3
        data = np.loadtxt(data_dir + return_name_md(N[0],N[1],L,comb),delimiter =';')
        axs.errorbar(data[:,0], data[:,1],yerr = data[:,2],marker = 'x',linewidth = 1.5,elinewidth = 1.0, label = '$\\rho = {:.2f}$'.format(rho),markersize= 2.5)

  #ax[x][y].set_title('$\\rho_0^* = {:.2f}; \\rho_1^* = {:.2f}; N_0 = {:}; N_1 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
  #axs.set_title('$ L = {:} \ \\sigma; N_1 = {:}; N_2 = {:};$'.format(L,int(N[0]),int(N[1])))
  axs.set_xlim(-0.1,6.0)
  axs.set_ylim(-0.05,3.3)
  axs.set_xlabel('$r[\\sigma]$')
  axs.set_ylabel('$g_{11}(r)$')
  axs.legend(loc = 'upper right', fontsize = 15, handlelength = 0.8, ncol = 2)


fig.savefig(expo_dir + 'gr.pdf')

exit()
