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
  

flexible = np.loadtxt("diff_coeff_ty1.dat")
semiflexible = np.loadtxt("diff_coeff_ty2.dat")

plt.errorbar(flexible[:,0],flexible[:,1],yerr=flexible[:,2], marker = 'x',linewidth = 0.0,elinewidth = 1.0,label = 'flexible', color = 'red')
plt.errorbar(flexible[:,0],semiflexible[:,1], yerr=semiflexible[:,2],marker = 'x',linewidth = 0.0, elinewidth = 1.0,label = 'semiflexible', color = 'blue')
plt.xlabel('Boxsize $[\\sigma]$')
plt.ylabel('D $[\\sigma^2/\\tau]$')
plt.legend()
plt.savefig('diff_coeffs_unscaled.pdf')

