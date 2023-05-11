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
data_dir = './data_rp/'
expo_dir = './export_rp/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name(N1 = '256', N2 = '256', M1 = '50', M2 = '50', Bend1 = '00.0', Bend2 = '30.0', L = '097.21'):
  return 'MIXTURE_N1-{:}_N2-{:}_MPR1-{:}_MPR2-{:}_Bend1-{:}_Bend2-{:}_L-{:}'.format(N1, N2, M1, M2, Bend1, Bend2, L)

def return_name_me(N1 = '256', N2 = '256', dens = '0.025',types=[0,0]):
    return 'RP_N{:},{:}_T1.0_rho{:}_rdf_{:}{:}_mc.dat'.format(N1,N2,dens,*types)


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
   '0': 'blue',
   '1': 'red',
  '00': 'blue',
  '10': 'darkmagenta',
  '11': 'red',
}

colors2 = {
   '1': 'dodgerblue',
   '2': 'darkred',
  '11': 'dodgerblue',
  '21': 'rebeccapurple',
  '22': 'darkred',
}
# plotting
Ns = [
	['0', '256'],
	['256', '256'],
	['256','0'],
]
Ns2 = [
	['000', '256'],
	['256', '256'],
	['256','000'],
]
default_style2 = {
  'marker': 'x',
  'markersize': 2.0,
  'alpha': 0.80,
}

dens = ['0.0125','0.025','0.0125']
labels = ['ff','sf','ss']
#names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']

#plt.figure(figsize = (18,10))
for nind,N in enumerate(Ns):
  plt.clf()
  rho0 = return_concentration(N[0])
  rho1 = return_concentration(N[1])
  overlap0 = return_overlap(50,Rgs["50"]["00.0"])
  overlap1 = return_overlap(50,Rgs["50"]["30.0"])
  r0 = rho0/overlap0
  r1 = rho1/overlap1
  for c, comb in enumerate([[0,0], [1,0], [1,1]]):
      if os.path.exists(data_dir + return_name_me(N[0],N[1],dens[nind],comb)):
        print('true')
        data = np.loadtxt(data_dir + return_name_me(N[0],N[1],dens[nind],comb),delimiter =';')
        plt.plot(data[:,0], data[:,1],label = 'CG;{:}'.format(labels[c]),linewidth = 1.0, color = colors['{:}{:}'.format(*comb)])
        plt.fill_between(data[:,0],data[:,1]-data[:,2],data[:,1]+data[:,2],color = colors['{:}{:}'.format(*comb)],alpha = 0.5)
        data = np.loadtxt(data_dir + return_name(Ns2[nind][0],Ns2[nind][1])+ '-rdf_{:}{:}.dat'.format(comb[0]+1,comb[1]+1))
        plt.errorbar(data[:,0]/unit_length, data[:,1],yerr = data[:,2],marker = 'x',linewidth = 0.0,elinewidth = 1.0, label = 'MR;{:}'.format(labels[c]),markersize= 2.0, color = colors2['{:}{:}'.format(comb[0]+1,comb[1]+1)])
  #ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  plt.title('$N_f = {:}; N_s = {:};$'.format(int(N[0]),int(N[1])))
  plt.xlim(-0.1,7.1)
  plt.ylim(-0.05,2.25)
  plt.xlabel('$r/R^0_f$')
  plt.ylabel('$g_{ij}(r)$')
  plt.legend(fontsize = 15,ncol = 2, loc = 'upper right')
  #ax[x][y].legend(loc = 'best', fontsize = 13, handlelength = 0.8)
  plt.savefig(f'grslides{nind}.pdf')



