import numpy as np
import numba as nb
from .numeric_pot_mc import d_matrix
from .radial_density import g_r_error



def structure_fac(frames,types,pair0,pair1,rho):
    pair = (pair0,pair1)
    N_types = np.unique(types, return_counts = True)[1]
    N_total = len(types)
    L = (N_total/rho)**(1/3)

    q_base = 2*np.pi/L
    qs = [q_base]
    prefac = [1,np.sqrt(2),np.sqrt(3)]
    i = 1
    while qs[-1] <= 8*q_base:
        q_i = (i//3 + 1)*prefac[i%3] * q_base
        qs.append(q_i)
        i = i+1
    qs = np.sort(qs)
    
    d_arr_idx = []
    for i in range(N_total):
        for j in range(N_total):
            if (types[i],types[j]) == pair and i!=j:
                d_arr_idx.append((i,j))

    S_frames = []
    for i in range(len(frames)):
        print(f'{i}/{len(frames)}')
        d_arr = d_matrix(frames[i].T,L)
        rs = []
        for j in d_arr_idx:
                rs.append(d_arr[j])
        

        S = []
        for q in qs:
            summation = 0
            for r in rs:
                summation = summation + np.sin(q*r)/(q*r)
            S.append(summation)

        S = np.array(S)
        S = 1/(np.sqrt(np.prod(N_types)))  * S
        S_frames.append(S)
    error = g_r_error(S_frames)
    S = np.mean(S_frames, axis = 0)

    return qs, S 


@nb.jit(nopython = True)            
def term(q,r):
    return np.sin(q*r)/(q*r)

    

        








