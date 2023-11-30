#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os

# plt settings
plt.style.use('bmh')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 25,
    "axes.titlesize": 30,
    "axes.labelsize": 30,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
	})

# paths
def gem_double(x, a, b, c, d, e, f):
    return a*np.exp(-((x-b)/c)**4) + d*np.exp(-((x-e)/f)**2)





# styles
default_style = {
  'linewidth': 1.0,
}

colors1 = {
  '00': 'magenta',
  '01': 'rebeccapurple',
  '11': 'dodgerblue',
}
params = {
        '00':[4.24077751,-0.07393337,3.64147053,3.39512498,2.17768182,3.64147053],
        '01':[0.36063821,-4.35526194,4.37715016,1.23648558,3.94265459,4.37715016],
        '11':[-6.58204409,-8.42927522,9.75657746,8.45336962,-6.45205662,9.75657746]
        }

rs = np.linspace(0,20,num=300)
fig,ax=plt.subplots(figsize = (10,7))
labels = ['11','12','22']
for cind,comb in enumerate(['00','01','11']):
    ax.plot(rs,gem_double(rs,*params[comb]),label = '${:}$'.format(labels[cind]),color = colors1[comb],linewidth=2.5)
plt.xlabel('$r \ [\\sigma]$')
plt.legend()
plt.ylabel('$\\beta V_{\\mathrm{eff}}(r)$')
plt.savefig('potentials.pdf')
        


# plotting
exit()
