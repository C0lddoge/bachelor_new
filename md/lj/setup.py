import codemodule as cm
import argparse 
import os


parser = argparse.ArgumentParser()
parser.add_argument(
   '--N',
   nargs = '+',
   type = int,
   required = True,
        )
parser.add_argument(
    '--density',
    type = float, 
    required = True
        )


args = parser.parse_args()

dir_name = 'RP_N{:}_rho{:}'.format(*args.N,args.density)
if not os.path.isdir(dir_name):
    os.mkdir(dir_name)


Ns = list(args.N)
for n in Ns:
    if n == 0:
        Ns.remove(0)
cm.write_data(Ns,args.density,dir_name + '/indata.in')



