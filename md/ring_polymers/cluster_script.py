import numpy as np
import argparse
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
         required = True
          )
parser.add_argument(
      '--error_len',
      type = int,
      default = 0
          )
parser.add_argument(
        "--r_c",
        type = float,
        required = True,
        )
args = parser.parse_args() 
data = cm.read_lammpstrj(args.file,args.cutoff)
frames = []
types = data[0]['types']
L = data[0]['L']
print(L)
for i in range(len(data[:])):
    frames.append(data[i]['xyz'])

size,ratio,ratio_error, = cm.struct_ana(frames,types,L,args.r_c,error_len = args.error_len)
print('next')
size,makeup,makeup_error = cm.mu_ana(frames,types,L,args.r_c,error_len = args.error_len)
result = np.column_stack((size,ratio,makeup,ratio_error,makeup_error))
np.savetxt(args.save_path,result,fmt = '%1.5f',header = 'cluster size | weight fraction | make up | wf error | mu error')


