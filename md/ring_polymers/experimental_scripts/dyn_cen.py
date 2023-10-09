import numpy as np
import argparse 
import matplotlib.pyplot as plt
import codemodule as cm


parser = argparse.ArgumentParser()

parser.add_argument(
        "--file",
        type = str,
        required = True,
        )
parser.add_argument(
        '--cutoff',
        type = float,
        default = 0.0,
        )
parser.add_argument(
        '--save_path',
        type = str,
        default = './'
        )
parser.add_argument(
        '--save_path_cenarr',
        type = str,
        default = './'
        )
parser.add_argument(
        '--tau_N',
        type = int,
        default = 20
        )
parser.add_argument(
        '--types',
        type = int,
        required = True
        )
parser.add_argument(
        '--error_len',
        type = int,
        default = 0
        )
parser.add_argument(
        '--r_c',
        type = float,
        default = 4.5
        )

filename = vars(parser.parse_args())['file']
args = parser.parse_args()
data = cm.read_lammpstrj(filename,args.cutoff)
types = [int(i) for i in data[0]['types']] 
adj_mat = cm.dyn_graph_ser(data,args.r_c)
cen_scores,taus,avg_cen,err = cm.mean_centrality(adj_mat,types,args.tau_N,args.types,args.error_len)
np.savetxt(args.save_path,np.column_stack((taus,avg_cen,err)),fmt = '%1.5f',header ='| compound time | mean centrality | error' )
np.savetxt(args.save_path_cenarr,cen_scores,fmt = '%1.5f',header = '|rows = particle index | columns = compound time' )




