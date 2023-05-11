import numpy as np



data_dir = './data_rp/'

def name_gen(N,types,rho):
    return 'RP_N{:},{:}_T1.0_rho{:}_cluster_rc2.0_types_{:}_v2.dat'.format(N[0],N[1],rho,types)

systems = [[128,256,0.01875],[256,128,0.01875],[256,256,0.025]]
rhos = [0.01875,0.01875,0.025]
types = ['11','all']



for system in systems:
    Ps = []
    N_tot = system[0]+system[1]
    N_2 = system[1]
    P_tot = np.loadtxt(data_dir + name_gen(system[:2],'all',system[2]), delimiter = ';')[1,1]
    P_tot_err = np.loadtxt(data_dir + name_gen(system[:2],'all',system[2]), delimiter = ';')[1,2]
    P_22 = np.loadtxt(data_dir + name_gen(system[:2],'11',system[2]), delimiter = ';')[1,1]
    P_22_err = np.loadtxt(data_dir + name_gen(system[:2],'11',system[2]), delimiter = ';')[1,2]
    print(P_22_err)
    C22 = N_2*P_22/(N_tot*P_tot)
    C22_err = np.sqrt((N_2/(N_tot*P_tot))**2*P_22_err**2 + (-(N_2*P_22)/(N_tot*P_tot**2))**2*P_tot_err**2)
    C12 = 1-C22
    print(f'{system}:\n C22: {C22} +- {C22_err} \n C12: {C12} +- {C22_err}\n')








