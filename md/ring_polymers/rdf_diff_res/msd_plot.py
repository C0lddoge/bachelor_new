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
data_dir = './MSDs_mr/'
expo_dir = './export_rp/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name(N,L,types):
    return 'RP_N{:},{:}_L{:}_newpot_MSDs_{:}_err.dat'.format(N[0],N[1],L,types)
def return_name_nvt(N,L,types):
    return 'RP_N{:},{:}_L{:}_NVT_MSDs_{:}_err.dat'.format(N[0],N[1],L,types)
def return_name_mr(N,L,types):
    return 'MIXTURE_N1-{:}_N2-{:}_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-{:}-com.lammpstrj_MSDs_{:}_err.dat'.format(N[0],N[1],L,types)






# styles
default_style = {
  'linewidth': 1.5,
  'markersize': 2.5
}
labels = {
    '1' :'flexible',
    '2' : 'semiflexible'
        }

colors = {
   '1': 'crimson',
   '2': 'darkblue'}
shade_colors = {
    '1': 'crimson',
    '2': 'deepskyblue'

        }

# plotting
N = ['256','256']
types = ['1','2']
Rgs = [3.55,6.50]
Ls = ['108.6','80.0','63.5','55.47','50.4','46.78','44.03']
Ls2 = ['108.60','080.00','063.50','055.47','050.40','046.78','044.03']
#names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']

fig, ax = plt.subplots(4, 2,figsize = (14,17))
for nind,L in enumerate(Ls2):
  x,y = np.unravel_index(nind,(4,2))
  for ind,ty in enumerate(types):
      print(data_dir + return_name(N,L,ty))
      if os.path.exists(data_dir + return_name_mr(N,L,ty)):
        print('test')
        data = np.loadtxt(data_dir + return_name_mr(N,L,ty))
        data[:,1:] = data[:,1:]/Rgs[ind]**2
        err = data[:,3]
        std = data[:,2]
        #ax[x][y].errorbar(data[:,0],data[:,1], yerr = err, marker ='o',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'{labels[ty]} lgv', color = colors[ty])
        #ax[x][y].fill_between(data[:,0],data[:,1]-std,data[:,1]+std,color = shade_colors[ty],alpha = 0.6)
        print(data[:,0])
        ax[x][y].errorbar(data[:,0],data[:,1], yerr = err, marker ='x',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'{labels[ty]} mr', color = colors[ty])
      
 # ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  ax[x][y].set_title('$L = {:}; N_1 = {:}; N_2= {:};$'.format(L,int(N[0]),int(N[1])))
  ax[x][y].set_xlabel('frame')
  ax[x][y].set_ylabel('$MSD [\\sigma^2/R_g^2]$')
  ax[x][y].set_yscale('log')
  ax[x][y].set_xscale('log')
  #ax[x][y].legend(loc = 'best', fontsize = 13, handlelength = 0.8)
  ax[x][y].legend(loc = 'upper left')

fig.delaxes(ax[3][1])
fig.savefig(expo_dir + 'msd_log_mr.pdf')

exit()
