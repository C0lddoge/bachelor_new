#!/usr/bin/env python3
import os
import numpy as np
import argparse
from matplotlib import pyplot as plt
import codemodule as cm
##### auxiliary functions
##### parsing the input

plt.style.use('bmh')
plt.rcParams.update({
       "text.usetex": True,
       "font.family": "sans-serif",
       "font.size": 20,
       "axes.titlesize": 20,
       "axes.labelsize": 20,
       "font.sans-serif": ["Helvetica"],
       "axes.facecolor": '#ffffff',
       "figure.autolayout": True,
           })




parser = argparse.ArgumentParser()
parser.add_argument(
            "--file",
            type = str,
            required = True,
            help = 'input .xyz file',
            )
parser.add_argument(
            "--Nlag",
            type = int,
            required = True,
            help = 'number of lag times logarithmicaly distributed from 1 to the number of frames',
            )
parser.add_argument(
            "--stride",
            default = 1,
            type = int,
            help = 'for a given lag time, average over 1/stride of all possible pairs',
            )
parser.add_argument(
            "--fig",
            default = 'fig.pdf',
            type = str,
            help = 'output file for the plot',
            )
parser.add_argument(
            "--type",
            default = '1',
            type = str,
            help = 'type of the particle we observe'
            )

parser.add_argument(
        '--cutoff',
        default = 0.0,
        type = float,
        help = 'set the percentage of frames cut from the beginning'
        )
parser.add_argument(
        '--integration_step',
        default = 1.0,
        type = float,
        help = 'set integration timestep, default will be 1 ie. units in steps'
        )
args = parser.parse_args()
frames = cm.read_lammpstrj(args.file,args.cutoff,args.stride)
frame_gap = frames[1]['timestep']-frames[0]['timestep']
##### the actual program
stride = args.stride
Nf = len(frames) # number of frames
Npart = len(frames[0]['types']) # number of particles
types = args.type
names = [int(i) for i in frames[0]['types']]
lag_times = sorted(list(set(np.logspace(0, np.log10(Nf - 1), num = args.Nlag, dtype = int)))) # lag times
max_tau = max(lag_times) # the largest lag time
unique,counts = np.unique(names,return_counts = True)
count_dict = dict(zip(unique,counts))
Npart_type = count_dict[int(types)]
MSDs = np.zeros((len(lag_times),Npart_type+2)) # init for the final output

# print data
print('\n ! MAKE SURE YOU HAVE UNFOLDED COORDINATES WITH UNIFORM TIMESTEP !\n')
print(' {:} particles'.format(Npart))
print(' {:} frames'.format(Nf))
print(' lag times', lag_times)
print(' {:} stride\n'.format(stride))

# MSD calculation


#print(types)
part_id = 0
for part in range(Npart):
  print(' calculating for the particle: {:}/{:}'.format(part, Npart), end = '\r')
  if names[part] == int(types):
    for l, lag in enumerate(lag_times):
      MSDs[l, 0] = lag*frame_gap*args.integration_step
      sample_accumulator = []
      for sample in range(0, Nf - lag, stride):
        dd = 0
        for dim in range(3):
          dx = frames[sample]['xyz'][part][dim] - frames[sample + lag]['xyz'][part][dim]
          dd += dx**2
        sample_accumulator.append(dd)
      MSDs[l, 2+part_id] = np.array(sample_accumulator).mean()
    part_id += 1

# take also the mean
MSDs[:,1] = MSDs[:,2:].mean(axis = -1)
print(np.shape(MSDs))
np.savetxt(f'./MSDs{types}.dat', MSDs, fmt = '%.3e', header = 'lag time | mean MSD | MSDs for each particle')
print()

# plot
plt.figure()
plt.grid()
plt.yscale('log')
plt.xscale('log')
plt.ylabel('MSD [$\\sigma^2$]')
plt.xlabel('lag time [steps]')
#for n in range(Npart_type):
 # plt.plot(lag_times, MSDs[:,n+2], color = 'blue', alpha = 0.1, linewidth = 0.3)
#plt.plot(lag_times, MSDs[:,1], linewidth = 2.0, alpha = 1.0, color = 'black', marker = 'o', markersize = 4)
#plt.savefig(args.fig)

exit()
