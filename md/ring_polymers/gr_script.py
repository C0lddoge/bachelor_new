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
        '--save_dir',
        type = str,
        default = './'
        )
parser.add_argument(
    '--bin_len',
    type = int,
    default = 0
        )
 
filename = vars(parser.parse_args())['file']
wish_name = filename.split('/')[2]
print(wish_name)
args = parser.parse_args()
data = cm.read_lammpstrj(filename,args.cutoff)
print(data[0]['xyz'])
L = data[0]['L']
N = len(data[0]['types'])
rho = N/(L**3)
xyz = [data[i]['xyz'] for i in range(len(data[:]))]
types = data[0]['types']
types = list(np.array(types)-1)
print(types)
pairs,r,g,error = cm.rad_dist_types(xyz,types,0.1,rho,args.bin_len)
for i in range(len(pairs)):
   # plt.plot(r[i],g[i])
   # plt.xlabel('r')
   # plt.ylabel(f'g_{pairs[i][0]}{pairs[i][1]}(r)')
  #  plot_name = args.save_dir + f'g_{pairs[i][0]}{pairs[i][1]}r.pdf'
    file_name = args.save_dir + '{:}_rdf_{:}{:}.dat'.format(wish_name,pairs[i][0],pairs[i][1])
#    plt.savefig(plot_name)
 #   plt.clf()
    cm.write_xy(file_name,(r[i],g[i],error[i]))




