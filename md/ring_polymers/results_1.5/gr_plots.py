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
data_dir = './data_old/'
expo_dir = './export_rp/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name_mc(N1,N2,dens,types):
    return 'RP_N{:},{:}_rho{:}_rdf_{:}{:}_mc.dat'.format(N1,N2,dens,*types)

def return_name_md(N1, N2, L,types):
    return 'RP_N{:},{:}_L{:}_rdf_{:}{:}.dat'.format(N1,N2,L,*types)
def return_name_mr(N1,N2,types):
    return 'MIXTURE_N1-{:}_N2-{:}_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-097.21-rdf_{:}{:}.dat'.format(N1,N2,*types)


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

# styles
default_style = {
  'linewidth': 1.0,
}

colors = {
   '1': 'red',
   '2': 'dodgerblue',
  '11': 'red',
  '21': 'darkmagenta',
  '22': 'dodgerblue',
}

# plotting
Ns = [
	['000', '256'],
        ['256','000'],
	['128', '256'],
	['256','128'],
	['256', '256'],
        ['256','256']
]

dens = ['97.21','97.21','97.21','97.21','97.21','97.21']
names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']

fig, ax = plt.subplots(3, 2,figsize = (12,15))
for nind,N in enumerate(Ns):
  rho0 = return_concentration(N[0])
  rho1 = return_concentration(N[1])
  overlap0 = return_overlap(50,Rgs["50"]["00.0"])
  overlap1 = return_overlap(50,Rgs["50"]["30.0"])
  r0 = rho0/overlap0
  r1 = rho1/overlap1
  x,y = np.unravel_index(nind,(3,2))
  for c, comb in enumerate([[1,1], [2,1], [2,2]]):
      print(data_dir + return_name_mr(N[0],N[1],comb))
      if os.path.exists(data_dir + return_name_mr(N[0],N[1],comb)):
        print('test')
        data = np.loadtxt(data_dir + return_name_mr(N[0],N[1],comb))
        r = data[:,0]
        ax[x][y].plot(r,data[:,1],label = 'MR; {:}{:}'.format(comb[0]-1,comb[1]-1),linewidth = 1.0, color = colors['{:}{:}'.format(*comb)])
        ax[x][y].fill_between(data[:,0],data[:,1]-data[:,2],data[:,1]+data[:,2],color = colors['{:}{:}'.format(*comb)],alpha = 0.5)
  ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  ax[x][y].set_title('$\\rho_0/\\rho_0^* = {:.2f}; \\rho_1/\\rho_1^* = {:.2f}; N_0 = {:}; N_1 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
  ax[x][y].set_xlim(-0.1,7.1)
  ax[x][y].set_ylim(-0.05,2.25)
  ax[x][y].set_xlabel('$r[\\sigma]$')
  ax[x][y].set_ylabel('$g_{ij}(r)$')
  #ax[x][y].legend(loc = 'best', fontsize = 13, handlelength = 0.8)


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

Ns2 = [
	['0', '256'],
        ['256','0'],
	['128', '256'],
	['256','128'],
	['256', '256'],
        ['256','256']
]
# plotting


for nind,N in enumerate(Ns2):
  rho0 = return_concentration(N[0])
  rho1 = return_concentration(N[1])
  overlap0 = return_overlap(50,Rgs["50"]["00.0"])
  overlap1 = return_overlap(50,Rgs["50"]["30.0"])
  r0 = rho0/overlap0
  r1 = rho1/overlap1
  x,y = np.unravel_index(nind,(3,2))
  for c, comb in enumerate([[0,0], [1,0], [1,1]]):
      print(data_dir + return_name_md(N[0],N[1],dens[nind],comb))
      if os.path.exists(data_dir + return_name_md(N[0],N[1],dens[nind],comb)):
        print('test')
        data = np.loadtxt(data_dir + return_name_md(N[0],N[1],dens[nind],comb),delimiter =';')
        ax[x][y].errorbar(data[:,0], data[:,1],yerr = data[:,2],marker = 'x',linewidth = 0.0,elinewidth = 1.0, label = 'MD; {:}{:}'.format(*comb),markersize= 2.0, color = colors2['{:}{:}'.format(*comb)])

  #ax[nind].set_title('$\\rho_0^* = {:.4f}; \\rho_1^* = {:.4f}; N_0 = {:}; N_1 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
  ax[x][y].set_xlim(-0.1,20)
  ax[x][y].set_ylim(-0.05,2.25)
  ax[x][y].set_xlabel('$r[\\sigma]$')
  ax[x][y].set_ylabel('$g_{ij}(r)$')
  ax[x][y].legend(loc = 'upper right', fontsize = 15, handlelength = 0.8, ncol = 2)



fig.savefig(expo_dir + 'gr2.pdf')

exit()
