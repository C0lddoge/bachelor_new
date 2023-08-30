import numpy as np
import codemodule as cm
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

def gauss_fit(data,t):
    data_r = data[:,0]
    data_g = data[:,1]
    f = lambda r,D: np.exp(-r**2/(4*D*t))/np.sqrt(4*np.pi*D*t)**3
    popt,pcov = curve_fit(f,data_r,data_g)
   # plt.plot(log_time,log_msd,label = 'data')
   # plt.plot(log_time,f_lin(log_time,*popt), label = 'fit')
   # plt.show()
    return popt,pcov

     

