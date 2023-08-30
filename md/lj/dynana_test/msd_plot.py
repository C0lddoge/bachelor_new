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
data_dir = './msds/'
expo_dir = './export_rp/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name(rho):
    return 'LJ_N500_rho{:}_MSDs_1_err.dat'.format(rho)






# styles
default_style = {
  'linewidth': 1.5,
  'markersize': 1.5
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
rhos = ['0.02','0.05','0.1','0.3']
#names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']


for nind,rho in enumerate(rhos):
  #x,y = np.unravel_index(nind,(2,2))
  print(data_dir + return_name(rho))
  if os.path.exists(data_dir + return_name(rho)):
    data = np.loadtxt(data_dir + return_name(rho))
    data[:,1:] = data[:,1:]
    err = data[:,3]
    std = data[:,2]
    plt.errorbar(data[:,0],data[:,1], yerr = err, marker ='o',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'$\\rho = {rho}$')
    #plt.fill_between(data[:,0],data[:,1]-std,data[:,1]+std,color = shade_colors[ty],alpha = 0.6)
       
      
 # ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  #ax[x][y].set_title('$L = {:}; N_1 = {:}; N_2= {:};$'.format(L,int(N[0]),int(N[1])))
  #ax[x][y].set_xlabel('$time [\\tau]$')
  #ax[x][y].set_ylabel('$MSD [\\sigma^2/R_g^2]$')
  plt.xlabel('$ \\tau $')
  plt.ylabel('$MSD \ [\\sigma^2]$')
  plt.yscale('log')
  plt.xscale('log')
  #ax[x][y].legend(loc = 'best', fontsize = 13, handlelength = 0.8)
  plt.legend(loc = 'upper left')
plt.savefig('msd_log.pdf')

exit()
