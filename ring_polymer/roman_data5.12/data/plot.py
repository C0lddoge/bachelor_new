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
data_dir = './DATA/'
expo_dir = './EXPORT/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name(N1 = '256', N2 = '256', M1 = '50', M2 = '50', Bend1 = '00.0', Bend2 = '30.0', L = '097.21'):
  return 'MIXTURE_N1-{:}_N2-{:}_MPR1-{:}_MPR2-{:}_Bend1-{:}_Bend2-{:}_L-{:}'.format(N1, N2, M1, M2, Bend1, Bend2, L)

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
  return int(N) / float(L)**3

# styles
default_style = {
  'marker': 'o',
  'markersize': 1,
  'linestyle': 'solid',
  'linewidth': 1.5,
  'elinewidth': 1.0,
  'alpha': 0.80,
}

colors = {
   '1': 'red',
   '2': 'dodgerblue',
  '11': 'red',
  '12': 'darkmagenta',
  '22': 'dodgerblue',
}

# plotting
Ns = [
	['000', '256'],
	['128', '256'],
	['256', '256'],
	['256', '128'],
	['256', '000'],
]

fig, ax = plt.subplots(1, len(Ns), figsize = (4*len(Ns), 3))
for nind, N in enumerate(Ns):
  N1, N2 = N
  for c, comb in enumerate([[1,1], [1,2], [2,2]]):
    data = np.loadtxt(data_dir + return_name(N1 = N1, N2 = N2) + '-rdf_{:}{:}.dat'.format(*comb))
    ax[nind].errorbar(data[:,0] / unit_length, data[:,1], yerr = data[:,2], label = '{:}{:}'.format(*comb), **default_style, color = colors['{:}{:}'.format(*comb)])

  ax[nind].set_title('rho = {:}'.format(None))
  ax[nind].set_xlim(-0.1,7.1)
  ax[nind].set_ylim(-0.05,2.25)
  ax[nind].set_xlabel('r/R0_1')
  ax[nind].set_ylabel('$g_{ij}(r)$')
  ax[nind].legend(loc = 'best', fontsize = 10, handlelength = 0.8)

fig.savefig(expo_dir + '/gr.pdf')

exit()
