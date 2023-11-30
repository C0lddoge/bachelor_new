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
        required = True
        )
parser.add_argument(
        '--qmax',
        type = int,
        required = True
        )
parser.add_argument(
        '--type',
        type = int,
        required = True
        )
parser.add_argument(
        '--save_file',
        type = str,
        required = True
        )
parser.add_argument(
    '--bin_len',
    type = int,
    default = 0
        )
parser.add_argument(
    '--stride',
    type = int,
    default = 1
        )
 
args = parser.parse_args()
data = cm.read_lammpstrj(args.file,args.cutoff)
res = cm.structure_factor(data,args.type,args.qmax,args.stride,args.bin_len)
np.savetxt(args.save_file,res, header = 'q | S(q) | error')




