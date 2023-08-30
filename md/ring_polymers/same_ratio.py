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
        default = 0.2,
        )
parser.add_argument(
        '--r_c',
        type = float,
        default = 4.5,
        )
parser.add_argument(
        '--save_path',
        type = str,
        default = './'
        )
parser.add_argument(
        '--error_len',
        type = int,
        default = 0
        )
parser.add_argument(
        '--lag',
        type = int,
        default = 1,
        )
parser.add_argument(
        '--type_flag',
        type = str,
        default = 'all'
        )
parser.add_argument(
        '--low_s',
        type = float,
        required = True
        ) 
parser.add_argument(
        '--high_s',
        type = float,
        required = True
        )
parser.add_argument(
        '--bin_width',
        type = float,
        default = 0.05
        )
args = parser.parse_args()
r,van,error = cm.same_ratio(args.file,args.r_c,args.cutoff,args.lag,args.low_s,args.high_s,args.type_flag,args.bin_width,args.error_len)
np.savetxt(args.save_path,np.column_stack((r,van,error)),fmt = '%1.5f',header ='| sr | P | error' )





