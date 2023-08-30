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
    "axes.labelsize": 10,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
	})

# paths
data_dir = './diffcorr_data/'
expo_dir = './export_diffcorr/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name(N,L,types):
    return 'diffcorr_N{:},{:}_L{:}_partind{:}_CG.dat'.format(N[0],N[1],L,types)

def return_name_mr(N,L,types):
    return 'diffcorr_N{:},{:}_L{:}_partind{:}_MR.dat'.format(N[0],N[1],L,types)






# styles
default_style = {
  'linewidth': 1.0,
  'markersize': 2.5
}
labels = {
    '150' :'flexible',
    '350' : 'semiflexible'
        }

colors = {
   '150': 'crimson',
   '350': 'darkblue'}
shade_colors = {
    '150': 'crimson',
    '350': 'deepskyblue'

        }

# plotting
N = ['256','256']
partind = ['150','350']
Rgs = [3.55,6.50]
Ls = ['108.6','80.0','63.5','55.47','50.4','46.78','44.03']
Ls2 = ['108.60','080.00','063.50','055.47','050.40','046.78','044.03']
#names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']

for nind,L in enumerate(Ls):
  for ind,ty in enumerate(partind):
      print(data_dir + return_name(N,L,ty))
      if os.path.exists(data_dir + return_name_mr(N,Ls2[nind],ty)):
        print('test')
        data_mr = np.loadtxt(data_dir + return_name_mr(N,Ls2[nind],ty))
        data_cg = np.loadtxt(data_dir + return_name(N,L,ty))
        plt.plot(data_mr[:,0],data_mr[:,1],marker ='x',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'{labels[ty]} mr', color = colors[ty])
        plt.plot(data_cg[:,0],data_cg[:,1],marker ='v',linewidth = default_style["linewidth"], markersize = default_style["markersize"], label = f'{labels[ty]} cg', color = colors[ty])
      
 # ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  plt.title('$L = {:}; N_1 = {:}; N_2= {:};$'.format(L,int(N[0]),int(N[1])))
  plt.xlabel('lag frames')
  plt.ylabel('Diffcorr')
  #ax[x][y].legend(loc = 'best', fontsize = 13, handlelength = 0.8)
  plt.legend(loc = 'lower right',fontsize = 10)
  plt.savefig(expo_dir + 'diffcorr{:}.pdf'.format(L))
  plt.clf()

exit()
