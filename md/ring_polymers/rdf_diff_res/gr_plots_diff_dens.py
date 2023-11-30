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
data_dir = './rdf_newpot/'
expo_dir = './export_rp/'
for ddir in [data_dir, expo_dir]:
  if not os.path.exists(ddir):
    os.mkdir(ddir)

def return_name_mc(N1,N2,dens,types):
    return 'RP_N{:},{:}_rho{:}_rdf_{:}{:}_mc.dat'.format(N1,N2,dens,*types)

def return_name_md(N1, N2, L,types):
    return 'RP_N{:},{:}_L{:}_newpot_rdf_{:}{:}.dat'.format(N1,N2,L,*types)
def return_name_mr(N1,N2,L,types):
    return 'MIXTURE_N1-{:}_N2-{:}_MPR1-50_MPR2-50_Bend1-00.0_Bend2-30.0_L-{:}-rdf_{:}{:}.dat'.format(N1,N2,L,*types)


# constants, concentrations etc
Rgs = {
	# size and stiffness
	'50': {
		'00.0': 3.55,
		'30.0': 6.51,
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
  '12': 'darkmagenta',
  '22': 'dodgerblue',
}

# plotting
N = ['256','256']

Ls = ['108.60','080.00','063.50','055.47','050.40','046.78','044.03']
#names = ['$\\mu$','$\\kappa$','$\\gamma$','$\\zeta$','$\\eta$','$\\eta$']

#for nind,L in enumerate(Ls):
#  rho0 = return_concentration(N[0],L)
 # rho1 = return_concentration(N[1],L)
  #overlap0 = return_overlap(50,Rgs["50"]["00.0"])
  #overlap1 = return_overlap(50,Rgs["50"]["30.0"])
  #r0 = rho0/overlap0
  #r1 = rho1/overlap1
  #x,y = np.unravel_index(nind,(4,2))
  #for c, comb in enumerate([[1,1], [1,2], [2,2]]):
   #   print(data_dir + return_name_mr(N[0],N[1],L,comb))
    #  if os.path.exists(data_dir + return_name_mr(N[0],N[1],L,comb)):
     #   print('test')
      #  data = np.loadtxt(data_dir + return_name_mr(N[0],N[1],L,comb))
       # r = data[:,0]
#        ax[x][y].plot(r,data[:,1],label = 'MR; {:}{:}'.format(comb[0],comb[1]),linewidth = 1.0, color = colors['{:}{:}'.format(*comb)])
 #       ax[x][y].fill_between(data[:,0],data[:,1]-data[:,2],data[:,1]+data[:,2],color = colors['{:}{:}'.format(*comb)],alpha = 0.5)
 # ax[x][y].text(1,1.5, names[nind], fontsize = 35, bbox = dict(facecolor = 'grey', alpha = 0.5))
  #ax[x][y].set_title('$L = {:}; N_1 = {:}; N_2= {:};$'.format(L,int(N[0]),int(N[1])))
  #ax[x][y].set_xlim(-0.1,7.1)
  #ax[x][y].set_ylim(-0.05,2.25)
  #ax[x][y].set_xlabel('$r[\\sigma]$')
  #ax[x][y].set_ylabel('$g_{ij}(r)$')
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

# plotting


Ls = ['43.68','41.98','41.61']
Ns = [[1000,0],[0,1000],[1331,0],[0,1331],[1728,0],[0,1728]]
fig, ax = plt.subplots(1, 3,figsize = (20,10))
rhos = [1000/43.68**3,1331/41.98**3,1728/41.61**3]
comb1 = [0,0]
comb2 = [1,1]
for nind,L in enumerate(Ls):
    for n,N in enumerate(Ns):
      if os.path.exists(data_dir + return_name_md(N[0],N[1],L,comb1)):
        print('test')
        data = np.loadtxt(data_dir + return_name_md(N[0],N[1],L,comb1),delimiter =';')
        if N[0] == 0:

            ax[nind].errorbar(data[:,0], data[:,1],yerr = data[:,2],marker ='x',linewidth = 1.5,elinewidth = 1.0, label = 'CG; {:}{:}'.format(comb2[1]+1,comb2[0]+1),markersize= 2.0, color = colors2['{:}{:}'.format(*comb2)])
        else:
            ax[nind].errorbar(data[:,0], data[:,1],yerr = data[:,2],marker = 'x',linewidth = 1.5,elinewidth = 1.0, label = 'CG; {:}{:}'.format(comb1[1]+1,comb1[0]+1),markersize= 2.0, color = colors2['{:}{:}'.format(*comb1)])


  #ax[x][y].set_title('$\\rho_0^* = {:.2f}; \\rho_1^* = {:.2f}; N_0 = {:}; N_1 = {:};$'.format(r0,r1,int(N[0]),int(N[1])))

    ax[nind].set_title('$ \\rho = {:3f} \ \\sigma^{{-3}}$'.format(rhos[nind]))
    ax[nind].set_xlim(-0.1,20)
    ax[nind].set_ylim(-0.05,3.3)
    ax[nind].set_xlabel('$r[\\sigma]$')
    ax[nind].set_ylabel('$g_{ij}(r)$')
    ax[nind].legend(loc = 'upper right', fontsize = 15, handlelength = 0.8, ncol = 2)


#fig.delaxes(ax[3][1])
fig.savefig(expo_dir + 'gr_newpot_pure_highdens.pdf')

exit()
