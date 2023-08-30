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
flexible = np.loadtxt(data_dir + "diff_coeff_ty1_nvt.dat")
semiflexible = np.loadtxt(data_dir + "diff_coeff_ty2_nvt.dat")
flexible_newdamp = np.loadtxt(data_dir + "diff_coeff_ty1_newdamp.dat")
semiflexible_newdamp = np.loadtxt(data_dir + "diff_coeff_ty2_newdamp.dat")
N_total = 512
plt.errorbar(N_total/flexible[:,0]**3,flexible[:,1],yerr=flexible[:,2], marker = 'x',linewidth = 0.0,elinewidth = 1.0,label = 'flexible nvt', color = 'red')
plt.errorbar(N_total/flexible[:,0]**3,semiflexible[:,1], yerr=semiflexible[:,2],marker = 'x',linewidth = 0.0, elinewidth = 1.0,label = 'semiflexible nvt', color = 'blue')
plt.errorbar(N_total/flexible[:,0]**3,flexible_newdamp[:,1], yerr=flexible_newdamp[:,2],marker = '2',linewidth = 0.0, elinewidth = 1.0,label = 'flexible newdamp', color = 'red')
plt.errorbar(N_total/flexible[:,0]**3,semiflexible_newdamp[:,1], yerr=semiflexible[:,2],marker = '2',linewidth = 0.0, elinewidth = 1.0,label = 'semiflexible newdamp', color = 'blue')
plt.xlabel('$\\rho \ [\\sigma^{{-3}}]$')
plt.ylabel('D $[\\sigma^2/\\tau]$')
plt.legend(fontsize = 10)
plt.savefig(export_dir + 'diff_coeffs_unscaled_newdamp.pdf')


