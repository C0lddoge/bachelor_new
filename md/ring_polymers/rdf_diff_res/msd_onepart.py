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
    return 'RP_N{:},{:}_L{:}_newdamp_MSDs_{:}_err.dat'.format(N[0],N[1],L,types)
def return_name_nvt(N,L,types):
    return 'RP_N{:},{:}_L{:}_NVT_MSDs_{:}_err.dat'.format(N[0],N[1],L,types)
def return_name_mr(N,L,types):
    return 'MIXTURE_N1-{:}_N2-{:}_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-{:}-com.lammpstrj_MSDs_{:}_all.dat'.format(N[0],N[1],L,types)






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
types = ['2']
Rgs = [3.55,6.50]
partind=511
#Ls = ['108.6','80.0','63.5','55.47','50.4','46.78','44.03']
Ls2 = ['046.78']
#names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']

#fig, ax = plt.subplots(1, 1,figsize = (14,17))
for nind,L in enumerate(Ls2):
 # x,y = np.unravel_index(nind,(1,1))
  for ind,ty in enumerate(types):
      if os.path.exists(data_dir + return_name_mr(N,L,ty)):
        print('test')
        data = np.loadtxt(data_dir + return_name_mr(N,L,ty))
        print(np.shape(data))
        #ax[x][y].errorbar(data[:,0],data[:,1], yerr = err, marker ='o',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'{labels[ty]} lgv', color = colors[ty])
        #ax[x][y].fill_between(data[:,0],data[:,1]-std,data[:,1]+std,color = shade_colors[ty],alpha = 0.6)
        print(data[:,0])
        plt.plot(data[:,0],data[:,-1],marker ='x',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'{labels[ty]} mr', color = colors[ty])
      
 # ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  plt.title('$L = {:}; id = {:};$'.format(L,partind))
  plt.xlabel('frame')
  plt.ylabel('$MSD [\\sigma^2]$')
  plt.yscale('log')
  #plt.xscale('log')
  #ax[x][y].legend(loc = 'best', fontsize = 13, handlelength = 0.8)
  #plt.legend(loc = 'upper left')

plt.savefig(expo_dir + 'msd_partind{:}_{:}.pdf'.format(partind,Ls2[0]))

exit()
