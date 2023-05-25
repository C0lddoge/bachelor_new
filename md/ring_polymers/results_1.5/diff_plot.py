import matplotlib.pyplot as plt
import numpy as np
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
  
data_dir = "diff_data/"
export_dir = "diff_export/"
flexible = np.loadtxt(data_dir + "diff_coeff_ty1.dat")
semiflexible = np.loadtxt(data_dir + "diff_coeff_ty2.dat")
N_total = 512
plt.errorbar(N_total/flexible[:,0]**3,flexible[:,1],yerr=flexible[:,2], marker = 'x',linewidth = 0.0,elinewidth = 1.0,label = 'flexible', color = 'red')
plt.errorbar(N_total/flexible[:,0]**3,semiflexible[:,1], yerr=semiflexible[:,2],marker = 'x',linewidth = 0.0, elinewidth = 1.0,label = 'semiflexible', color = 'blue')
plt.xlabel('$\\rho \ [\\sigma^{{-3}}]$')
plt.ylabel('D $[\\sigma^2/\\tau]$')
plt.legend()
plt.savefig(export_dir + 'diff_coeffs_unscaled.pdf')


