import numpy as np
import codemodule as cm
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def f_lin(x,alpha,d):
    return alpha*x+d

def diff_coeff(msd_data,time_range):
    mask = np.logical_and(msd_data[:,0]>=time_range[0],msd_data[:,0]<=time_range[1])
    msd_data = msd_data[mask]
    log_msd = np.log(msd_data[:,1])
    log_time = np.log(msd_data[:,0])
    popt,pcov = curve_fit(f_lin,log_time,log_msd)
    print(pcov)
    D_coeff = np.exp(popt[1])
    D_err = (np.sqrt(np.diag(pcov))[1])
    D_err = D_coeff*D_err
    alpha_err = np.sqrt(np.diag(pcov)[0])
   # plt.plot(log_time,log_msd,label = 'data')
   # plt.plot(log_time,f_lin(log_time,*popt), label = 'fit')
   # plt.show()
    return {'D' : D_coeff, 'D_err': D_err, 'alpha': popt[0], 'alpha_err': alpha_err}

     

