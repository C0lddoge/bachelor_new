import argparse
import numpy as np
import codemodule as cm
import os
parser = argparse.ArgumentParser()


parser.add_argument(
        "--file",
        type = str,
        required = True,
        )
parser.add_argument(
        "--save_path",
        type = str,
        default = './diff_coeff'
        )
parser.add_argument(
        "--t1",
        type = float,
        default = 0.0
        )
parser.add_argument(
        "--t2",
        type = float,
        default = 0.0
        )
parser.add_argument(
        "--L",
        type = float,
        required = True
        )
parser.add_argument(
        "--R_g",
        type = float,
        default = 1.0

        )
args = parser.parse_args()
time_range = [args.t1,args.t2]
data = np.loadtxt(args.file)
data[:,1:] = data[:,1:]/(args.R_g**2)
if not os.path.isfile(args.save_path):
    f = open(args.save_path,'x')
    f.write('#Boxsize | D | error | \n')
else:
    f = open(args.save_path,'a')
if all(time_range) == 0.0:
    time_range = [data[0,0],data[-1,0]]
    diff_data = cm.diff_coeff(data,time_range)
    save_data = np.array([args.L,diff_data['D'],diff_data['D_err']])
    print(f'L = {args.L}')
    print(f'alpha = {diff_data["alpha"]} ; D = {diff_data["D"]}')
    #print(save_data)
    np.savetxt(f,save_data.reshape(1,save_data.shape[0]), fmt = "%.5f")
else:
    diff_data = cm.diff_coeff(data,time_range)
    save_data = np.array([args.L,diff_data['D'],diff_data['D_err']])
    print(f'alpha = {diff_data["alpha"]} ; D = {diff_data["D"]}')
    np.savetxt(f,save_data.reshape(1,save_data.shape[0]), fmt = "%.5f")



