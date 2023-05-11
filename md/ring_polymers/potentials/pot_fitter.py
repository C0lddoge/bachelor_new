#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from scipy.optimize import minimize
import argparse
import math


parser = argparse.ArgumentParser()

parser.add_argument(
    '--inputfile',
    type = str,
    required = True, 
    help = 'effectice potential to fit'
        )
#parser.add_argument(
   # '--outputfile',
  #  type = str,
 #   required = True,
#    help = 'output file containing the smoothed effective potential'

#        )

parser.add_argument(
    '--fitpoints',
    type = int,
    default = 10000,
    help = 'amount of points from the fit function in output'    
        )



args = parser.parse_args()
def fit_single(x, a, b):
  return a * np.exp(-(x/b)**4)

def fit_double(x, a, b, c,d,e):
  return a * np.exp(-((x-b)/c)**4) + d * np.exp(-((x-e)/c)**2) 

def force_double(x,a,b,c,e,f):
    return 4*a/(b**4)*(x-e)**3*np.exp(-((x-e)/b)**4)+(c*2*np.sign((x-f)/b)*(np.abs((x-f)/b))**2)/(x-f)*np.exp(-(np.sign((x-f)/b)*(np.abs((x-f)/b))**2))

def outer(a,b,c,d,e,f):
    def inner(x):
        return -(a*np.exp(-((x-e)/b)**4)+c*np.exp(((x-f)/b)**d))
    return inner

data = np.loadtxt(args.inputfile)
#popt1, pcov1 = curve_fit(fit_single, data[:,0], data[:,1])
#x_low = np.linspace(10**-8,0.5,90000)
#x = np.concatenate([x_low,np.linspace(0.5,20,args.fitpoints-len(x_low)+1)[1:]])
x = np.linspace(1e-3,15.0,args.fitpoints)
popt1, pcov1 = curve_fit(fit_double, data[:,0], data[:,1],maxfev = 10000)
plt.plot(x,fit_double(x,*popt1),label=f'fit')
#plt.plot(x,fit_double(x,*popt1),label='fit')
#plt.plot(x,force_double(x,*popt1),label='force')
plt.scatter(data[:,0],data[:,1],s = 2.0,label = 'input')
plt.legend()
plt.xlabel('r [sigma]')
plt.ylabel('Potential [epsilon]')
plt.show()
print(popt1)
#double_fit = fit_double(x,*popt1)
#double_force = force_double(x,*popt1)
#with open(args.outputfile,'x') as out_f:
   # out_f.write('ring_polymers\n')
  #  out_f.write('N {:}\n'.format(len(x)))
 #   out_f.write('\n')
#    for i in range(len(x)):
#        print(i)
#        out_f.write('{:} {:.10f} {:.10f} {:.10f}\n'.format(i+1,x[i],double_fit[i],double_force[i]))

#with open(args.outforce,'x') as out_fo:
 #   out_fo.write('ring polymers\n')
  #  out_fo.write('N {:}\n'.format(len(x)))
   # out_fo.write('\n')
    #for i in range(len(x)):
     #   out_fo.write('{:} {:} {:}\n'.format(i+1,x[i],double_force[i]))
    



print(popt1)

