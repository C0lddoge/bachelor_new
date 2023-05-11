#!/usr/bin/env python3
import numpy as np

def read_lammpstrj_frame(f_in):
  '''
  read one frame of .lammpstrj trajectory from a file object
  '''
  line = f_in.readline()
  if line == '':
    return None
  timestep = int(f_in.readline())
  f_in.readline()
  N = int(f_in.readline())
  f_in.readline()
  for k in range(3):
    lohi = f_in.readline().split(' ')
    lo, hi = map(float, lohi)
    L = abs(lo) + abs(hi)
  f_in.readline()
  pos, types, ids, images = [], [], [], []
  for i in range(N):
    line = f_in.readline().split('\n')[0].split(' ')
    ids.append(int(line[0]))
    types.append(int(line[1]))
    xs, ys, zs = map(float, line[2:5])
    ix, iy, iz = map(int, line[5:8])
    pos.append([(xs + ix) * L, (ys + iy) * L, (zs + iz) * L])

  frame = {}
  frame['L'] = L
  frame['timestep'] = timestep
  frame['ids'] = ids
  frame['types'] = types
  frame['xyz'] = np.array(pos)

  return frame

def read_lammpstrj(fn_in, discard = 0.00, stride = 1):
  '''
  read lammps trajectory from a custom .lammpstrj file and filter it
  '''
  assert discard >= 0 and discard < 1 and isinstance(stride, int)
  frames = []
  with open(fn_in) as f_in:
    while True:
      frame = read_lammpstrj_frame(f_in)
      if not frame:
        break
      frames.append(frame)

  N_frames = len(frames)
  frames = frames[int(N_frames*discard)::stride]
  print('{:} frames with {:} discard and {:} stride gives back {:} frames'.format(N_frames, discard, stride, len(frames)))
  return frames





