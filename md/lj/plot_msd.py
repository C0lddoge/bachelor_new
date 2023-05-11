import numpy as np
import matplotlib.pyplot as plt
import codemodule as cm


plt.style.use('bmh')
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.size": 15,
    "axes.titlesize": 15,
    "axes.labelsize": 15,
    "font.sans-serif": ["Helvetica"],
    "axes.facecolor": '#ffffff',
    "figure.autolayout": True,
        })
   


data1 = np.loadtxt('MSDs1.dat')
data2 = np.loadtxt('MSDs2.dat')
msd1 = data1[:,:2]
msd2 = data2[:,:2]
msd1_part = data1[:,2:]
msd2_part = data2[:,2:]
N1 = data1[0,2:]
N2 = data2[0,2:]
std1 = np.sqrt(np.var(msd1_part,axis = 1))
std2 = np.sqrt(np.var(msd2_part,axis = 1))
err1 = []
for i in range(len(msd1[:,0])):
    err1.append(np.sqrt(cm.bin_ana(msd1_part[i,:],10)))

err2 = []
for i in range(len(msd1[:,0])):
    err2.append(np.sqrt(cm.bin_ana(msd2_part[i,:],10)))


plt.errorbar(msd1[:,0],msd1[:,1],yerr = err1,marker ='o',linewidth = 0.5, color = 'red', markersize = 0.5,label='type 1')
plt.errorbar(msd2[:,0],msd2[:,1],yerr = err2 ,marker = 'o',linewidth = 0.5, color = 'blue', markersize = 0.5,label='type 2')
plt.fill_between(msd1[:,0],msd1[:,1]-std1,msd1[:,1]+std1,color = 'red', alpha = 0.6)
plt.fill_between(msd1[:,0],msd1[:,1]-std2,msd1[:,1]+std2, color = 'cornflowerblue', alpha = 0.6)
plt.xlabel('lag time $[\\tau]$')
plt.ylabel('MSD $[\\sigma^2]$')
plt.legend()
plt.yscale('log')
plt.xscale('log')
plt.savefig('msd.pdf')

