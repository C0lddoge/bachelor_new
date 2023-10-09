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
        '--part_ind',
        type = int,
        default = 1
        )
parser.add_argument(
        '--r_c',
        type = float,
        required = True
        )
parser.add_argument(
        '--max_lifetime',
        type = int,
        default = 50
        )
parser.add_argument(
        '--state',
        type = int,
        default = 1
        )

filename = vars(parser.parse_args())['file']
args = parser.parse_args()
data = cm.read_lammpstrj(filename,args.cutoff)
adj_mat,part_ind = cm.dyn_graph(data,args.part_ind,args.r_c)
hist,bins = cm.clust_time(adj_mat,args.state,args.part_ind,args.max_lifetime)
np.savetxt(args.save_path,np.column_stack((bins,hist)),fmt = '%1.5f',header ='| lifetime | P |' )





