#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os

# plt settings
plt.style.use('bmh')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 12,
    "axes.titlesize": 12,
    "axes.labelsize": 12,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
	})

# paths
data_dir = './data/'
expo_dir = './EXPORT/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name(N1 = '256', N2 = '256', M1 = '50', M2 = '50', Bend1 = '00.0', Bend2 = '30.0', L = '097.21'):
  return 'MIXTURE_N1-{:}_N2-{:}_MPR1-{:}_MPR2-{:}_Bend1-{:}_Bend2-{:}_L-{:}'.format(N1, N2, M1, M2, Bend1, Bend2, L)

def return_name_me(N1 = '256', N2 = '256', dens = '0.025',types=[0,0]):
    return 'RP_N{:},{:}_T1.0_rho{:}_rdf_{:}{:}.dat'.format(N1,N2,dens,*types)


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
   '0': 'red',
   '1': 'dodgerblue',
  '00': 'red',
  '10': 'darkmagenta',
  '11': 'dodgerblue',
}

# plotting
Ns = [
	['0', '256'],
	['128', '256'],
	['256', '256'],
	['256', '128'],
	['256', '0'],
]

dens = ['0.0125','0.01875','0.025','0.01875','0.0125']

fig, ax = plt.subplots(1, len(Ns), figsize = (4*len(Ns), 3))
for nind,N in enumerate(Ns):
  print(N[0])
  rho0 = return_concentration(N[0])
  print(rho0)
  rho1 = return_concentration(N[1])
  overlap0 = return_overlap(50,Rgs["50"]["00.0"])
  print(overlap0)
  overlap1 = return_overlap(50,Rgs["50"]["30.0"])
  r0 = rho0/overlap0
  r1 = rho1/overlap1
  for c, comb in enumerate([[0,0], [1,0], [1,1]]):
      print(return_name_me(N[0],N[1],dens[c],comb))
      if os.path.exists(data_dir + return_name_me(N[0],N[1],dens[nind],comb)):
        data = np.loadtxt(data_dir + return_name_me(N[0],N[1],dens[nind],comb),delimiter =';')
        ax[nind].plot(data[:,0], data[:,1], label = 'coarse-grained;{:}{:}'.format(comb[0]+1,comb[1]+1),**default_style, color = colors['{:}{:}'.format(*comb)])

  ax[nind].set_title('$\\rho_1/\\rho_1^* = {:.4f}; \\rho_2/\\rho_2^* = {:.4f}; N_1 = {:}; N_2 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
  ax[nind].set_xlim(-0.1,7.1)
  ax[nind].set_ylim(-0.05,2.25)
  ax[nind].set_xlabel('$r/R^0_1$')
  ax[nind].set_ylabel('$g_{ij}(r)$')
  ax[nind].legend(loc = 'best', fontsize = 10, handlelength = 0.8)


default_style2 = {
  'marker': 'x',
  'markersize': 2.0,
  'alpha': 0.80,
}


colors2 = {
   '1': 'red',
   '2': 'dodgerblue',
  '11': 'red',
  '12': 'darkmagenta',
  '22': 'dodgerblue',
}

# plotting
Ns2 = [
	['000', '256'],
	['128', '256'],
	['256', '256'],
	['256', '128'],
	['256', '000'],
]


for nind,N in enumerate(Ns2):
  print(N[0])
  rho0 = return_concentration(N[0])
  print(rho0)
  rho1 = return_concentration(N[1])
  overlap0 = return_overlap(50,Rgs["50"]["00.0"])
  print(overlap0)
  overlap1 = return_overlap(50,Rgs["50"]["30.0"])
  r0 = rho0/overlap0
  r1 = rho1/overlap1
  for c, comb in enumerate([[1,1], [1,2], [2,2]]):
      print(data_dir + return_name(N[0],N[1])+ '-rdf_{:}{:}.dat'.format(comb[0],comb[1]))
      if os.path.exists(data_dir + return_name(N[0],N[1]) + '-rdf_{:}{:}.dat'.format(comb[0],comb[1])):
        data = np.loadtxt(data_dir + return_name(N[0],N[1])+ '-rdf_{:}{:}.dat'.format(comb[0],comb[1]))
        ax[nind].plot(data[:,0]/unit_length, data[:,1], 'x',label = 'monomer-resolved; {:}{:}'.format(*comb),markersize= 2.0, color = colors2['{:}{:}'.format(*comb)])

  #ax[nind].set_title('$\\rho_0^* = {:.4f}; \\rho_1^* = {:.4f}; N_0 = {:}; N_1 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))
  ax[nind].set_xlim(-0.1,7.1)
  ax[nind].set_ylim(-0.05,2.25)
  ax[nind].set_xlabel('$r/R^0_1$')
  ax[nind].set_ylabel('$g_{ij}(r)$')
  ax[nind].legend(loc = 'upper right', fontsize = 7, handlelength = 0.8)



fig.savefig(expo_dir + '/grboth.pdf')

exit()
