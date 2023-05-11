#!/usr/bin/env python3
import os
import numpy as np
import argparse
from matplotlib import pyplot as plt

##### auxiliary functions
def read_xyz_frame(f_in):
  '''
  read a single xyz frame from an open XYZ file
  `f_in`: opened XYZ file
  '''
  line = f_in.readline()
  if line == '':
    return None
  N = int(line)
  comment = f_in.readline()[:-1]
  names = []
  data = []
  for i in range(N):
    items = f_in.readline().split()
    names.append(items[0])
    data.append([float(item) for item in items[1:]])
  return comment, names, np.array(data)

def read_xyz(fn_in):
  '''
  read all frames from an open XYZ file
  `fn_in`: filename of the XYZ file
  '''
  frames = []
  with open(fn_in) as f_in:
    while True:
      frame = read_xyz_frame(f_in)
      if not frame:
        break
      frames.append(frame)
    return frames

##### parsing the input
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
args = parser.parse_args()

##### the actual program
frames = read_xyz(args.file)
stride = args.stride
Nf = len(frames) # number of frames
Npart = len(frames[0][1]) # number of particles

lag_times = sorted(list(set(np.logspace(0, np.log10(Nf - 1), num = args.Nlag, dtype = int)))) # lag times
max_tau = max(lag_times) # the largest lag time
MSDs = np.zeros((len(lag_times), Npart+2)) # init for the final output

# print data
print('\n ! MAKE SURE YOU HAVE UNFOLDED COORDINATES WITH UNIFORM TIMESTEP !\n')
print(' {:} particles'.format(Npart))
print(' {:} frames'.format(Nf))
print(' lag times', lag_times)
print(' {:} stride\n'.format(stride))

# MSD calculation
for part in range(Npart):
  print(' calculating for the particle: {:}/{:}'.format(part+1, Npart), end = '\r')
  for l, lag in enumerate(lag_times):
    MSDs[l, 0] = lag
    sample_accumulator = []
    for sample in range(0, Nf - lag, stride):
      dd = 0
      for dim in range(3):
        dx = frames[sample][2][part][dim] - frames[sample + lag][2][part][dim]
        dd += dx**2
      sample_accumulator.append(dd)
    MSDs[l, 2+part] = np.array(sample_accumulator).mean()

# take also the mean
MSDs[:,1] = MSDs[:,2:].mean(axis = -1)
np.savetxt('./MSDs.dat', MSDs, fmt = '%.3e', header = 'lag time | mean MSD | MSDs for each particle')
print()

# plot
plt.figure()
plt.grid()
plt.yscale('log')
plt.xscale('log')
plt.ylabel('mean square displacement')
plt.xlabel('stride')
plt.style.use('seaborn')
for n in range(Npart):
  plt.plot(lag_times, MSDs[:,n+2], color = 'blue', alpha = 0.1, linewidth = 0.3)
plt.plot(lag_times, MSDs[:,1], linewidth = 2.0, alpha = 1.0, color = 'black', marker = 'o', markersize = 4)
plt.savefig(args.fig)

exit()
