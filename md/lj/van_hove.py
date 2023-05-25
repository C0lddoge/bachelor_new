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
        '--error_len',
        type = int,
        default = 0
        )
parser.add_argument(
        '--lag',
        type = int,
        default = 10,
        )
parser.add_argument(
        '--types',
        type = str,
        default = 'all'
        )
parser.add_argument(
        '--bin_low',
        type = float,
        required = True
        ) 
parser.add_argument(
        '--bin_high',
        type = float,
        required = True
        )
parser.add_argument(
        '--bin_number',
        type = int,
        default = 1000
        )
filename = vars(parser.parse_args())['file']
args = parser.parse_args()
data = cm.read_lammpstrj(filename,args.cutoff)
r,van,error = cm.van_hoft(data,args.lag,args.bin_number,[args.bin_low,args.bin_high],args.types,args.error_len)
np.savetxt(args.save_path,np.column_stack((r,van,error)),fmt = '%1.5f',header ='| r | G_s | error' )





