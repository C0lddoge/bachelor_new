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


def return_name_md(N1, N2, L,types):
    return 'RP_N{:},{:}_L{:}_rdf_{:}{:}.dat'.format(N1,N2,L,*types)
def return_name_mr(N1,N2,L,types):
    return 'MIXTURE_N1-{:}_N2-{:}_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-{:}-rdf_{:}{:}.dat'.format(N1,N2,L,*types)


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


data_dir = './G_Rs/'

# styles
default_style = {
  'linewidth': 1.0,
}

colors1 = {
  '00': 'magenta',
  '01': 'rebeccapurple',
  '11': 'dodgerblue',
}
colors2 = {
  '00': '#cb08cf',
  '01': 'blueviolet',
  '11': 'steelblue',
}
N = [256,256]
Ls = ['046.78','055.47','080.00']
titles = ['high density', 'medium density', 'low density']

for Lind,L in enumerate(Ls):
    fig,ax=plt.subplots(figsize=(10,7))
    ax.plot(0,0,color = 'white',label = '$\\mathrm{MR}$')
    ax.errorbar(0,0,color = 'white',label = '$\\mathrm{CG}$')
    for cind,comb in enumerate([[0,0],[0,1],[1,1]]):
        name_cg = data_dir + return_name_md(N[0],N[1],float(L),comb)
        name_mr = data_dir + return_name_mr(N[0],N[1],L,[comb[0]+1,comb[1]+1])
        data_cg = np.loadtxt(name_cg,delimiter = ';')
        data_mr = np.loadtxt(name_mr)
        ax.plot(data_mr[:,0],data_mr[:,1],color=colors2['{:}{:}'.format(*comb)],linestyle = 'solid',linewidth = 2.5,label = '${:}{:}$'.format(comb[0]+1,comb[1]+1))
        ax.fill_between(data_mr[:,0],data_mr[:,1]-data_mr[:,2],data_mr[:,1]+data_mr[:,2],color=colors2['{:}{:}'.format(*comb)],alpha=0.3)
        ax.errorbar(data_cg[:,0],data_cg[:,1],yerr = data_cg[:,2],color=colors1['{:}{:}'.format(*comb)],marker = 'x',markersize = 4.0, linestyle = 'none',linewidth = 1.0,label = '${:}{:}$'.format(comb[0]+1,comb[1]+1))
        ax.set_xlim(-0.1,20)
        ax.set_ylim(-0.05,3.3)
        ax.set_xlabel('$r \ [\\sigma]$')
        ax.set_ylabel('$g_{ij}(r)$')
    plt.legend(ncol = 2, columnspacing = 0.5,handlelength = 0.7)
    phieff = (N[0]*(2*Rgs['50']['00.0'])**2+N[0]*(2*Rgs['50']['30.0'])**2)/float(L)**3
  #  plt.suptitle(titles[Lind] + '; $\\mathbf{{\\phi_{{eff}}}}$ = {:.2f}'.format(phieff))
    plt.savefig('gr_L{:}.pdf'.format(L))
        


# plotting
exit()
