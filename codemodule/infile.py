import numpy as np
import math


def write_data(N,density,filename):

    #generating atom positions
    N_total = np.sum(N)
    N_prime = math.ceil(N_total**(1/3))
    L = (N_total/density)**(1/3)
    a = L/N_prime
    counter = 0
    xyz = np.zeros((N_total,3))
    for i in range(N_prime):
        for j in range(N_prime):
            for k in range(N_prime):
                if counter < N_total:
                    xyz[counter,0] = a*(i+0.5)
                    xyz[counter,1] = a*(j+0.5)
                    xyz[counter,2] = a*(k+0.5)
                    counter += 1
  
    types = np.zeros(N_total, dtype = int)
    counter = 0
    for i in range(len(N)):
        for j in range(N[i]):
            types[counter] = i
            counter += 1

    #writing the file 
    
    with open(filename, 'x') as f:
        f.write('LAMMPS Simulation Data\n')
        f.write('{:} atoms\n'.format(N_total))
        f.write('{:} atom types\n'.format((len(N))))
        f.write('\n')
        f.write('0 {:} xlo xhi \n'.format(L))
        f.write('0 {:} ylo yhi \n'.format(L))
        f.write('0 {:} zlo zhi \n'.format(L))
        f.write('\n')
        f.write('Masses\n')
        f.write('\n')
        for i in range(len(N)):
            f.write('{:} 1.0\n'.format(int(i+1)))
        f.write('\n')
        f.write('Atoms\n')
        f.write('\n')
        for i in range(N_total):
            f.write('{:} {:} {:.8f} {:.8f} {:.8f}\n'.format(i+1,int(types[i]+1),xyz[i,0],xyz[i,1],xyz[i,2]))

    pass





