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
  line=f_in.readline()
  if line=='':
    return None
  N,frame = int(line),{}
  frame['comment']=f_in.readline()[:-1]
  types,xyz=[],[]
  for n in range(N):
    items=f_in.readline().split()
    types.append(items[0])
    xyz.append([float(item) for item in items[1:]])
  frame['types']=types
  frame['xyz']=np.array(xyz)
  return frame

def read_xyz(fn_in):
  '''
  read all frames from an open XYZ file
  `fn_in`: filename of the XYZ file
  '''
  frames=[]
  with open(fn_in) as f_in:
    while True:
      frame=read_xyz_frame(f_in)
      if not frame:
        break
      frames.append(frame)
    return frames

##### parsing the input
parser=argparse.ArgumentParser()
parser.add_argument("--file",type=str,required=True,help='input .xyz file')
parser.add_argument("--type",type=str,required=True,help='name of type')
parser.add_argument("--output",type=str,required=True,help='output .dat file')
parser.add_argument("--boxL",type=float,required=True,help='box length')
parser.add_argument("--qmax",required = True,type=int,help='magnitude of the largest qvector considered')
parser.add_argument("--stride",default=1,type=int,help='period with which we take the frames')
parser.add_argument("--discard",default=0.0,type=float,help='discard a fraction of the trajectory starting from the first frame')
args = parser.parse_args()

##### the actual program
frames=cm.read_lammpstrj(args.file,args.discard)
NFR=len(frames)
TYPE=int(args.type)
BOX_L=args.boxL
QMAX=args.qmax
QMAX2=QMAX*QMAX
TWO_PI_iL=2*np.pi/BOX_L
NA=frames[0]['types'].count(TYPE)
NPART=len(frames[0]['types'])
print('\n {:} frames selected for S(q) wit qmax {:} for:'.format(NFR,QMAX))
print(' type {:} with {:} particles'.format(TYPE,NA))

# loop over the frames
for f,frame in enumerate(frames):
  print(' running frame: {:d}/{:d}'.format(f+1,NFR),end='\r')
  Sqs=np.zeros(QMAX2)
  qvec_counts=np.zeros_like(Sqs,dtype=int)
  for qi in range(0,QMAX+1):
    for qj in range(-QMAX,QMAX+1):
      for qk in range(-QMAX,QMAX+1):
        n=qi*qi+qj*qj+qk*qk
        if (n>0) and (n<=QMAX2):
          Csum,Ssum=0.0,0.0
          for p in range(NA):
            if frame['types'][p]==TYPE:
              qr=TWO_PI_iL*(qi*frame['xyz'][p,0]+qj*frame['xyz'][p,1]+qk*frame['xyz'][p,2])
              Csum+=np.cos(qr)
              #print(Csum)
              Ssum+=np.sin(qr)
          Sqs[n-1]+=Csum*Csum+Ssum*Ssum
          qvec_counts[n-1]+=1
  # normalization
  if f==0:
    QLEN=np.count_nonzero(qvec_counts)
    Sq_dump=np.zeros((QLEN,2))
  counter=0
  for q in range(QMAX2):
    if qvec_counts[q]!=0:
      Sq_dump[counter,0]=TWO_PI_iL*np.sqrt(q+1)
      Sq_dump[counter,1]+=Sqs[q]/(NA*qvec_counts[q])/NFR
      counter+=1
np.savetxt(args.output,Sq_dump,fmt='%.5e',header='q | S(q)')
exit()
