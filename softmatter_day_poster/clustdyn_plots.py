#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os

# plt settings
plt.style.use('bmh')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 25,
    "axes.titlesize": 30,
    "axes.labelsize": 30,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
	})

# paths


def return_name(N1, N2, L,size,types):
    return 'RP{:},{:}_L{:}_insize{:}_ty{:}.dat'.format(N1,N2,L,size,types)


# constants, concentrations etc
Rgs = {
	# size and stiffness
	'50': {
		'00.0': 3.5532,
		'30.0': 6.5076,
	}
}
unit_length = Rgs['50']['00.0']

def return_overlap(M, Rg):
  return int(M) / (2 * float(Rg))**3

def return_concentration(N, L = '097.21'):
  return int(N)*50 / float(L)**3


data_dir = './clust_dyn/'

# styles
default_style = {
  'linewidth': 1.0,
}

colors1 = {
  '2': 'magenta',
  '5': '#cb08cf',
}
colors2 = {
  '2' : 'dodgerblue',
  '5' : 'mediumblue'
}
N = [256,256]
Ls = ['046.78','055.47','080.00']
#titles = ['low density']

for Lind,L in enumerate(Ls):
    fig,ax=plt.subplots(figsize=(10,7))
    for sind,size in enumerate([2,5]):
        name1= data_dir + return_name(N[0],N[1],L,size,1)
        name2= data_dir + return_name(N[0],N[1],L,size,2)
        if os.path.isfile(name1) and os.path.isfile(name2):
            data1 = np.loadtxt(name1)
            data2= np.loadtxt(name2)
            ax.errorbar(data1[:,0]*50,data1[:,1],yerr=data1[:,2],color=colors1['{:}'.format(size)],marker= 'v', linestyle = 'solid',markersize = 4.0,linewidth = 2.5,label = '$ 1 \ \ | \ \ {:}$'.format(size))
            ax.errorbar(data2[:,0]*50,data2[:,1],yerr = data2[:,2],color=colors2['{:}'.format(size)],marker = 'x',markersize = 4.0, linestyle = 'solid',linewidth = 2.5,label = '$ 2 \ \ | \ \ {:}$'.format(size))
            ax.set_xlabel('$\\mathrm{lag \ time} \ [\\tau]$')
            ax.set_xscale('log')
            ax.set_xticks((50,100,500,1000,5000))
            #ax.set_xticklabels(('$5 \\times 10^1$','$10^2$','$5 \\times 10^2$','$10^3$','$5 \\times 10^3$'))
            ax.set_xticklabels(('$50$','$100$','$500$','$1000$','$5000$'))
            ax.set_xlim(30,10**4)
            ax.set_ylim(0.0,1.0)
            ax.set_ylabel('$\\mathrm{memory \ function}$')
    plt.legend(handlelength = 0.4, title = '$ \ \ \ \\mathrm{type} \ | \ \\mathrm{s}$')
    phieff = (N[0]*(2*Rgs['50']['00.0'])**2+N[0]*(2*Rgs['50']['30.0'])**2)/float(L)**3
#    plt.suptitle(titles[Lind] + '; $\\mathbf{{\\phi_{{eff}}}}$ = {:.2f}'.format(phieff))
    plt.savefig('survival_L{:}.pdf'.format(L))
        


# plotting
exit()
