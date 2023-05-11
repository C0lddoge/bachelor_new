import numpy as np
import os
import codemodule as cm
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
            "--density",
            type = float,
            required = True
            )
parser.add_argument(
            "--N",
            nargs = '+',
            type = int 
            )

parser.add_argument(
        "--T",
        type = float,
        default = 1.0
        )

parser.add_argument(
        "--xyz_switch",
        type = bool,
        default = False 

        )
parser.add_argument(
        "--e_switch",
        type = bool,
        default = False

        )
parser.add_argument(
        "--p_switch",
        type = bool,
        default = False
        )
parser.add_argument(
        "--config_path",
        type = str
        )
parser.add_argument(
        "--frame_path",
        type = str,
        default = ''
        )


input_dictionary = vars(parser.parse_args())

def sim_name(N, density,T):
    print(N)
    N_total = sum(N)
    types = len(N)
    return 'RP_N{:},{:}_T{:}_rho{:}'.format(N[0],N[1],T,density)


def simulate(N, density,T,xyz_switch,e_switch,p_switch,config_path,frame_path):
    if not os.path.isdir('data'):
      os.mkdir('data')
    sim_path = '{:}/data/{:}/'.format(os.getcwd(), sim_name(N, density,T))
    if not os.path.exists(sim_path):
        os.mkdir(sim_path)
    if not os.path.isfile(sim_path + '/log.dat'):
        open(sim_path + '/log.dat','x')
    plot_path = os.path.join(sim_path,'plots')
    if not os.path.isdir(plot_path):
        os.mkdir(plot_path)
    if not os.path.isdir(sim_path + 'results'):
        os.mkdir(sim_path+'results')
    if e_switch:
        E_tot_file = sim_path + '/ener.dat'
        if not os.path.isfile(E_tot_file):
            e_out = open(E_tot_file,'x')
        else:
            e_out = open(E_tot_file,'a')
    else:
        e_out = 0
    if xyz_switch:
        xyz_file = sim_path + '/frames.xyz'
        if not os.path.isfile(xyz_file):
            f_out = open(xyz_file,'x')
            initial = 0
        else:
            f_out = open(xyz_file,'a')
            xyz,types = cm.read_last(xyz_file)
            xyz = xyz.T
            initial = (xyz,types)

    potential_dict,error_dict = cm.read_config(config_path) 
    beta = 1.0/T
    trunc = 5.5
    mc_moves = 10**3
    max_displacement = 5.7
    energy_steps = 1000
    w_steps = 10000
    p_steps = 1000


    if frame_path != '':
        xyz,types = cm.read_1frames(frame_path)
        xyz = xyz.T
        initial = (xyz,types)
    accept_ratio = cm.simulate_num(N,beta,density,mc_moves,trunc,max_displacement,energy_steps,w_steps,p_steps,xyz_switch,e_switch,p_switch,potential_dict,initial,f_out,e_out)
    with open(sim_path + '/log.dat', 'a') as out_f:
        out_f.write('\ntrunc = {:}\nmc_moves = {:}\nenergy_steps = {:}\n xyz_steps = {:}\npressure_steps = {:}\nN = {:}\ndensity = {:}\nT = {:}\npotential_file = {:}, \naccept_ratio = {}'.format(trunc,mc_moves,energy_steps,w_steps,p_steps,N, density,T,config_path,accept_ratio))  
    out_f.close()


simulate(**input_dictionary)


















