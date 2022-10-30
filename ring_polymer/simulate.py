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

input_dictionary = vars(parser.parse_args())

def sim_name(N, density,T):
    print(N)
    N_total = sum(N)
    types = len(N)
    return 'RP_N{:d}_types{:}_dens{:.2e}_T{:.2e}'.format(N_total,types,density, T)


def simulate(N, density,T,xyz_switch,e_switch,p_switch,config_path):
    if not os.path.isdir('data'):
      os.mkdir('data')
    sim_path = '{:}/data/{:}/'.format(os.getcwd(), sim_name(N, density,T))
    if not os.path.exists(sim_path):
        os.mkdir(sim_path)
    plot_path = os.path.join(sim_path,'plots')
    if not os.path.isdir(plot_path):
        os.mkdir(plot_path)
    if not os.path.isdir(sim_path + 'results'):
        os.mkdir(sim_path+'results')
    E_tot_file = sim_path + '/ener.dat'
    xyz_file = sim_path + '/frames.xyz'
    pressure_file = sim_path +'/pressure.dat'
    potential_dict,error_dict = cm.read_config(config_path) 
    beta = 1.0/T
    trunc = 4.0
    mc_moves = 10**6
    max_displacement = 0.5
    energy_steps = 1000
    w_steps = 1000
    p_steps = 1000
    accept_ratio = cm.simulate_num(N,beta,density,mc_moves,trunc,max_displacement,energy_steps,w_steps,p_steps,xyz_switch,e_switch,p_switch,potential_dict,xyz_file,E_tot_file,pressure_file)
    with open(sim_path + '/log.dat', 'w') as out_f:
        out_f.write('\ntrunc = {:}\nmc_moves = {:}\nenergy_steps = {:}\n xyz_steps = {:}\npressure_steps = {:}\nN = {:}\ndensity = {:}\nT = {:}\npotential_file = {:}, \naccept_ratio = {}'.format(trunc,mc_moves,energy_steps,w_steps,p_steps,N, density,T,config_path,accept_ratio))  
    out_f.close()


simulate(**input_dictionary)


















