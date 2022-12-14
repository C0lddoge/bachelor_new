import argparse
import codemodule as cm
import os
import numpy as np
import matplotlib.pyplot as plt

parser = argparse.ArgumentParser()
parser.add_argument(
        "--directory",
        type = str,
        required = True
        )

parser.add_argument(
        '--energy_pressure',
        type = bool,
        default = False
        )
parser.add_argument(
        '--g_r',
        type = bool,
        default = False

        )
parser.add_argument(
        '--A_k',
        type = bool,
        default = False
        )

directory = vars(parser.parse_args())["directory"]
energy_pressure = vars(parser.parse_args())['energy_pressure']
g_r = vars(parser.parse_args())['g_r']
A_k = vars(parser.parse_args())['A_k']
xyz_path = '{:}/frames.xyz'.format(directory)
ener_path = '{:}/ener.dat'.format(directory)
p_path = '{:}/pressure.dat'.format(directory)
def result_path(resultname):

    return directory + '/results/' + resultname

def plot_path(plotname):

    return directory + '/plots/' + plotname +'.eps'

N =int(directory[4:7]) 
rho = float(directory[20:28])
T = float(directory[30:37])
print(N)
print(rho)
print(T)
xyz,types = cm.read_xyz(xyz_path,500,1500)
if energy_pressure == False:

    data = cm.read_txt(ener_path,';')
    data = cm.equilibrate(data,0.2)
    plt.plot(cm.equil_check(data,30))
    plt.show()
    name_tag = '_ener'
    y_name = 'E'
    switch = int(input())
    tail_correction = cm.tail_correction_lj(2.5,N,rho,1,1)

if energy_pressure:

    data = cm.read_txt(p_path,';')
    data = cm.equilibrate(data,0.3)
    plt.plot(cm.equil_check(data,30))
    plt.show()
    name_tag = '_pressure'
    y_name = 'P'
    switch = int(input())

if g_r:
    pairs,r,g,error = cm.rad_dist_types(xyz,types,0.05,rho)
    for i in range(len(pairs)):
        plt.plot(r[i],g[i])
        plt.xlabel('r')
        plt.ylabel(f'g_{pairs[i]}(r)')
        plot_name = f'g_{pairs[i]}r'
        file_name = f'g_r{pairs[i]}.dat'
        plt.savefig(plot_path(plot_name), format = 'eps')
        plt.clf()
        np.savetxt(result_path(file_name),(r[i],g[i],error[i]),fmt = '%.6e', delimiter = ';')

if switch == 1:
    if A_k:
       k,A=cm.A(data)
       tau,tau_final = cm.A_time(A)
       kmax = np.arange(1,len(tau)+1)

       plt.plot(k,A)
       plt.xlabel('k')
       plt.ylabel('A')
       plot_name = 'A_k' + name_tag
       file_name = 'A_k' + name_tag +'.dat'
       plt.savefig(plot_path(plot_name), format = 'eps')
       plt.clf()
       cm.write_xy(result_path(file_name),(k,A))

       plt.plot(tau)
       plt.xlabel('kmax')
       plt.ylabel('tau')
       plot_name = 'corr_time' + name_tag
       file_name = 'corr_time.' + name_tag + 'dat'
       plt.savefig(plot_path(plot_name), format = 'eps')
       plt.clf()
       cm.write_xy(result_path(file_name),(kmax,tau))
       N_eff = len(data[:,1])/(2*tau_final)
       error = np.sqrt(np.var(data[:,1])/N_eff)
    if not A_k:
        Nb = np.arange(2,500)
        plot = []
        for i in Nb:
            plot.append(cm.bin_ana(data,i))
        k = len(data)//Nb
        plt.plot(Nb,np.array(plot), '.',  markersize = 3.0)
        plt.show()
        input_nb = int(input())
        error = np.sqrt(cm.bin_ana(data,input_nb))




    plt.plot(data[:,1])
    plt.xlabel('mc-step')
    plt.ylabel(y_name)
    plot_name = 'series' + name_tag
    file_name = 'series' + name_tag
    plt.savefig(plot_path(plot_name), format = 'eps')
    plt.clf()
    cm.write_xy(result_path(file_name),(data[:,0],data[:,1]))



    if not os.path.isfile(result_path('results.dat')):
        f = open(result_path('results.dat'),'x')
    else:
        f = open(result_path('results.dat'),'a')

    if not energy_pressure:
        error_part = error/N
        avg_e = np.mean(data[:,1])
        E_pot_part = avg_e/N
        E_kin = 3/2 * T
        E_tot = E_pot_part + E_kin + tail_correction
        f.write('\n avg_E = {:} +- {:} \n E_part = {:} +- {:} \n E_kin = {:} \n E_tot_part = {:} +- {:}'.format(avg_e,error,E_pot_part,error_part,E_kin,E_tot,error_part,tail_correction))
        f.close()
    
    if energy_pressure:
        avg_p = np.mean(data[:,1])
        f.write('\n avg_p = {:} +- {:} \n'.format(avg_p,error))
        f.close()


















