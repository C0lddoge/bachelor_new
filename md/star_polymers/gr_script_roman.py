#!/usr/bin/env python3
import numpy as np
import argparse
import codemodule as cm
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

def pbc_distance(r1, r2, L):
  '''
  calculate distance between two points in the periodic boundary conditions
  `r1`: (1,3) array of coordinates
  `r2`: (1,3) array of coordinates
  `L`: box length
  '''
  d2 = 0.0
  for k in range(3):
    dx = r1[k] - r2[k]
    dx -= L * round(dx / L)
    d2 += dx * dx
  return np.sqrt(d2)

##### parsing the input
parser = argparse.ArgumentParser()
parser.add_argument(
            "--file",
            type = str,
            required = True,
            help = 'input .xyz file',
            )
parser.add_argument(
            "--typeA",
            required = True,
            type = str,
            help = 'name of type A',
            )
parser.add_argument(
            "--typeB",
            required = True,
            type = str,
            help = 'name of type B',
            )
parser.add_argument(
            "--output",
            type = str,
            required = True,
            help = 'output .dat file',
            )
parser.add_argument(
            "--boxL",
            required = True,
            type = float,
            help = 'box length',
            )
parser.add_argument(
            "--stride",
            default = 1,
            type = int,
            help = 'period with which we take the frames',
            )
parser.add_argument(
            "--discard",
            default = 0.0,
            type = float,
            help = 'discard a fraction of the trajectory starting from the first frame',
            )
parser.add_argument(
            "--width",
            default = 0.5,
            type = float,
            help = 'bin width for g(r)',
            )
args = parser.parse_args()

##### the actual program
frames = cm.read_lammpstrj(args.file)
frames = frames[int(args.discard*len(frames)):-1:args.stride] # discard the equilibration and apply the stride
Nf = len(frames) # new number of frames
L = args.boxL
width = args.width
typeA = int(args.typeA)
typeB = int(args.typeB)
Nbins = int((L/2) // width) # number of bins
NA = frames[0]['types'].count(typeA) # number of type A particles
NB = frames[0]['types'].count(typeB) # number of type B particles
Npart = len(frames[0]['types']) # number of particles
final_gr = np.zeros(Nbins) # accumulator across the frames

# print data
print('\n {:} frames selected for g(r) between:'.format(Nf))
print(' type {:} with {:} particles'.format(typeA, NA))
print(' type {:} with {:} particles'.format(typeB, NB))
print(' {:} bins with width {:}\n'.format(Nbins, width))

# loop over the frames
test_file = open('test_file','x')
for f, frame in enumerate(frames):
  print(' running frame: {:d}/{:d}'.format(f+1, Nf), end = '\r')
  types = frame['types']
  xyz = frame['xyz']
  distances = []
  # select relevant pair distances
  for i in range(Npart):
    for j in range(Npart):
      if types[i] == typeA and types[j] == typeB and i != j:
        distances.append(pbc_distance(xyz[i,:], xyz[j,:], L))

  # calculate the histogram

  bins, edges = np.histogram(distances, range = (0, L/2), bins = Nbins, density = False)
  bins = bins.astype(float) # convert from int to float to enable reassignment
  centers = (edges[1:] + edges[:-1]) / 2
  volumes = 4 / 3 * np.pi * (edges[1:]**3 - edges[:-1]**3)
  # normalize and add to the accumulator
  bins /= (volumes * NA * NB / L**3)
  print(bins)
  test_file.write('{:};{:}\n'.format(centers[0],bins[0]))
  final_gr += (bins / Nf)

print()
np.savetxt(args.output, np.vstack((centers, final_gr)).T, fmt = '%.3e', header = 'r | <g(r)>')
exit()
