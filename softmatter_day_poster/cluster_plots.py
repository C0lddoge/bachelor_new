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


def return_name_md(N1, N2, L,r_c):
    return 'RP_N{:},{:}_L{:}_clust_rc{:}_CG.dat'.format(N1,N2,L,r_c)
def return_name_mr(N1,N2,L,r_c):
    return 'RP_N{:},{:}_L{:}_clust_rc{:}_MR.dat'.format(N1,N2,L,r_c)


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


data_dir = './clusters_struc/'

# styles
default_style = {
  'linewidth': 1.0,
}

colors = {
  '00': 'magenta',
  '01': 'purple',
  '11': 'dodgerblue',
}
N = [256,256]
Ls = ['046.78','055.47','080.00']
r_c = 4.5
titles = ['high density', 'medium density', 'low density']

for Lind,L in enumerate(Ls):
    fig,ax=plt.subplots(figsize=(10,7))
    name_cg = data_dir + return_name_md(N[0],N[1],float(L),r_c)
    name_mr = data_dir + return_name_mr(N[0],N[1],L,r_c)
    data_cg = np.loadtxt(name_cg)
    data_mr = np.loadtxt(name_mr)
    print(data_mr-data_cg)
    ax.errorbar(data_mr[:,0],data_mr[:,1],yerr=data_mr[:,3],color='orangered',marker = 'v', markersize = 7.0,linestyle = 'solid',linewidth = 2.0,label = '$\\mathrm{MR}$')
    ax.errorbar(data_cg[:,0],data_cg[:,1],yerr = data_cg[:,3],color='indigo',marker = 'x',markersize = 7.0, linestyle = 'dashed',linewidth = 2.0,label = '$\\mathrm{CG}$')
    ax.set_xlabel('$\\mathrm{cluster \ size}$')
    ax.set_xscale('log')
    ax.set_yscale('log')
    ax.set_ylim(10**(-3),1)
    ax.set_xlim(1,10**2)
    ax.set_ylabel('$\\mathrm{probability \ density}$')
    plt.legend(loc='lower left')
    phieff = (N[0]*(2*Rgs['50']['00.0'])**2+N[0]*(2*Rgs['50']['30.0'])**2)/float(L)**3
    plt.savefig('cluster_structure_L{:}.pdf'.format(L))
        


# plotting
exit()
